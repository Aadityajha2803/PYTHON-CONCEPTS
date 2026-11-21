def middle_element(items):
    middle = len(items) // 2
    middle_item = items[middle]
    return middle_item

items = eval(input())
print(middle_element(items))