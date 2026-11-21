def is_decreasing_4digit(n):
  if 1000 <= n <= 9999:
    if int(str(n)[0]) > int(str(n)[1]) > int(str(n)[2]) > int(str(n)[3]):
      return True
    else:
      return False
  else:
    return False  


n = int(input())
print(is_decreasing_4digit(n))