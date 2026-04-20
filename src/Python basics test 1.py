"""
LAB EXERCISE: The "Clean Sweep" Sales Tool
-------------------------------------------
USER STORY:
As a Junior Data Analyst, I need a function that takes a raw transaction string 
(e.g., 'apple:2.50:3') and converts it into a clean, human-readable summary. 
The system must validate the data to prevent reporting crashes.

INPUT: 
    - raw_string (str): A string in the format "ItemName:Price:Quantity"

OUTPUT:
    - dict: {'item': str, 'total': float} if successful.
    - str: An error message if validation fails.

VALIDATION RULES:
    1. Data Types: Price and Quantity must be numeric values.
    2. Price: Must be 0.0 or higher (no negative prices).
    3. Quantity: Must be 1 or higher.

LOGIC:
    - Split input by ':'
    - Convert Price/Quantity to numbers.
    - Calculate Total (Price * Quantity).
    - Apply 10% discount if Total > 100.
    
ERROR MESSAGES:
    - 'Invalid numeric data'
    - 'Price cannot be negative'
    - 'Quantity must be at least 1'
-------------------------------------------
"""

def process_sale(raw_string):
    raw_string = raw_string.split(':')
    data_set = {'item': raw_string[0], 'price': raw_string[1], 'quantity': raw_string[2]}

    try:
        price = float(data_set['price'])
        quantity = int(data_set['quantity'])
    except:
        return 'Invalid numeric data'
    
    if price < 0:
        return 'Price cannot be negative'
    
    if quantity < 1:
        return 'Quantity must be at least 1'
    
    total = price * quantity
    if total > 100:
        total *= 0.9
    return {'item': data_set['item'], 'total': float(total)}

# Test 1: Standard Sale
print(process_sale("Apple:2.0:5")) 
# Expected: {'item': 'Apple', 'total': 10.0}

# Test 2: Bulk Discount (10% off 200)
print(process_sale("Laptop:200:1")) 
# Expected: {'item': 'Laptop', 'total': 180.0}

# Test 3: Bad Data
print(process_sale("Banana:FREE:5")) 
# Expected: 'Invalid numeric data'
