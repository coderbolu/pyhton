numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Create a variable to store the highest number, and temporarily store 0 in it.
max_number = 0

# Loop through each number in the list and check whether it's greater than our current highest number (initially 0).
for number in numbers:
    if number > max_number:
        # If the number in the list is higher than the current highest number, then update the highest number with the current number.
        max_number = number

print("The largest number is:", max_number)

