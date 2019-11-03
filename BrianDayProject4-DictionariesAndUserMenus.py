#CIT144 Python 1 Project #4
#Dictionaries and Main Menu Options
#By Brian Day

def setup() :
    f = open("C:\\Users\\aday\\Documents\\Python\\students.txt", "r")
    students = {}

    for line in f :
        name, s1, s2, s3 = line.split(",")
        s1 = int(s1)
        s2 = int(s2)
        s3 = int(s3)
        students[name] = [s1, s2, s3] 
    f.close()
    return students
 
def userchose1(students) :
    print("--Student:  Score1 Score2 Score3--")
    for name in students :
        s1, s2, s3 = students[name]
        print(name, " ",s1, "   ",s2, "   ",s3)

def userchose2(students) :
    name = input("Enter new student name: ")
    s1 = input("Enter their first score: ")
    s1 = int(s1)
    s2 = input("Enter their second score: ")
    s2 = int(s2)
    s3 = input("Enter their third score: ")
    s3 = int(s3)
    students[name] = s1, s2, s3


def userchose3(students) :
    print("--Student: ---Avg--")
    for name in students :
        s1, s2, s3 = students[name]
        average = (s1 + s2 + s3)/3
        print(name, average)

def userchose4(students) :
    outfile = open("C:\\Users\\aday\\Documents\\Python\\students.txt", "w")
    for name in students :
        s1, s2, s3 = students[name]
        
        outline = name +","+str(s1)+","+str(s2)+","+str(s3)+"\n"
        outfile.write(outline)
    outfile.close
    
def main() :
    students = setup()
    saveandexit = False
    while saveandexit == False :
        print("--- Menu options. Choose 1, 2, 3, or 4 ---")
        print(" 1. Display student names and scores")
        print(" 2. Add a new student")
        print(" 3. Display exam averages")
        print(" 4. Save and exit")
        userchoice = input("Your choice: ")
        print()
        if userchoice == "1" :
            userchose1(students)                                                          
        elif userchoice == "2" :
            userchose2(students)
        elif userchoice == "3" :
            userchose3(students)
        elif userchoice == "4" :
            userchose4(students)
            saveandexit = True
            break

main()