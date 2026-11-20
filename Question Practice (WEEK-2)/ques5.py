room_type = input()
is_weekend = input()
is_loyalty_member = input()
is_online_payment = input()

cost = 0
if room_type == "standard":
    cost += 2000
elif room_type == "deluxe":
    cost += 3500
elif room_type == "suite":
    cost += 5000
else:
    print("Invalid room type")

if is_weekend == "True":
    cost = cost + (cost * 20/100)
else:
    cost = cost

if is_loyalty_member == "True":
    cost = cost - (cost * 10/100)
else:
    cost = cost

if is_online_payment == "True":
    cost = cost + (cost * 5/100)
else:
    cost = cost

print(f"{cost:.02f}")
