name = input("Enter your name: ")
age = int(input("Enter your age: "))
current_level = input("Enter the program you're currently enrolled in: ")
number_of_subjects = int(input("Enter the number of subjects you have: "))
if number_of_subjects == 4:
    subject1 = input("Enter your first subject: ")
    subject2 = input("Enter your second subject: ")
    subject3 = input("Enter your third subject: ")
    subject4 = input("Enter your fourth subject: ")
    marks_of_subject1 = int(input("Enter the marks you got in the first subject: "))
    marks_of_subject2 = int(input("Enter the marks you got in the second subject: "))
    marks_of_subject3 = int(input("Enter the marks you got in the third subject: "))
    marks_of_subject4 = int(input("Enter the marks you got in the fourth subject: "))
    
    average = int((marks_of_subject1 + marks_of_subject2 + marks_of_subject3 + marks_of_subject4)/4)

    if marks_of_subject1 > 90:
        print("CONGRATULATIONS! YOU GOT S GRADE in your first subject")
    elif marks_of_subject1 > 80:
        print("You got A Grade in your first subject")
    elif marks_of_subject1 > 70:
        print("You got B Grade in your first subject")
    elif marks_of_subject1 > 60:
        print("You got C grade in your first subject")
    elif marks_of_subject1 > 50:
        print("You got D grade in your first subject")
    elif marks_of_subject1 > 40:
        print("You got E grade in your first subject")
    else:
        print("You Failed... You got a U grade in your first subject")
    
    if marks_of_subject2 > 90:
        print("CONGRATULATIONS! YOU GOT S GRADE in your in your second subject")
    elif marks_of_subject2 > 80:
        print("You got A Grade in your second subject")
    elif marks_of_subject2 > 70:
        print("You got B Grade in your second subject")
    elif marks_of_subject2 > 60:
        print("You got C grade in your second subject")
    elif marks_of_subject2 > 50:
        print("You got D grade in your second subject")
    elif marks_of_subject2 > 40:
        print("You got E grade in your second subject")
    else:
        print("You Failed... You got a U grade in your second subject")
    
    if marks_of_subject3 > 90:
        print("CONGRATULATIONS! YOU GOT S GRADE in your third subject")
    elif marks_of_subject3 > 80:
        print("You got A Grade in your third subject")
    elif marks_of_subject3 > 70:
        print("You got B Grade in your third subject")
    elif marks_of_subject3 > 60:
        print("You got C grade in your third subject")
    elif marks_of_subject3 > 50:
        print("You got D grade in your third subject")
    elif marks_of_subject3 > 40:
        print("You got E grade in your third subject")
    else:
        print("You Failed... You got a U grade in your third subject")
    
    if marks_of_subject4 > 90:
        print("CONGRATULATIONS! YOU GOT S GRADE in your fourth subject")
    elif marks_of_subject4 > 80:
        print("You got A Grade your fourth subject")
    elif marks_of_subject4 > 70:
        print("You got B Grade your fourth subject")
    elif marks_of_subject4 > 60:
        print("You got C grade your fourth subject")
    elif marks_of_subject4 > 50:
        print("You got D grade your fourth subject")
    elif marks_of_subject4 > 40:
        print("You got E grade your fourth subject")
    else:
        print("You Failed... You got a U grade your fourth subject")
    print("Your Average is: ",average)
    
