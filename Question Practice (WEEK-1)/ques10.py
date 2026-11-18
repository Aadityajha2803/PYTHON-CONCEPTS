age = int(input()) # int: Read a number as integer from standard input
dob = str(input()) # str: Read a string of format dd/mm/yy from standard input
day, month, year = int(dob[0:2]), int(dob[3:5]), int(dob[6::]) # int, int, int: Get the correct parts from dob as int

fifth_birthday = str(str(day) + "/" + str(month) + "/" + str(int(year+5))) # str: fifth birthday formatted as day/month/year 

last_birthday = str(str(day) + "/" + str(month) + "/" + str(int(year+age))) # str: last birthday formatted as day/month/year

tenth_month = str(str(day) + "/" + str(month + 10 < 12 and month + 10 or month + 10 - 12) + "/" + str(year + (month + 10 < 12 and 0 or 1))) # str: dob same day after 10 months formatted as day/month/year

# print tenth_month, fifth_birthday and last_birthday in same line separated by comma and a space
print(tenth_month + ", " + fifth_birthday + ", " + last_birthday)