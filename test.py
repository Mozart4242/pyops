import os
from struct import iter_unpack
import time
from progressbar import progressbar


# x == 0 -> success
# x == 256 -> no output
# x == 32512 -> error command
# os.waitstatus_to_exitcode(x)

def check_package():
    items = {}
    git_check = os.system('which git')
    if git_check == 0:
        items["Git"] = "Installed"
    aws_check = os.system('which aws')
    if aws_check == 0:
        items["AWS"] = "Installed"
    terraform_check = os.system('which terraform')
    if terraform_check == 0:
        items["Terraform"] = "Installed"
    
    for item in items:
        print(item ,items[item])
    

check_package()
