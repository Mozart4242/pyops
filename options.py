import pyfiglet
import settings
import time
import os
from progressbar import progressbar
from modules import git, terraform, install, aws
from stringcolor import cs


menu_options = {
    1: 'Get my system ready 🛠',
    2: 'Git',
    3: 'Terraform',
    4: 'aws',
    9: 'Settings',
    0: 'Exit'
}


def print_bar():
    for i in progressbar(range(100)):
        time.sleep(0.01)
    input(cs("💲 Press enter to get back to the main menu >", "blue").bold())


def print_menu():
    banner = pyfiglet.figlet_format("PyOps  v1 . 0")
    print(banner, "<<✅ This is going to auto setup these modules >>")
    for key in menu_options.keys():
        print(key, '->', menu_options[key])


def option1():
    priv = os.getuid()
    if priv != 0:
        raise Exception(cs("Please Run the program as root", "red"))
    install.install()
    input(cs("💲 Press enter to get back to the main menu >", "blue").bold())


def option2():
    git.ssh_key_generate()
    input(cs("💲 Press enter to get back to the main menu >", "blue").bold())


def option3():
    terraform.menu()

    input(cs("💲 Press enter to get back to the main menu >", "blue").bold())


def option4():
    input("This is going to generate the AWS configuration file, press ENTER to continue...")
    aws.create_file()
    print_bar()


def option9():
    settings.update_config()
    print_bar()
