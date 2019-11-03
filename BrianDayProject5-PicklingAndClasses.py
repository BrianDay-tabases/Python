#CIT144 Python 1 Project #5
#Pickles and Classes
#By Brian Day

import pickle

class Student(object) :
    def __init__(stu, stuid, name, midterm, final) : #__init__ 
        stu.id = stuid
        stu.mid = midterm
        stu.fin = final
        stu.nam = name
        
    def totaLetter(stu) :
        return round(stu.mid + stu.fin)/2
        
    def studentInfo(stu) :
        letter = stu.totaLetter()
        if (letter >= 90 and letter < 100) :
            letter = 'A'
        elif (letter >= 80 and letter < 89) :
            letter = 'B'
        elif (letter >= 70 and letter < 79) :
            letter = 'C'
        elif (letter >= 60 and letter < 69) :
            letter = 'D'
        else :
            letter = 'F'
        return stu.id, stu.nam, stu.mid, stu.fin, letter


def displayStudents(students) :
    print("Student         Midterm|Final|Letter")
    print("  ID  -- Name --  Score|Score|Grade")
    for student in students :
        print(students[student].studentInfo())
        
def addStudent(CIT101) :
    student_id = input("Enter StudentID: ")
    nam = input("In format 'lastname,firstname' Enter Student Name: ")
    mid = int(input("Enter midterm exam score: "))
    fin = int(input("Enter final exam score: "))
    CIT101[student_id] = Student(student_id, nam, mid, fin)
    return CIT101

def fileReading(filename) :
    try :
        file = open(filename, "rb")
        CIT101 = pickle.load(file)
        file.close()
    except IOError:
        CIT101 = {}
    return CIT101

def fileSaving(filename, CIT101) :
    file = open(filename, "wb")
    pickle.dump(CIT101, file)
    file.close()
    
def deleteStudent(CIT101, student_id) :
    del CIT101[student_id]
    return CIT101

def main() :
    filename = "students2.txt"
    students = fileReading(filename)
    
    saveandexit = False
    while saveandexit == False :
        print("--Menu options. Choose a number:--")
        print("  1.Display all students")
        print("  2.Add a student")
        print("  3.Display a particular student")
        print("  4.Delete a student")
        print("  5.Save and exit")
        userchoice = input("Enter your choice 1  2  3  4  5 :")
        print()
        
        if userchoice == "1" :
            displayStudents(students)
        elif userchoice == "2" :
            students = addStudent(students)
        elif userchoice == "3" :
            print()
            student_id = input("Enter particular students ID: ")
            print("Student|Midterm|Final|Letter")
            print("  Name |Score  |Score|Grade")
            print(students[student_id].studentInfo())
        elif userchoice == "4" :
            print()
            student_id = input("Enter the ID of student to delete: ")
            students = deleteStudent(students, student_id)
        elif userchoice == "5" :
            fileSaving(filename, students)
            print("Thank you for using my program!")
            saveandexit = True
            break

main()