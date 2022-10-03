import pyfiglet
import settings
import time
from progressbar import progressbar
from git.git import *
from packages.install import *

menu_options = {
    1: 'Get my system ready 🛠',
    2: 'Git',
    3: 'AWS',
    9: 'Settings',
    0: 'Exit '
}


def print_bar():
    for i in progressbar(range(100)):
        time.sleep(0.01)
    input("Press any button to get back to the main menu >")


def print_menu():
    banner = pyfiglet.figlet_format("PyOps  v1 . 0")
    print(banner, "<<✅ This is going to auto setup these modules >>")
    for key in menu_options.keys():
        print(key, '->', menu_options[key])


def option1():
    install()
    input("💲 Press any button to get back to the main menu >")


def option2():
    pass
    input("💲 Press any button to get back to the main menu >")


def option3():
    pass
    input("Press any button to get back to the main menu >")


def option9():
    settings.update_config()
    input("Press any button to get back to the main menu >")
