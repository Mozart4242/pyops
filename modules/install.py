import os
import time
from progressbar import progressbar


def __bar(name):
    print(f"🔹 ... Installing {name} ... 🔹")
    for i in progressbar(range(100)):
        time.sleep(0.005)
    print("✅ Installed ✅")


def __check_package():
    items = {}
    git_check = os.system('which git')
    if git_check == 0:
        items["Git"] = "Installed"
    elif git_check == 256:
        items["Git"] = "Not installed"

    aws_check = os.system('which aws')
    if aws_check == 0:
        items["AWS"] = "Installed"
    elif aws_check == 256:
        items["AWS"] = "Not installed"

    terraform_check = os.system('which terraform')
    if terraform_check == 0:
        items["Terraform"] = "Installed"
    elif terraform_check == 256:
        items["Terraform"] = "Not installed"

    for item in items:
        print(item, items[item])


def install():
    print("🛠  This will installs or update packages on your machine 🛠")
    x = os.system('which dpkg > /dev/null 2>&1')
    if x == 0:
        os.system('apt update > /dev/null 2>&1')
        os.system(
            'apt install apt-transport-https ca-certificates gnupg software-properties-common -y> /dev/null 2>&1')
        __bar("Prerequisite")

        os.system('apt install git -y > /dev/null 2>&1')
        __bar("Git")

        CMD = 'curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "/tmp/awscliv2.zip" > /dev/null 2>&1 \
        && unzip /tmp/awscliv2.zip > /dev/null 2>&1\
        && ./tmp/aws/install -b /usr/local/bin -i /usr/local/aws-cli > /dev/null 2>&1'
        os.system(CMD)
        __bar("AWS CLI")

        CMD = 'wget -O- https://apt.releases.hashicorp.com/gpg | \
        gpg --dearmor | \
        tee /usr/share/keyrings/hashicorp-archive-keyring.gpg > /dev/null 2>&1'
        os.system(CMD)
        CMD = 'echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] \
        https://apt.releases.hashicorp.com $(lsb_release -cs) main" | \
        tee /etc/apt/sources.list.d/hashicorp.list > /dev/null 2>&1'
        os.system(CMD)
        os.system(
            'apt update > /dev/null 2>&1 && apt install terraform -y > /dev/null 2>&1')
        __bar("Terraform")

        __check_package()
    else:
        os.system('yum update > /dev/null 2>&1')
        os.system('yum install git -y > /dev/null 2>&1')
        __bar("Git")

        os.system('yum install -y yum-utils > /dev/null 2>&1')
        CMD = 'yum-config-manager --add-repo https://rpm.releases.hashicorp.com/RHEL/hashicorp.repo > /dev/null 2>&1'
        os.system(CMD)
        os.system('yum -y install terraform > /dev/null 2>&1')
        __bar("Terraform")

        __check_package()
