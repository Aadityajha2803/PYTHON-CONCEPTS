import time
count = int(input("Enter your countdown number:"))
print("\n Countdown starts now:")
for i in range(count,0,-1):
    print(i)
    time.sleep(1)
print("\n WOHOO!")

