def count_vowels(text):
  vowels = 0
  known_vowels = "AEIOUaeiou"
  for ch in text:
    if ch in known_vowels:
      vowels += 1
  return vowels

text = input()
print(count_vowels(text))