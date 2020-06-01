import colorama
from colorama import Fore, Back, Style

def init():
    colorama.init()

def print_color(color, text):
    print(color + text + Style.RESET_ALL)

def print_green(text):
    print_color(Fore.GREEN, text)

def print_red(text):
    print_color(Fore.RED, text)