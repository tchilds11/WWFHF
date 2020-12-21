def get_menu_choice():
    def print_menu():       # Your menu design here
        print(30 * "-", "CHARACTER SELECTION", 29 * "-")
        print("1. GOLDBERG ")
        print("2. THE UNDERTAKER ")
        print("3. KURT ANGLE ")
        print("4. BIG SHOW ")        
        print("5. TAP OUT (EXIT) ")
        print(11 * "WWFHF  ")

    loop = True
    int_choice = -1

    while loop:          # While loop which will keep going until loop = False
        print_menu()    # Displays menu
        choice = input("Enter your choice [1-5]: ")

        if choice == '1':
            int_choice = 1
            print("You Have Selected GOLDBERG")
            loop = False
        elif choice == '2':
            int_choice = 2
            print("You Have Selected THE UNDERTAKER")
            loop = False
        elif choice == '3':
            int_choice = 3
            print("You Have Selected KURT ANGLE")
            loop = False
        elif choice == '4':
            int_choice = 4
            print("You Have Selected THE BIG SHOW")
            loop = False
        elif choice == '5':
            int_choice = -1
            print("Exiting..")
            loop = False  # This will make the while loop to end
        else:
            # Any inputs other than values 1-4 we print an error message
            input("Wrong menu selection. Enter any key to try again..")
    return  


print(get_menu_choice())
#