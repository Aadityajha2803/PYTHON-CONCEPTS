def repeat_second_half(tup):
    m = len(tup) // 2
    new_tup = (tup + tup[m::] + tup[m::])
    return new_tup


tup = eval(input())
print(repeat_second_half(tup))