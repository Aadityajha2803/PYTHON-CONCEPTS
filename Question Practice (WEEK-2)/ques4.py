main_dish = input()
time_of_day = int(input())
has_voucher = input()
is_card_payment = input()
total_cost = 0
if main_dish == "paneer tikka":
    total_cost += 250
    
    if time_of_day >= 12 and time_of_day <= 15:
        total_cost = total_cost - (total_cost * 15/100)
    else:
        total_cost = total_cost

elif main_dish == "butter chicken":
    total_cost += 240
    
    if time_of_day >= 12 and time_of_day <= 15:
        total_cost = total_cost - (total_cost * 15/100)
    else:
        total_cost = total_cost

elif main_dish == "masala dosa":
    total_cost += 200
    
    if time_of_day >= 12 and time_of_day <= 15:
        total_cost = total_cost - (total_cost * 15/100)
    else:
        total_cost = total_cost

else:
    print("Invalid Dish")

if has_voucher == "True":
    total_cost = total_cost - (total_cost * 10/100)
else:
    total_cost = total_cost

if is_card_payment == "True":
    total_cost = total_cost + (total_cost * 5/100)
else:
    total_cost = total_cost

print(f"{total_cost:.02f}")








