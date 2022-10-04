from configparser import ConfigParser
from progressbar import progressbar
import os
from stringcolor import cs

def menu():
    menu_options = {
        1: 'Docker',
        2: 'Kubernetes',
        3: 'AWS'
    }
    print("Choose a resource to configure:")
    for key in menu_options.keys():
        print("|Terraform|",key, '->', menu_options[key])
        
    try:
        option = int(input('📌 Enter your choice: '))
        if option == 1:
            docker()
        elif option == 2:
            kubernetes()
        elif option == 3:
            aws()
        else:
            print('❗ Invalid option. Please enter a valid number ❗')
    except ValueError:
        print("❗ Invalid option. Please enter a valid number ❗")


    
def docker():
    pass

def kubernetes():
    pass

def aws():
    pass