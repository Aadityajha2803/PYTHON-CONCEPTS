def count_digits(text):
    total = 0
    for i in text:
        if i.isdigit():
            total += 1
        else:
            continue
    return total
text = input()
print(count_digits(text))