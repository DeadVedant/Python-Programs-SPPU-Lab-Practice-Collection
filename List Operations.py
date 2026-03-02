#Assignmnet 2: List Operations

# Python Program to find Maximum, Minimum, Average and Sum of a List

# Asking user how many numbers they want to enter
n = int(input("Enter how many numbers you want in the list: "))

# Creating an empty list
numbers = []

# Using a loop to take 'n' numbers as input

for i in range(n):
    num = float(input(f"Enter number {i+1}: "))
    numbers.append(num)

# Calculate required values

maximum = max(numbers)
minimum = min(numbers)
total = sum(numbers)
average = total / n

# Display the results

import time

print("\nCalculating results...")
time.sleep(2)  # Simulating some processing time
start=time.time()

print("\nResults:")
print("Numbers entered: ", numbers)
print("Maximum number: ", maximum)
print("Minimum number: ", minimum)
print("Sum of numbers: ", total)
print("Average of numbers: ", round(average, 2))
print("Time taken to compute results: ", round(time.time()-start,5), "seconds") 
print("\nThank you for using the program!")