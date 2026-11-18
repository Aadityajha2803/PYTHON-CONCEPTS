#PART-1
word = "glowing"
new_word = word
if new_word[-3:] == "ing":
    new_word = new_word[:-3]
    print(new_word)

#PART-2
age = int(input("Enter your age: "))
if age < 18:
    print("Child")
else:
    print("Adult")

#PART-3
colour_code = input("Enter your code: ")
if colour_code == "R":
    print("Red")
elif colour_code == "B":
    print("Blue")
elif colour_code == "G":
    print("Green")
else:
    print("Black")

#PART-4
time = input("Enter your time: ")
is_time_valid = 0<int(time[:2])<=12
time_in_hrs = int(time[:2])%12 + (time[-2:] == "PM") * 12
print(is_time_valid)
print(time_in_hrs)

if not is_time_valid:
    print("Time is invalid")
elif is_time_valid < 6:
    print("Night")
elif is_time_valid < 12:
    print("Morning")
elif is_time_valid < 18:
    print("Afternoon")
else:
    print("Evening")

