from package.mamasalanang import menu_function as mamasalanang_main
from package.reyes import main as reyes_main
from package.victorioso import menu_function as victorioso_main
from package.mosquito import menu_function as mosquito_main

def menu_members():
    print("Welcome! Select a Person!")
    print("1. Ivan Delumen")
    print("2. Gerald Mamasalanang")
    print("3. Michael Angelo Mosquito")
    print("4. Simone Jake Reyes")
    print("5. Daniel Victorioso")
    print("6. Exit")

def main_function():
    while True:
        menu_members()

        choice = int(input("Enter your Choice: "))

        if choice == 1:
            print("Ivan")
            delumen_main()
        elif choice == 2:
            print("Gerald")
            mamasalanang_main()
        elif choice == 3:
            print("Michael")
            mosquito_main()
        elif choice == 4:
            print("Simone")
            reyes_main()
        elif choice == 5:
            print("\n")
            victorioso_main()
        elif choice == 6:
            print("Exiting")
            break
        else:
            print("Invalid Choice")

main_function()