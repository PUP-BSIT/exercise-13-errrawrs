def menu():
    print("Hello, Gerald K. Mamasalanang")
    print("1)Basic Information")
    print("2) Goals")
    print("3) Comment from Ivan")
    print("4) Comment from Mosquito")
    print("5) Comment from Reyes")
    print("6) Comment from Victorioso")
    print("7: Exit")
    
def basic_info():
    print("Name: Gerald K. Mamasalanang")
    print("Age: 19")
    print("Birthdate: October 26, 2005")
    print("Hometown: Taguig City")

def goals():
    print("My goal is to be successful cyber security expert.")
    print("To be a successful person.")

def comment_ivan():
    print("Code smart, debug smarter!")

def comment_mosquito():
    print("")

def comment_reyes():
    print("")

def comment_victorioso():
    print("Be happy in your life. Good luck to your journey!")

def menu_function():
    while True: 
        menu()

        user_choice = input("Enter your choice: ")

        if user_choice == "1":
            basic_info()
        elif user_choice == "2":
            goals()
        elif user_choice == "3":
            comment_ivan()
        elif user_choice == "4":
            comment_mosquito()
        elif user_choice == "5":
            comment_reyes
        elif user_choice == "6":
            comment_victorioso()
        elif user_choice == "7":
            print("Exit.")
            break
        else: 
            print("Invalid Input!")