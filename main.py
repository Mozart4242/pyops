import options
import auth
import os


logged_in = auth.auth()

while logged_in is True:
    options.print_menu()
    try:
        option = int(input('📌 Enter your choice: '))
        if option == 1:
            options.option1()
        elif option == 2:
            options.option2()
        elif option == 3:
            options.option3()
        elif option == 4:
            options.option4()
        elif option == 9:
            options.option9()
        elif option == 0:
            break
        else:
            print('❗ Invalid option. Please enter a valid number ❗')
    except ValueError:
        print("❗ Invalid option. Please enter a valid number ❗")
