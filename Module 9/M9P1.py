#Iana Vasileva  CIS160 B65   M9P1    10/24/26
# Function to compute extended price
def compute_extended_price(quantity, unit_price):
    extended_price = quantity * unit_price

    # Apply 10% discount if total is over $10,000
    if extended_price > 10000:
        extended_price = extended_price * 0.90

    return extended_price

# Define total extended price
total_extended_price = 0

# Get quantity from user
quantity = int(input("Enter quantity (0 to stop): "))

# Loop until signal
while quantity != 0:
    unit_price = float(input("Enter unit price: "))
    extended_price = compute_extended_price(quantity, unit_price)

# Display results
    print(f"Quantity: {quantity}")
    print(f"Price: ${unit_price:,.2f}")
    print(f"Extended price: ${extended_price:,.2f}")
    print()

# Add to total
    total_extended_price = total_extended_price + extended_price

# Get next quantity
    quantity= int(input("Enter quantity (0 to stop): "))

# Display total
print(f"Total extended price: ${total_extended_price:,.2f}")
