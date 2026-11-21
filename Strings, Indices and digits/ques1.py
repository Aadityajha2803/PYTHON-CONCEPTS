def is_odd_length_palindrome(s):
    if len(s) % 2 != 0 and s[::-1] == s:
        return True
    else:
        return False

s = input()
print(is_odd_length_palindrome(s))