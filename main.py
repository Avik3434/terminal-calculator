# Calulator by Avik Mukherjee 
import time
import sys as s

# Define ANSI color codes
red = "\033[31m"
green = "\033[32m"
yellow = "\033[33m"
cyan = "\033[36m"
reset = "\033[0m"

while True:
    name = input(f"{cyan}Enter your name: {reset}")

    print(f"{yellow}<----Welcome to my calculator---->{reset}")
    time.sleep(0.6)

    dots = ["", ".", "..", "..."]
    start_time = time.time()

    while True:
        for dot in dots:
            print(f"\r{green}Starting app{dot}   {reset}", end="")
            time.sleep(0.3)
            if time.time() - start_time >= 2:
                break
        if time.time() - start_time >= 2:
            break

    print(f"{red}\nWelcome {name}{reset}")

    def summation():
        total = 0        
        while True:
            number = input("Enter your numbers (type 'Done' to finish): ")
            if number.lower() == 'done':
                break
            else:
                try:
                    num = float(number)
                    total += num
                except ValueError:
                    print("Enter a valid number: ")
        
        print(f"The sum is {total}")
        user_choice = input("Enter 'modes' to open Calculator or 'exit' to Quit: ")
        if user_choice.lower() == 'modes':
            choice()
        
        if user_choice.lower() == 'exit':
            exit_app()

    def substraction():
        result = None
        while True:
            number = input("Enter a number (or 'done' to finish): ")

            if number.lower() == 'done':
                break

            try:
                num = float(number)
                if result is None:
                    result = num
                else:
                    result -= num
            except ValueError:
                print("Enter a valid number!")

        print("Final result:", result)
        user_choice = input("Enter 'modes' to open Calculator or 'exit' to Quit: ")
        if user_choice.lower() == 'modes':
            choice()
        elif user_choice.lower() == 'exit':
            exit_app()

    def multiplication():
        result = 1
        while True:
            numbers = input("Enter your number (type 'done' to finish): ")

            if numbers.lower() == 'done':
                break
            else:
                try:
                    num = int(numbers)
                    result *= num
                except ValueError:
                    print("Enter valid number")
        print("Final result:", result)
        user_choice = input("Enter 'modes' to open Calculator or 'exit' to Quit: ")
        if user_choice.lower() == 'modes':
            choice()
        elif user_choice.lower() == 'exit':
            exit_app()
    def division():
        result = None
        while True:
            numbers = input("Enter your number (type 'done' to finish): ")

            if numbers == 'done':
                break
            else:
                try:
                    num = float(numbers)
                    if result is None:
                        result = num
                    else:
                        if num == 0:
                            print("Cannot divide by zero.")
                            continue
                        result /= num

                except ValueError:
                    print("Invalid numbers enter again")
        print("Final result:", result)
        user_choice = input("Enter 'modes' to open Calculator or 'exit' to Quit: ")
        if user_choice.lower() == 'modes':
            choice()
        elif user_choice.lower() == 'exit':
            exit_app()
    def exit_app():
        print(f"\t\tGood bye {name}\n--Thank your for using this calculator--")
        s.exit()

    def choice():
        print("\n\n\n===Modes===")
        print("'1' for summation\n'2' for substraction\n'3' for multiplication\n'4' for division\n'5' for Exit")
        modes = input("\nEnter your mode (1-5) ")
        if modes == '1':
            summation()
        elif modes == '2':
            substraction()
        elif modes == '3':
            multiplication()
        elif modes == '4':
            division()
        elif modes.lower() == '5':
            exit_app()
        else:
            print("Enter number between (1-5)")
            choice()
            
    e = input(f"{cyan}Type 'exit' to quit or 'open' to open calculator: {reset}").lower()
    if e == 'exit':
        break
    if e.lower() == 'open':  
        choice()
    elif e.lower() == 'exit':
        exit_app()

print("--Thank your for using this calculator--")

