def display_menu():
   print("Hello , My Name is Daniel B. Victorioso")
   print("1) Basic Information")
   print("2) Goals")
   print("3) Comment From Reyes")
   print("4) Comment From  Mosquito")
   print("5) Comment From  Delumen")
   print("6) Comment From  Victorioso")
   print("7: Exit")

def gerald_basic_info():
   print("Name: Daniel B. Victorioso")
   print("Age: 24")
   print("Birthday: November 05, 2000")

def goals():
   print("To be successful in life. Be a skilled cyber security professional")

def simone_comment():
   print("")

def michael_comment():
   print("")

def ivan_comment():
   print("")

def daniel_comment():
   print("")

def menu_function():
   while True:
      display_menu()

      user_choice = input("Enter your user_choice: ")

      if user_choice:
         gerald_basic_info()
      elif user_choice == "2":
         goals()
      elif user_choice == "3":
         simone_comment()
      elif user_choice == "4":
         michael_comment()
      elif user_choice == "5": 
         ivan_comment()
      elif user_choice == "6":
         daniel_comment()
      elif user_choice == "7":
         print("Exiting...")
         break
      else:
         print("Invalid user_choice!!!")


menu_function()