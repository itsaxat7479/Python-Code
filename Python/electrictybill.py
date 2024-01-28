# Accept the number of units from the user
units = float(input("Enter the number of units consumed: "))

# Minimum service charge
minimum_charge = 250.0

# Initialize the total bill
total_bill = 0.0

# Calculate the bill based on the given criteria
if units <= 100:
    # First 100 units are free
    total_bill = minimum_charge
elif units <= 200:
    # Next 100 units charged at Rs. 5 per unit
    total_bill = minimum_charge + (units - 100) * 5.0
else:
    # Units above 200 charged at Rs. 10 per unit
    total_bill = minimum_charge + 100 * 5.0 + (units - 200) * 10.0

# Print the total bill
print(f"Electricity Bill: Rs. {total_bill:.2f}")
