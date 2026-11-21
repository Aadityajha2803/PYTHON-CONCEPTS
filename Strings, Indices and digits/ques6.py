def bold_nth_char(s, n):
    idx = n -1
    char = s[:idx] + "**" + s[idx] + "**" + s[idx+1:]
    return char

s = input()
n = int(input())
print(bold_nth_char(s, n))