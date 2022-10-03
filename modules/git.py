from configparser import ConfigParser
from progressbar import progressbar
import os
import time
from stringcolor import cs


def ssh_key_generate():
    config_object = ConfigParser()
    config_object.read("config.ini")
    git = config_object["GIT"]
    git_username = git["username"]
    OS_USER = os.getenv("USER")
    if git_username == '':
        print(cs("git username (Email) is not defined, set it now", "red").bold())
        git_username = input(">> ")
        git["username"] = git_username
        with open('config.ini', 'w') as conf:
            config_object.write(conf)

    os.system(f'ssh-keygen -t ed25519 -C "{git_username}"')
    with open(f'/home/{OS_USER}/.ssh/id_ed25519.pub', 'r') as file:
        key = file.read()

    for i in progressbar(range(100)):
        time.sleep(0.01)
    print(cs("🔑🔑🔑 Your SSH-KEY is:🔑🔑🔑", "blue").bold())
    print(cs(key, "purple"))
