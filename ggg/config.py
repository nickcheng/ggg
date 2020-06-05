COMMIT_SCOPE_LIST = [
    ("<<skip>>", -1),
    "Parser",
    "Router",
    "WeatherForecast",
    "SplashScreen",
]

COMMIT_TYPE_LIST = [
    "fix",
    "feat",
    "chore",
    "refactor",
    "test",
    "ci",
    "docs",
    "style",
    "perf",
    "build",
    "BREAKING CHANGE",
]

import os
import toml

CONFIG_FILE_NAME = ".ggg"
proj_config_file_path = os.path.expanduser(f"{os.getcwd()}/{CONFIG_FILE_NAME}")
sys_config_file_path = os.path.expanduser(f"~/{CONFIG_FILE_NAME}")

if os.path.exists(proj_config_file_path):
    file_path = proj_config_file_path
    print("Found project configuration file. Gonna use it.")
elif os.path.exists(sys_config_file_path):
    file_path = sys_config_file_path
    print("Found system configuration file. Gonna use it.")
else:
    file_path = ""

if file_path:
    try:
        t = toml.load(file_path)
        
        scope_list = t.get("commit_scope")
        if scope_list:
            COMMIT_SCOPE_LIST = [COMMIT_SCOPE_LIST[0]] + scope_list
            # print(COMMIT_SCOPE_LIST)
        
        type_list = t.get("commit_type")
        if type_list:
            COMMIT_TYPE_LIST = type_list
    except FileNotFoundError:
        file_not_found_exit()
else:
    file_not_found_exit()
        
def file_not_found_exit():
    print("No configuration file found under HOME directory.")
    print("Going to use default settings.")
