def menu():
    print("Hello, Ivan V. Delumen")
    print("1)Basic Information")
    print("2) Goals")
    print("3) Comment from Mamasalanang")
    print("4) Comment from Mosquito")
    print("5) Comment from Reyes")
    print("6) Comment from Victorioso")
    print("7: Exit")
    
def basic_info():
    print("Name: Ivan V. Delumen")
    print("Age: 20")
    print("Birthdate: October 28, 2004")
    print("Hometown: Taguig City")

def goals():
    print("I want to be a front end developer.")
    print("To be a successful person.")

def comment_mamasalanang():
    print("")

def comment_mosquito():
    print("")

def comment_reyes():
    print("Hello I'm Simone Jake D. Reyes. I'a one of Ivan's groupmates")

def comment_victorioso():
    print("")

def menu_function():
    while True: 
        menu()

        user_choice = input("Enter your choice: ")

        if user_choice == "1":
            basic_info()
        elif user_choice == "2":
            goals()
        elif user_choice == "3":
            comment_mamasalanang()
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