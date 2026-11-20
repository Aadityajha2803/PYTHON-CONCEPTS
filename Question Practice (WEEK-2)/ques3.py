#PART-1
odd_num_check = int(input())
if odd_num_check % 2 != 0:
    print("Odd")
else:
    print("Even")

#PART-2
num = int(input())
if num < 0:
    print("not a perfect square")
elif num == 0:
    print("perfect square")
else:
    root = int(num**0.5)
    if root*root == num:
        print("perfect square")
    else:
        print("not a perfect square")

#PART-3
word = input()
if "a" in word or "e" in word or "i" in word or "o" in word or "u" in word or "A" in word or "E" in word or "I" in word or "O" in word or "U" in word:
    print("yes")
else:
    print("no")

#PART-4
num = int(input())
if num % 2 == 0 and num % 3 == 0:
    print("Divisible by 2 and 3")
elif num % 2 == 0:
    print("Divisible by 2")
elif num % 3 == 0:
    print("Divisible by 3")
else:
    print("Not divisible by 2 and 3")

#PART-5
word = input()
palindrominator = word + word[::-1]
print(palindrominator)

#PART-6
p = int(input())
r = int(input())
t = int(input())
simple_interest = float((p*r*t)/100)
print(simple_interest)