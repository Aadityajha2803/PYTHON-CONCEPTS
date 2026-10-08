str = input("Enter your favourite food:")
mid = len(str)//2
output1 = str[mid-1:mid+2]
output2 = str[-2:]
print("Middle three characters are:", output1)
print("Last two characters are:", output2)
