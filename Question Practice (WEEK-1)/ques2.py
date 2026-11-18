n = 24
is_positive = bool(n > 0) # bool: check whether n is greater than 0
is_two_digit = bool(99 >= n >= 10) # bool: check whether n is from 10 to 99, including both 10 and 99
is_even = bool(n % 2 == 0) # bool: check whether n gives remainder 0 when divided by 2
is_multiple_of_3 = bool(n % 3 == 0) # bool: check whether n gives remainder 0 when divided by 3
is_good_number = bool(is_positive and is_two_digit and is_even and is_multiple_of_3) # bool: check whether n is positive, two-digit, and divisible by 6
is_not_small = bool(n>=10) # bool: check whether n is not less than 10

print(is_positive)
print(is_two_digit)
print(is_even)
print(is_multiple_of_3)
print(is_good_number)
print(is_not_small)
