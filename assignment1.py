# Ques 1. Write a Python script that accepts a number from the command line 
# and checks whether it is prime. Explain how command-line arguments 
# are accessed.
import sys

num = int(sys.argv[1])

if num <= 1:
    print(num, "is not a prime number")
else:
    for i in range(2, num):
        if num % i == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")

# Explanation
# * Command-line arguments are accessed using the sys.argv list.
# * sys.argv[0] contains the program name.
# * sys.argv[1] contains the first argument passed from the command line.
# * The number is checked by testing divisibility from 2 to num-1.


# Ques 2. Write a program using different data types to demonstrate the 
# difference between ‘is’ and ‘==’. Explain the output.

a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)
print(a is b)
print(a is c)

# Explanation

# * == checks value equality.
# * is checks memory location (identity).
# * a == b → True because values are same.
# * a is b → False because both are stored in different memory locations.
# * a is c → True because both refer to the same object.

# Ques 3. Write a program that iterates through a list, skips negative numbers, 
# stops execution at zero, and handles non-integer values using exception 
# handling. 

data = [10, -5, 8, "hello", 3, 0, 7]

for item in data:
    try:
        if not isinstance(item, int):
            raise ValueError

        if item < 0:
            continue
        if item == 0:
            break

        print(item)

    except ValueError:
        print("Non-integer value encountered")


# Ques 4. Using a single list comprehension, generate a list of squares of numbers 
# from 1 to 20 that are divisible by both 2 and 5. 

squares = [x**2 for x in range(1, 21) if x % 2 == 0 and x % 5 == 0]
print(squares)

# Ques 5. Write a user-defined function that returns the largest and smallest 
# values from a list without using built-in functions. 

def find_min_max(lst):
    smallest = lst[0]
    largest = lst[0]

    for num in lst:
        if num < smallest:
            smallest = num
        if num > largest:
            largest = num

    return smallest, largest

numbers = [5, 2, 9, 1, 7]
result = find_min_max(numbers)
print("Smallest:", result[0])
print("Largest:", result[1])
