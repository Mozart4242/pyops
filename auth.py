import hashlib
from configparser import ConfigParser
from getpass import getpass

def auth():
    logged_in = False
    while logged_in is not True:
        print("🔐 Please Log in")
        username = input("Username: ")
        password = getpass(prompt='Password: ', stream=None)
        hash_password = hashlib.md5(password.encode())
        hash_password = hash_password.hexdigest()

        config_object = ConfigParser()
        config_object.read("config.ini")
        userinfo = config_object["USERINFO"]

        if username == userinfo["username"] and hash_password == userinfo["password"]:
            print("🔓 Successfully logged in")
            logged_in = True
            break
    return logged_in