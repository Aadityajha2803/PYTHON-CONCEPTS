def tens_greater_than_ones(n):
    ones_digit = abs(n) % 100
    oness_digit = abs(ones_digit) % 10
    tens_digit = (ones_digit - oness_digit) // 10
    if tens_digit > oness_digit:
        return True
    else:
        return False

n = int(input())
print(tens_greater_than_ones(n))