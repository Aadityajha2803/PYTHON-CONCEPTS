def count_vowels_consonants(text: str) -> tuple:
    vowels = 0
    consonants = 0
    extra = 0
    if text[0] in "AEIOU":
        vowels += 1
    elif text[0] in "BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxz":
        consonants += 1
    else:
        extra += 1
    return vowels, consonants
        
if __name__ == "__main__":
    text = input()
    vowels, consonants = count_vowels_consonants(text)
    print(vowels, consonants)
