def compare_last_digits(a, b):
    last_digit_a = abs(a) % 10
    last_digit_b = abs(b) % 10
    if last_digit_a > last_digit_b:
        return 1
    if last_digit_a < last_digit_b:
        return -1
    if last_digit_a == last_digit_b:
        return 0

a = int(input())
b = int(input())
print(compare_last_digits(a, b))