def countVowConso(user_input):
    vowels = "aeiouAEIOU"
    countvowels = 0
    countconsonants = 0
    for eachchar in user_input:
        if (eachchar in vowels):
            countvowels += 1
        elif (eachchar.isalpha()):
            countconsonants += 1
    return countvowels, countconsonants
vowels, consonants = countVowConso("Hello Aaditya Jha")
print("The number of vowels are:", vowels)
print("The number of consonants are:", consonants)


