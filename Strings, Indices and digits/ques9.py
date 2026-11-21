def is_strict_prefix_ci(prefix, s):
    prefix_word = str(prefix[0::])
    word = s
    if prefix_word in word and prefix_word < word:
        return True
    else:
        return False

prefix = input()
s = input()
print(is_strict_prefix_ci(prefix, s))