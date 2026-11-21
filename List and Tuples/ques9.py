def shuffle_digits(n):
  s = str(n)
  left = 0
  right = len(s) - 1
  res = ""

  while left <= right:
    res += s[left]
    if left != right:
      res += s[right]
    left += 1
    right -= 1

  return int(res)


n = int(input())
print(shuffle_digits(n))