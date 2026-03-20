# Create a program that ask user to input a number, continue asking until the user input is invalid. Display the lowest number
def main():
    numbers = []

    while True:
        try:
            user_input = input("Enter a number: ")
            num = float(user_input)

            numbers.append(num)
            print(f"Added: {num}")

        except ValueError:
            if numbers:
                lowest = min(numbers)
                print(f"\nLowest number: {lowest}")
            else:
                print("\nNo valid numbers entered.")
            print("Program ended.")
            break

if __name__ == "__main__":
    print("Lowest Number")
    main()