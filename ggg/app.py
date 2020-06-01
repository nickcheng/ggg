import click
import inquirer

from . import config
from .mylib import cmd
from .mylib.shell import run
from .mylib import colorprint
from .mylib.colorprint import print_green, print_red

@click.group()
def cli():
    colorprint.init()
    pass

@cli.command("pr", help="[WIP] Send pull-request interactively.")
def pull_request():
    to_run = cmd.git_recent_release_branches()
    result = run(to_run)

    if result[0] > 0:
        print_red(f"Return Code: {result[0]}")
        print(result[1])
        print(result[2])
        return

    branch_list = [i.strip() for i in result[1].split("\n")]
    branch_list.insert(0, "develop")

    questionBranch = [
        inquirer.List(
            'branch',
            message = "Which branch to send PR?",
            choices = branch_list,
        ),
    ]
    answerScope = inquirer.prompt(questionBranch)

    # Input title
    # Input JIRA Ticket
    # 
    # hub pull-request -b {base branch} --edit --copy --message {xx}
    return

@cli.command("rb", help="Switch among recent branches.")
def recent_branches():
    to_run = cmd.git_recent_branches()
    result = run(to_run)

    if result[0] > 0:
        print_red(f"Return Code: {result[0]}")
        print(result[1])
        print(result[2])
        return

    branch_list = [i.strip() for i in result[1].split("\n")]
    current_branch = [i for i in branch_list if i.startswith("*")]
    if current_branch:
        branch_name = current_branch[0][2:]
        print_green(f"Current branch: {branch_name}")

    other_branches = [i for i in branch_list if not i.startswith("*") and i]

    # print(branch_list)
    # List Recent Branches
    questionBranch = [
        inquirer.List(
            'branch',
            message = "Which branch to checkout?",
            choices = other_branches,
        ),
    ]
    answerScope = inquirer.prompt(questionBranch)

    to_run = cmd.git_checkout(answerScope["branch"])
    print("Gonna run:")
    print_green(to_run)
    if not continue_run():
        print("🍵 Cancelled!")
        return

    # Run Command
    result = run(to_run)
    if result[0] > 0:
        print_red(f"Return Code: {result[0]}")
    else:
        print_green("Succeeded!")
    print(result[1])
    print(result[2])

@cli.command("c", help="Make semantic git commit.")
def commit():
    # Commit Type
    questionType = [
        inquirer.List(
            'type',
            message = "Commit Type?",
            choices = config.COMMIT_TYPE_LIST,
        ),
    ]
    answerType = inquirer.prompt(questionType)

    # Commit Scope
    questionScope = [
        inquirer.List(
            'scope',
            message = "Commit Scope?",
            choices = config.COMMIT_SCOPE_LIST,
        ),
    ]
    answerScope = inquirer.prompt(questionScope)

    # Commit Description
    questionDescription = [
        inquirer.Text(
            'description',
            message = "Commit Description?(required)",
            validate = lambda _, x: len(x.strip()) > 0
        ),
    ]
    answerDescription = inquirer.prompt(questionDescription)

    # Generate Commit Message
    commit_message = answerType["type"]
    if answerScope["scope"] != -1:
        commit_message += f"({answerScope['scope']})"
    commit_message += ": "
    commit_message += answerDescription["description"]

    # Confirm to run the command
    to_run = cmd.git_commit(commit_message)
    print("Gonna run:")
    print_green(to_run)
    if not continue_run():
        print("🍵 Cancelled!")
        return

    # Run Command
    result = run(to_run)
    if result[0] > 0:
        print_red(f"Return Code: {result[0]}")
    else:
        print_green("Succeeded!")
    print(result[1])
    print(result[2])

    print("🍺 Done!")

def continue_run():
    questionConfirm = [
        inquirer.Confirm("continue", message = "Should I continue?", default = False),
    ]
    answerConfirm = inquirer.prompt(questionConfirm)
    return answerConfirm["continue"]

if __name__ == '__main__':
    cli()
    