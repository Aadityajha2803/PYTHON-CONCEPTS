def word_sandwich(words):
  first = words[0]
  last = words[-1]
  res = []
  for w in words[1:-1]:
    res.extend([first, w, last])
    return res
  
words = eval(input())
print(word_sandwich(words))