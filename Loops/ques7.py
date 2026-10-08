n = int(input("Enter your number:"))
table = 0
while table <= 10:
    print(n, "X", table, "=", n*table)
    table = table+1
print("This was the multiplication table of:", n)
