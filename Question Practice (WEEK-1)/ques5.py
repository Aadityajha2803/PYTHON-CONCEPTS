# Read the input values first.
# Then calculate item_cost and final_amount.
# Create message using this format: item value, quantity value, final_amount value
# Finally, print item, item_cost, final_amount, and message on separate lines.

item = str(input()) # str: read item name using input()
quantity = int(input()) # int: read quantity using input() and convert to int
price = float(input()) # float: read price using input() and convert to float
packing = float(input()) # float: read packing charge using input() and convert to float

item_cost = float(quantity * price) # float: multiply quantity and price
final_amount = float(item_cost + packing) # float: add item_cost and packing
message = str(item + ", " + str(quantity) + ", " + str(final_amount)) # str: join values with comma and space

print(item_cost)
print(final_amount)
print(message)
