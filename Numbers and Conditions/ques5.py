def reverse_first_half(s):
    mid = len(s)//2
    first_reversed = s[:mid][::-1]
    second_reverse = s[mid:]
    return first_reversed + second_reverse

s = input()
print(reverse_first_half(s))