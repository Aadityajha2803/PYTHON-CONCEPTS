code = "BK24M157"

product_type = code[0:2:1] # str: get the first 2 characters of code
year_text = code[2:4:1] # str: get the year part from code as text
batch = code[4:5:1] # str: get the batch character from code
product_number = int(code[-3::]) # int: get the last 3 characters and convert them to int
first_half = code[0:4:1] # str: get the first 4 characters of code
last_half = code[-4::] # str: get the last 4 characters of code
reverse_code = code[::-1] # str: get code in reverse order

print(product_type)
print(year_text)
print(batch)
print(product_number)
print(first_half)
print(last_half)
print(reverse_code)
