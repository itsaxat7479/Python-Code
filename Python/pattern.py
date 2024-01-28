# Define the number of rows for the pyramid
num_rows = 5

# Loop to generate and print the pyramid
for i in range(1, num_rows + 1):
    # Calculate and print the numbers for the current row
    for j in range(1, i + 1):
        print(i * j, end=" ")
    print()  # Move to the next line for the next row
