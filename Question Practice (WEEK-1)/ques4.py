first_name = "Ravi"
last_name = "Kumar"
course = "Python"
symbol = "*"
count = 5

full_name = str(first_name + " " + last_name) # str: join first_name and last_name with one space
name_tag = str(course + ":" + full_name) # str: join course, ": ", and full_name
line = str(symbol * count) # str: repeat symbol count times
short_code = str(first_name[0:2:1] + last_name[-2::]) # str: join first 2 letters of first_name and last 2 letters of last_name
has_py = bool("Py" in course) # bool: check whether course contains "Py"
same_names = bool(len(first_name) == len(last_name)) # bool: check whether first_name and last_name are equal
comes_before = bool(first_name[0] < last_name[0]) # bool: check whether first_name comes before last_name alphabetically

print(full_name)
print(name_tag)
print(line)
print(short_code)
print(has_py)
print(same_names)
print(comes_before)
