#CIT144 Python 1 Project #2
#Exam Average Loop
#By Brian Day

print("Exam Grade Average Calculator")
print("The scores can be integers or floats")

proceed = True
score_quantity = 0
score_sum = 0
average = 0
while (proceed == True):
    request_response = input("Enter an exam score. 999 to quit: ")
    response = float(request_response)
    if (response == 999):
        proceed = True
        break
    elif (response < 0 or response > 100):
        print("Score is not in range. Please re-enter")
    else :
        score_quantity = score_quantity + 1
        score_sum = score_sum + response

average = score_sum / score_quantity
print("These ", score_quantity, " scores average as: ", ("%.1f" % average))  