a = 5

price1, discount1 = 50, 4 # for offer1
price2, discount2 = 60, 8 # for offer2

output1 = bool(a >= 5) # bool: True if a is greater than or equal to 5

output2 = bool(a % 5 == 0) # bool: True if a is divisible by 5

output3 = bool(a % 2 != 0 and a < 10) # bool: True if a is odd number less than 10

output4 = bool(a % 2 != 0 and -10 <= a <= 10) # bool: True if a is an odd number within the range -10 and 10

output5 = bool(len(str(a)) % 2 == 0 and len(str(a)) < 10) # bool: True if a has even number of digits but not more than 10 digits

price1_after_discount = float(price1 - (price1 * discount1/100))
price2_after_discount = float(price2 - (price2 * discount2/100))
is_offer1_cheaper = bool(int(price1_after_discount) < int(price2_after_discount))# bool: True if the offer1 is strictly cheaper

print(output1)
print(output2)
print(output3)
print(output4)
print(output5)

print(price1_after_discount)
print(price2_after_discount)
print(is_offer1_cheaper)
