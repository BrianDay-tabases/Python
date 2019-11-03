#CIT144 Python 1 Project #3
#Process Data In a Text File
#By Brian Day

totals = []
infile = open("C:\\Users\\aday\\Documents\\Python\\BrianDay-Project3\\grades.txt", "r")

def avgtoLetter(average) :
    if (average >= 90 and average < 100) :
        #recievedGrade = 'A'
        totals.append('a')
        print("Average: A")
    elif (average >= 80 and average < 89) :
        #recievedGrade = 'B'
        totals.append('b')
        print("Average: B")
    elif (average >= 70 and average < 79) :
        #recievedGrade = 'C'
        totals.append('c')
        print("Average: C")
    elif (average >= 60 and average < 69) :
        #recievedGrade = 'D'
        totals.append('d')
        print("Average: D")
    else : 
        #recievedGrade = 'F'
        totals.append('f')
        print("Average: F")
        

def main() :
    line = infile.readline()
    while line != "" :
        line = line.rstrip()
        splitLine = line.split()
        student = splitLine[0]
        print(student, end=" ")
        grade1 = int(splitLine[1])
        grade2 = int(splitLine[2])
        grade3 = int(splitLine[3])
        average = (grade1 + grade2 + grade3)/3
        avgtoLetter(average)
        line = infile.readline()

main()
print('Total number of A\'s: ', totals.count('a'))
print('Total number of B\'s: ', totals.count('b'))
print('Total number of C\'s: ', totals.count('c'))
print('Total number of D\'s: ', totals.count('d'))
print('Total number of F\'s: ', totals.count('f'))