otp = input()
hidden = "".join("#" if ch.isdigit() else ch for ch in otp)
print(hidden)
