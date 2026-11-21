def divisible_by_last_two(n):
    m = abs(n) % 100
    if m == 0:
        return False
    return n % m == 0

n = int(input())
print(divisible_by_last_two(n))