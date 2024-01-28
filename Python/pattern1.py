# Define the number of rows for the diamond
num_rows = 5

# Loop to generate and print the diamond pattern
for i in range(1, num_rows + 1):
    # Calculate the number of asterisks and underscores for each row
    num_asterisks = num_rows - i + 1
    num_underscores = 2 * i - 2

    # Print the left side of the diamond
    print('*' * num_asterisks, end='')

    # Print the underscores in the middle
    print('_' * num_underscores, end='')

    # Print the right side of the diamond
    print('*' * num_asterisks)
    print('*' * num_asterisks, end='')
    print('_' * num_underscores, end='')
    print('*' * num_asterisks)
