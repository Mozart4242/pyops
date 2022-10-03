from configparser import ConfigParser
import options
import hashlib


def update_config():
    config_object = ConfigParser()
    config_object.read("config.ini")
    userinfo = config_object["USERINFO"]
    git = config_object["GIT"]
    aws = config_object["AWS"]

    USERINFO_username = str(input("PyOps login id: "))
    USERINFO_password = str(input("PyOps password: "))
    hash_password = hashlib.md5(USERINFO_password.encode())
    hash_password = hash_password.hexdigest()
    GIT_username = str(input("Github Username: "))
    GIT_password = str(input("Github Password: "))
    AWS_acc_key_id = str(input("AWS Access Key ID: "))
    AWS_secret_acc_key = str(input("AWS Secret Access Key: "))
    AWS_reg = str(input("AWS Default region: (default: us-east-1):")
                  or "us-east-1")
    AWS_out = str(
        input("AWS Default output format (default: json):") or "json")

    userinfo["username"] = USERINFO_username
    userinfo["password"] = hash_password
    git["username"] = GIT_username
    git["password"] = GIT_password
    aws["Access-Key-ID"] = AWS_acc_key_id
    aws["Secret-Access-Key"] = AWS_secret_acc_key
    aws["Default-region"] = AWS_reg
    aws["Default-output"] = AWS_out

    with open('config.ini', 'w') as conf:
        config_object.write(conf)

    options.print_bar()
