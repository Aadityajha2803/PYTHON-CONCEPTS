#TESTCASE-1
armstrong_check = int(input())
s = str(armstrong_check)
n = len(s)
if int(s[0]) ** n + int(s[1]) ** n + int(s[2]) ** n == armstrong_check:
    print("True")
else:
    print("False")

#TESTCASE-2
import math
factorial_calculator = int(input())
if factorial_calculator < 0:
    print("Invalid input")
elif factorial_calculator == 0:
    print("1")
else:
    print(math.factorial(factorial_calculator))

#TESTCASE-3
fizzbuzz_single = int(input())
if fizzbuzz_single % 3 == 0 and fizzbuzz_single % 5 == 0:
    print("fizzbuzz")
elif fizzbuzz_single % 3 == 0:
    print("fizz")
elif fizzbuzz_single % 5 == 0:
    print("buzz")
else:
    print(fizzbuzz_single)

#vowel count
word = input()
vowel = 0
consonants = 0
for ch in word:
    if ch in "AEIOUaeiou":
        vowel += 1
    elif ch in "BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz":
        consonants += 1
print(vowel,consonants)

#Number of digits
number = int(input())
s = str(number)
print(len(s))

#Compound Interest
P = int(input())
R = int(input())
T = int(input())
Amount = P * (1 + R/100) ** T
compound_interest = int(Amount - P)
print(compound_interest)
