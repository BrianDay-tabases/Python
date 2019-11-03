#CIT144 Python 1 Project
#Fahrenheit and Celsius Script
#By Brian Day

firstInput = input("Enter a temperature to convert: ")
user_temp = float(firstInput)

#Original Logic for attaining user response value, then tried 'desired_conversion'
#secondInput = input("Convert this to Fahrenheit or Celsius? Enter F or C: ")
#user_response = str(secondInput)

secondInput = input("Convert this to Fahrenheit or Celsius? Enter F or C: ")
desired_conversion = str.upper(secondInput)

#Original Attempt at processing user response
#if (user_response == 'f' | 'F') :
#   convert_to = 'F'
#elif (user_response == 'c' | 'C') :
#   convert_to = 'C'
#else :
#   print("You did not enter F or C. Goodbye")
#   quit()

#Original Set-up for Converting
#if convert_to == 'F':
#    converted_temp = 1.8 * user_temp + 32
#elif convert_to == 'C':
#    converted_temp = (user_temp - 32) / 1.8

if desired_conversion == 'F':
    converted_temp = 1.8 * user_temp + 32
    ogUnitofMeasurement = 'C'
elif desired_conversion == 'C':
    converted_temp = (user_temp - 32) / 1.8
    ogUnitofMeasurement = 'F'
else:
    exit("You did not enter F or C. Goodbye")

print(user_temp, "deg ", ogUnitofMeasurement, " = ", ("%.1f" % converted_temp), " deg ", desired_conversion)