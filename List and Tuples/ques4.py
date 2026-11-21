def make_dict_from_index(keys, values, idx):
    if idx >= 0 and idx < len(keys) and idx < len(values):
        m = {
            keys[idx] : values[idx],
        }
        return m
    else:
        return {}
keys = eval(input())
values = eval(input())
idx = int(input())
print(make_dict_from_index(keys, values, idx))