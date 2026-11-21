def double_if_even_else_square(lst):
    new_lst = []
    for i in lst:
        if i % 2 == 0:
            new_lst.append(i * 2)
        else:
            new_lst.append(i ** 2)
    return new_lst
lst = eval(input())
print(double_if_even_else_square(lst))