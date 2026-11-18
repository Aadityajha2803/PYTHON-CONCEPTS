a = 5
b = 6
price, discount_percent = 80, 5.75
total_mins = 470

output1 = int(a + b) # int: sum of a and b
output2 = int(output1 * 2) # int: twice the sum of a and b
output3 = int(abs(a - b)) # int: absolute difference between a and b
output4 = int(abs((a*b) - output1)) # int: absolute difference between sum and product of a and b

# Find discounted price given price and discount_percent
price = int(1200)
discount_percent = float(25)
# input variables : price: int, discount_percent: float
discounted_price = float(price - (price * discount_percent/100)) # float

# Round the discounted_price
rounded_discounted_price = int(discounted_price) # int

print(output1)
print(output2)
print(output3)
print(output4)
print(discounted_price)
print(rounded_discounted_price)

# Find hrs and mins given the total_mins
# input variables : total_mins
total_mins = 270
hrs = int(total_mins // 60) # int: hint: think about floor division operator
mins = int(total_mins % 60)  # int
print(str(hrs) + " Hours and " + str(mins) + " Minutes")


