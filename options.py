import pyfiglet
import settings
import time
from progressbar import progressbar
from modules import git, terraform, install
from stringcolor import cs


menu_options = {
    1: 'Get my system ready 🛠',
    2: 'Git',
    3: 'Terraform',
    9: 'Settings',
    0: 'Exit '
}


def print_bar():
    for i in progressbar(range(100)):
        time.sleep(0.01)
    input(cs("💲 Press any button to get back to the main menu >").bold())


def print_menu():
    banner = pyfiglet.figlet_format("PyOps  v1 . 0")
    print(banner, "<<✅ This is going to auto setup these modules >>")
    for key in menu_options.keys():
        print(key, '->', menu_options[key])


def option1():
    install.install()
    input(cs("💲 Press any button to get back to the main menu >").bold())


def option2():
    git.ssh_key_generate()
    input(cs("💲 Press any button to get back to the main menu >").bold())


def option3():
    pass
    input(cs("💲 Press any button to get back to the main menu >").bold())


def option9():
    settings.update_config()
    input(cs("💲 Press any button to get back to the main menu >").bold())
