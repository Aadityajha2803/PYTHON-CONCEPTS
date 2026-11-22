def process_numbers(numbers):
    result = []

    for num in numbers:
        digit_sum = sum(int(digit) for digit in str(num))

        if digit_sum % 2 == 0:
            result.append(num // 2)
        else:
            result.append(digit_sum ** 2)

    return result


numbers = list(map(int, input().split()))

result = process_numbers(numbers)

for num, value in zip(numbers, result):
    print(f"{num}({value})", end=" ")