elif number_of_subjects == 3:
    subject1 = input("Enter your first subject: ")
    subject2 = input("Enter your second subject: ")
    subject3 = input("Enter your third subject: ")
    marks_of_subject1 = int(input("Enter the marks you got in the first subject: "))
    marks_of_subject2 = int(input("Enter the marks you got in the second subject: "))
    marks_of_subject3 = int(input("Enter the marks you got in the third subject: "))
        
    average = int((marks_of_subject1 + marks_of_subject2 + marks_of_subject3)/3)
    
    if marks_of_subject1 > 90:
        print("CONGRATULATIONS! YOU GOT S GRADE in your first subject")
    elif marks_of_subject1 > 80:
        print("You got A Grade in your first subject")
    elif marks_of_subject1 > 70:
        print("You got B Grade in your first subject")
    elif marks_of_subject1 > 60:
        print("You got C grade in your first subject")
    elif marks_of_subject1 > 50:
        print("You got D grade in your first subject")
    elif marks_of_subject1 > 40:
        print("You got E grade in your first subject")
    else:
        print("You Failed... You got a U grade")
    
    if marks_of_subject2 > 90:
            print("CONGRATULATIONS! YOU GOT S GRADE")
    elif marks_of_subject2 > 80:
        print("You got A Grade in your second subject")
    elif marks_of_subject2 > 70:
        print("You got B Grade in your second subject")
    elif marks_of_subject2 > 60:
        print("You got C grade in your second subject")
    elif marks_of_subject2 > 50:
        print("You got D grade in your second subject")
    elif marks_of_subject2 > 40:
        print("You got E grade in your second subject")
    else:
        print("You Failed... You got a U grade in your second subject")
    
    if marks_of_subject3 > 90:
        print("CONGRATULATIONS! YOU GOT S GRADE in your second subject")
    elif marks_of_subject3 > 80:
        print("You got A Grade in your third subject")
    elif marks_of_subject3 > 70:
        print("You got B Grade in your third subject")
    elif marks_of_subject3 > 60:
        print("You got C grade in your third subject")
    elif marks_of_subject3 > 50:
        print("You got D grade in your third subject")
    elif marks_of_subject3 > 40:
        print("You got E grade in your third subject")
    else:
        print("You Failed... You got a U grade in your third subject")
    print("Your Average is: ",average)

elif number_of_subjects == 2:
    subject1 = input("Enter your first subject: ")
    subject2 = input("Enter your second subject: ")
    marks_of_subject1 = int(input("Enter the marks you got in the first subject: "))
    marks_of_subject2 = int(input("Enter the marks you got in the second subject: "))
            
    average = int((marks_of_subject1 + marks_of_subject2)/2)
        
    if marks_of_subject1 > 90:
        print("CONGRATULATIONS! YOU GOT S GRADE in your first subject")
    elif marks_of_subject1 > 80:
        print("You got A Grade in your first subject")
    elif marks_of_subject1 > 70:
        print("You got B Grade in your first subject")
    elif marks_of_subject1 > 60:
        print("You got C grade in your first subject")
    elif marks_of_subject1 > 50:
        print("You got D grade in your first subject")
    elif marks_of_subject1 < 40:
        print("You got E grade in your first subject")
    else:
        print("You Failed... You got a U grade in your first subject")
    
    if marks_of_subject2 > 90:
            print("CONGRATULATIONS! YOU GOT S GRADE in your second subject")
    elif marks_of_subject2 > 80:
        print("You got A Grade in your second subject")
    elif marks_of_subject2 > 70:
        print("You got B Grade in your second subject")
    elif marks_of_subject2 > 60:
        print("You got C grade in your second subject")
    elif marks_of_subject2 > 50:
        print("You got D grade in your second subject")
    elif marks_of_subject2 > 40:
        print("You got E grade in your second subject")
    else:
        print("You Failed... You got a U grade in your second subject")
    print("Your Average is: ",average)
else:
    subject1 = input("Enter your first subject: ")
    marks_of_subject1 = int(input("Enter the marks you got in the first subject: "))
                
    average = int((marks_of_subject1)/1)
            
    if marks_of_subject1 > 90:
        print("CONGRATULATIONS! YOU GOT S GRADE in your subject")
    elif marks_of_subject1 > 80:
        print("You got A Grade in your subject")
    elif marks_of_subject1 > 70:
        print("You got B Grade in your subject")
    elif marks_of_subject1 > 60:
        print("You got C grade in your subject")
    elif marks_of_subject1 > 50:
        print("You got D grade in your subject")
    elif marks_of_subject1 > 40:
        print("You got E grade in your subject")
    else:
        print("You Failed... You got a U grade in your subject")
    print("Your Average is: ",average)




