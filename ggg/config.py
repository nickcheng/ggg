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
file_path = os.path.expanduser(f"~/{CONFIG_FILE_NAME}")

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
    print("No configuration file found under HOME directory.")
    print("Going to use default settings.")
    
