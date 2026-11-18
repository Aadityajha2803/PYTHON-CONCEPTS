weight = float(input()) # float: Read a number as float from stdin(Standard input)
kg = int(weight)
grams = (weight - int(weight)) * 1000
weight_readable = str(str(kg) + " Kg " + str(grams) + " Grams") # str: reformat weight of format 55 kg 250 grams

# print weight_readable 
print(weight_readable)

