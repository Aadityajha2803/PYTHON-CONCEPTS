def get_circular_element(items: list, index: int):
    r = len(items)
    output1 = int(index % r)
    output = items[output1]
    return output
    pass
items = eval(input())
index = int(input())
print(get_circular_element(items, index))