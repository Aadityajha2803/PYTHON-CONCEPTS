name = input("Enter your name: ")
Age = int(input("Enter your age: "))
Degree_level = input("Enter the level you're currently in: ")
subject_number = int(input("Enter your subject number: "))
subject1_marks = int(input("Enter your subject 1 marks: "))
subject2_marks = int(input("Enter your subject 2 marks: "))
subject3_marks = int(input("Enter your subject 3 marks: "))
average = int((subject1_marks + subject2_marks + subject3_marks)/3)
print("Your average marks is: ", average)
if average > 80:
    print("Grade A")
elif average > 70:
    print("Grade B")
elif average > 60:
    print("Grade C")
elif average > 50:
    print("Grade D")
elif average > 40:
    print("Grade E")
else:
    print("Sorry you did not qualify: U GRADE")

if subject1_marks < 40:
    marks = 40 - subject1_marks
    print("To pass Subject-1 you require this much marks more:",marks)

if subject2_marks < 40:
    marks = 40 - subject2_marks
    print("To pass Subject-2 you require this much marks more:", marks)

if subject3_marks < 40:
    marks = 40 - subject3_marks
    print("To pass Subject-3 you require this much marks more:", marks)

if average < 50:
    marks = 50 - average
    print("You needed this much marks more to pass the term in average: ",marks)

if subject1_marks > 90:
    print("CONGRATULATIONS! You got S GRADE in Subject-1")

if subject2_marks > 90:
    print("CONGRATULATIONS! You got S GRADE in Subject-2")

if subject3_marks > 90:
    print("CONGRATULATIONS! You got S GRADE in Subject-3")


