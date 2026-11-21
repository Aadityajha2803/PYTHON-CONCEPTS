def deinterleave_indices(s):
    even_chars = s[0::2]
    odd_chars = s[1::2]
    return (even_chars, odd_chars)

s = input()
print(deinterleave_indices(s))