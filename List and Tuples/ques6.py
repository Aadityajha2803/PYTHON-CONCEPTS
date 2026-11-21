def separate_outer_characters(s):
    if len(s) == 0:
        return ("","")
    elif len(s) == 1:
        return(s,"")
    else:
        outer = s[0] + s[-1]
        inner = s[1:-1]
        return (outer,inner)
s = input().strip()
print(separate_outer_characters(s))