def rotate_even_indices(lst):
    res = lst[:]
    evens = res[0::2]
    if len(evens) < 2:
        return res
    res[0::2] = evens[1:] + evens[:1]
    return res


lst = eval(input())
print(rotate_even_indices(lst))