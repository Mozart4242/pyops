import options


def test():
    x = options.print_menu()
    if x:
        return True
    else:
        print("Falseee")
        return False
