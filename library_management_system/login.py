from models import User
from manager import UserManager


def login_menu(user_name, user_phonenumber):
    manager = UserManager()
    while True:
        try:
            login_menu_input = int(
                input("1-Login\n2-Register\n3-Exit\n"))
        except ValueError:
            print("Enter only numbers")
            continue
        if login_menu_input == 1:
            login_success = manager.login_user(user_phonenumber)

            if login_success:
                print("Login Successfull")
                return True
            else:
                return False

        elif login_menu_input == 2:

            print("====User Register====")

            if not user_phonenumber.isdigit() or len(user_phonenumber) != 10:
                print("Enter a Valid Phone number\n")
                continue

            user = User(user_name, user_phonenumber)

            success = manager.register_user(user)

            
            if success:
                manager.save_user()
                print("User Registered Successfully")
                print("Please Login")
                break
            else:
                print("User Exist")
                return False

        elif login_menu_input == 3:
            break
