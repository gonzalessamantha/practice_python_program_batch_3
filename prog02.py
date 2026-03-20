# Create a program that ask user to input 10 numbers. Display all numbers. For numbers with duplicate, display only the first entry.
nums = list(map(int, input("Enter 10 numbers: ").split()))
seen = []
print("All numbers:", *nums)
print("First occurrences only:", *[x for x in nums if x not in seen or seen.append(x) or True])