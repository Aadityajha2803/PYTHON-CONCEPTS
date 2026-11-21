def first_last_sorted(s):
    first_char = s[0]
    last_char = s[-1]
    if first_char < last_char:
        return (first_char, last_char)
    else:
        return (last_char, first_char)

s = input()
print(first_last_sorted(s))