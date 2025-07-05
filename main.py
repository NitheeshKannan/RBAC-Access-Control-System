from module.auth import signup,login,reactivate,deactivate
def main():
    while True:
        try:
            print("RBAC SYSTEM CLI PAGE")
            print("1.login")
            print("2.signup")
            print("3.deactivate")
            print("4.reactivate")
            print("5.exit")

            choice=int(input("Enter your choice: "))

            if choice==1:
                user_name=input("enter the username: ")
                password=input("enter your password: ")
                login(user_name,password)
            elif choice==2:
                user_name=input("Enter your username: ")
                password=input("Enter your password: ")
                signup(user_name,password)
            elif choice==3:
                user_id=input("Enter your user id: ")
                if user_id.isdigit():
                    deactivate(user_id)
                else:
                    print('Invalid user id')
            elif choice==4:
                user_id=input("Enter your user id: ")
                if user_id.isdigit():
                    reactivate(user_id)
                else:
                    print('Invalid user id')
            elif choice==5:
                print("exiting bye")
                break
            else:
                print("Invalid choice")
        except ValueError:
            print("Invalid choice")
if __name__ == '__main__':
    main()
