def print_colored(text, color_code):
    print(f"\033[{color_code}m{text}\033[0m")

def main():
    while True:
        print("="*40)
        print_colored("1. Normal Prime Checker", "33;1")
        print_colored("2. Multi Line Prime Checker", "33;1")
        print_colored("3. Exit", "33;1")
        print("="*40)

        option = input("\n••• Choose an Option: ").strip()

        if option == "1":
            print_colored("\nWelcome to Normal Mode Prime Checker", "32")
            print_colored("-"*40, "32")
            try:
                number = int(input("\nEnter a number: "))
                if number < 2:
                    print_colored(f"{number} is not a prime number.", "31")
                else:
                    for i in range(2, int(number ** 0.5) + 1):
                        if number % i == 0:
                            print_colored(f"{number} is not a prime number.", "31")
                            break
                    else:
                        print_colored(f"{number} is a prime number.", "32")
            except ValueError:
                print_colored("Invalid input. Please enter a valid integer.", "31")

        elif option == "2":
            print_colored("\nWelcome to Multi Line Prime Checker", "32")
            print_colored("-"*40, "32")
            try:
                start = int(input("\nEnter the start of the range: "))
                end = int(input("Enter the end of the range: "))
                primes = [num for num in range(start, end + 1) if num > 1 and all(num % x != 0 for x in range(2, int(num ** 0.5) + 1))]
                if primes:
                    print_colored("Prime numbers in the range:", "32")
                    print(primes)
                else:
                    print_colored("No prime numbers found in the range.", "31")
            except ValueError:
                print_colored("Invalid input. Please enter valid integers.", "31")

        elif option == "3":
            print_colored("\nExiting the program. Goodbye!", "34;1")
            break

        else:
            print_colored("\nChoose a valid option!", "31;1")

        print("\n" + "="*40)

if __name__ == "__main__":
    main()