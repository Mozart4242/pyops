from configparser import ConfigParser
from progressbar import progressbar
from stringcolor import cs
import terraform


def menu():
    menu_options = {
        1: 'Docker',
        2: 'Kubernetes',
        3: 'AWS'
    }
    print("Choose a resource to configure:")
    for key in menu_options.keys():
        print("|Terraform|", key, '->', menu_options[key])

    try:
        option = int(input('📌 Enter your choice: '))
        if option == 1:
            terraform.docker()
        elif option == 2:
            pass
        elif option == 3:
            pass
        else:
            print('❗ Invalid option. Please enter a valid number ❗')
    except ValueError:
        print("❗ Invalid option. Please enter a valid number ❗")
