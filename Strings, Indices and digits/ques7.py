def sum_ends_divisible_by_k(s, k):
    sum = int(s[0]) + int(s[-1])
    if sum % k == 0:
        return True
    else:
        return False

s = input()
k = int(input())
print(sum_ends_divisible_by_k(s, k))