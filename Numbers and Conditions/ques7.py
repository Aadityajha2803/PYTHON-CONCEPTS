def shuffle_three_words(sentence):
    m = sentence.split(" ")
    return m[-1] + " " + m[0] + " " + m[1]

sentence = input()
print(shuffle_three_words(sentence))