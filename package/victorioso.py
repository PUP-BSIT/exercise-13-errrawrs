def display_menu():
   print("Hello , My Name is Daniel B. Victorioso")
   print("1) Basic Information")
   print("2) Goals")
   print("3) Comment From Mamasalanang")
   print("4) Comment From  Mosquito")
   print("5) Comment From  Delumen")
   print("6) Comment From  Reyes")
   print("7) Back to Main Menu")
   print("8) Exit")

def basic_info():
   print("Name: Daniel B. Victorioso")
   print("Age: 24")
   print("Birthday: November 05, 2000")

def goals():
   print("To be successful in life. Be a skilled cyber security professional")

def gerald_comment():
   print("Goodluck future programmer, may your path will guide you to your future")

def michael_comment():
   print("Type today, change the world tomorrow.")

def ivan_comment():
   print("Your code defines the future; make it count.")

def simone_comment():
   print("Every day is a programming day!")

def menu_function():
   display_menu()

   user_choice = input("Enter your user_choice: ")

   while True:
      if user_choice == "1":
         basic_info()
      elif user_choice == "2":
         goals()
      elif user_choice == "3":
         gerald_comment()
      elif user_choice == "4":
         michael_comment()
      elif user_choice == "5": 
         ivan_comment()
      elif user_choice == "6":
         simone_comment()
      elif user_choice == "7":
         break
      elif user_choice == "8":
         print("Exiting...")
         exit()
      else:
         print("Invalid user_choice!!!")