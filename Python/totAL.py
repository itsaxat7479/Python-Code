# Initialize variables for sum, maximum, and minimum
total = 0
maximum = float('-inf')  # Negative infinity
minimum = float('inf')  # Positive infinity

# Loop to take twenty floating-point inputs
for i in range(20):
    try:
        # Take input from the user and convert it to a floating-point number
        num = float(input("Enter a floating-point number: "))
        
        # Update total sum
        total += num
        
        # Update maximum and minimum
        if num > maximum:
            maximum = num
        if num < minimum:
            minimum = num
            
    except ValueError:
        # Handle invalid input (non-floating-point value)
        print("Invalid input. Please enter a floating-point number.")

# Calculate average
average = total / 20

# Print the results
print("Sum:", total)
print("Average:", average)
print("Maximum:", maximum)
print("Minimum:", minimum)
