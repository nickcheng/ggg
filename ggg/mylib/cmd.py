def git_commit(message):
    result = f'git commit --no-verify -m"{message}"'
    return result

def git_recent_branches():
    result = f"git branch --sort=-committerdate"
    return result

def git_checkout(branch_name):
    result = f'git checkout "{branch_name}"'
    return result

def git_recent_release_branches():
    result = f"git branch -r --sort=-committerdate | grep release"
    return result