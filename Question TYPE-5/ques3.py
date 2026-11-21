def vowel_counts_per_word(sentence):
    words = sentence.split()
    vowels_known = "AEIOUaeiou"
    result = []
    for word in words:
        count = 0
        for ch in word:
            if ch in vowels_known:
                count += 1
        result.append(count)
    return result

sentence = input()
print(vowel_counts_per_word(sentence))