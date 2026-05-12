from auth import register,login

def main():

    while True:
        print("\nMenu:")
        print("1.Register")
        print("2.Login:")
        print("3.Exit")

        option = input("Enter an option: ")

        if option == '1':
            register()
        elif option == '2':
            login()
        elif option == '3':
            print("Exit from login...............")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
