# Create a program that ask user to input a number, continue asking until the user input is invalid.
# Display "Unique" after input when the inputted number don't have duplicate.
# Display "Duplicate" after input when the inputted number have duplicate.
def main():
    numbers = []
    while True:
        try:
            user_input = input("Enter a number: ")
            num = int(user_input)

            if num in numbers:
                print("Duplicate/s")
            else:
                print("Unique")
                numbers.append(num)

        except ValueError:
            print("Invalid input. Program ended.")
            break

if __name__ == "__main__":
    print("Number Duplicate Checker")
    main()
