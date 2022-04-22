# Age left in days, weeks and months.
age = input("what is your current age")
yearsLeft = 90 - int(age) # Assuming the lifetime is 90years.
daysLeft = 365  * yearsLeft
weeksLeft = 52 * yearsLeft
monthsLeft = 12 * yearsLeft
print(f"you have {daysLeft} days, {weeksLeft} weeks, {monthsLeft} months left.")

# Calculator
firstNumber = input("Enter first Number")
secondNumber = input("Enter second Number")
addition = int(firstNumber) + int(secondNumber)
print("Addition - " + str(addition))
subtraction = int(firstNumber) - int(secondNumber)
print("subtraction - " + str(subtraction))
multiplication = int(firstNumber) * int(secondNumber)
print("multiplication - " + str(multiplication))
division = int(firstNumber) / int(secondNumber)
print("division - " + str(division))

# Speed Calculator
distance = input("Enter your distance")
time = input("Enter your time")
speed = int(distance)/int(time)
print(str(speed) +  " " + "m/s")

# ArithmeticOperations of 1stdigit of 1st number and 2nd digit of 2nd number and 3rd digit of 3rd number
firstNumber = input("Enter first number")
secondNumber = input("Enter second number")
thirdNumber = input("Enter third number")
firstDigit = firstNumber[0]
secondDigit = secondNumber[1]
thirdDigit = thirdNumber[2]
addition = int(firstDigit) + int(secondDigit) + int(thirdDigit)
print("addition-" + str(addition))
subtraction = int(firstDigit) - int(secondDigit) - int(thirdDigit)
print("subtraction-" + str(subtraction))
multiplication = int(firstDigit) * int(secondDigit) * int(thirdDigit)
print("multiplication-" + str(multiplication))
division = int(firstDigit) / int(secondDigit) / int(thirdDigit)
print("division-" + str(division))

# Per Person bill calculator
Bill = float(input("what was the total bill?"))
totalPersons = int(input("How many people to split the bill?"))
percentage = float(input("what percentage tip would you like to give?"))
tip =(Bill/100)*percentage
totalAmount = Bill+tip
eachPersonBill = round(totalAmount/totalPersons,2)
print(f"Each person should pay: {eachPersonBill}")
