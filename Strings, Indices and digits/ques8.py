def encode_shifting_ends(s):
    new = s[-1] + s[1:-1] + s[0]
    if len(s) == 1:
        return s
    else:
        return new

s = input()
print(encode_shifting_ends(s))