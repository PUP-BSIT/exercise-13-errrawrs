def display_menu():
    print("Greetings Michael Angelo P. Mosquito")
    print("1. Basic info")
    print("2. Goals ")
    print("3. comment simone")
    print("4. comment gerald")
    print("5. comment ivan")
    print("6. comment daniel")
    print("7. Exit")

def basic_info():
    print("Name: Michael Angelo P. Mosquito")
    print("Age: 19 years old")
    print("Birthday: June 8, 2005")
    print("Education: Second-year student at PUP-Taguig")

def goal():
    print("Become a skilled programmer by the end of 2025")
    print("\n")

def simone_comment():
    print("Don't fear errors—they guide you to greatness.")

def gerald_comment():
    print("Hope your code is compiling without errors today!")

def ivan_comment():
    print("The only limit is your imagination.")

def daniel_comment():
    print("The clarity of your documentation is a lifesaver!")

def menu_function():

    while True:
        display_menu()

        choice = input("Enter your choice: ")

        if choice == "1":
            print("\n")
            print(basic_info())
        elif choice == "2":
            print("\n")
            print(goal())
        elif choice == "3":
            print("\n")
            print(simone_comment())
        elif choice == "4":
            print("\n")
            print (gerald_comment())
        elif choice == "5":
            print("\n")
            print(ivan_comment())
        elif choice == "6":
            print("\n")
            print(daniel_comment())
        elif choice == "7":
            print("\n")
            print("Exiting....")
            break
        else:
            print("\n")
            print("Invalid choice!!!")