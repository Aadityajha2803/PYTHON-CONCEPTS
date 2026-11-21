def unique_symmetric_letters(s1, s2):
    return len(set(s1) ^ set(s2))
s1 = input()
s2 = input()
print(unique_symmetric_letters(s1, s2))