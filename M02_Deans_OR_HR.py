
#Micqyela Santana-Perez
#M02_Deans_OR_HR
#This Python program will aske for a student's name and GPA to check is if they are qualified for the Dean's list od Honor Roll. 
#GPA of 3.5+ made the Dean's List. GPA of 3.25+ made Honor Roll.

l_name = input("Enter your last name or ZZZ to quit: ")

while (l_name != "ZZZ") :
    f_name = input("Enter your first name: ")
    student_gpa = float(input("Enter your GPA: "))
    if (student_gpa >= 3.5):
        print(f_name, l_name, "has made the Dean's List.")
    elif (student_gpa >= 3.25):
        print(f_name, l_name, "has made the Honor Roll.")
    else:
        print(f_name, l_name, "has NOT made the Dean's List or the Honor Roll.")
    l_name = input("Enter your last name or ZZZ to quit: ")
print("Thanks for using my program!")