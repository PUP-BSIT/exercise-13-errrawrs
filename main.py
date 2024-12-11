from package.delumen import menu_function as delumen_main
from package.victorioso import menu_function as victorioso_main

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
        elif choice == 3:
            print("Michael")
        elif choice == 4:
            print("Simone")
        elif choice == 5:
            print("\n")
            victorioso_main()
        elif choice == 6:
            print("Exiting")
            break
        else:
            print("Invalid Choice")

main_function()