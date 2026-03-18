# Create a program that ask user to input 10 numbers. Display all numbers that don't have duplicate.
nums = list(map(int, input("Enter 10 numbers: ").split()))
print("Unique numbers:", *set(nums))