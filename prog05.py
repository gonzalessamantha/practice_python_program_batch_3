# Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number from lowest to highest.
# Clue: sort() function
def main():
    numbers = []

    while True:
        try:
            user_input = input("Enter a number: ")
            num = int(user_input)

            numbers.append(num)
            print(f"Added: {num} (Total: {len(numbers)} numbers)")

        except ValueError:
            if numbers:
                numbers.sort()
                print("\nNumbers from lowest to highest:")
                for i, num in enumerate(numbers, 1):
                    print(f"{i}. {num}")
            else:
                print("\nNo valid numbers entered.")
            print("Program ended.")
            break

if __name__ == "__main__":
    print("Number Sorter (Lowest to Highest)")
    main()