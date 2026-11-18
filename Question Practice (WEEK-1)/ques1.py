students = 47
teachers = 3
bus_capacity = 20
ticket_price = 75
snacks_price = 12.5

total_people = students + teachers
full_busses = int(total_people // bus_capacity)
people_left = int(total_people % bus_capacity)
ticket_amount = int(total_people * ticket_price)
snack_amount = float(snacks_price * total_people)
total_amount = float(ticket_amount + snack_amount)
rounded_total = int(total_amount)

print(total_people)
print(full_busses)
print(people_left)
print(ticket_amount)
print(snack_amount)
print(total_amount)
print(rounded_total)

