userInput = input("Please enter FirstNumber, SecondNumber, Operator, e.g 5,10,+: ")
userInputValues = userInput.split(",")
firstNumber = int(userInputValues[0])
secondNumber = int(userInputValues[1])
operator = userInputValues[2]
print(operator)

if (operator == "+"):
    result = firstNumber + secondNumber
    print(f"{firstNumber} {operator} {secondNumber} = {result}")
elif(operator == "-"):
    result = firstNumber - secondNumber
    print(f"{firstNumber} {operator} {secondNumber} = {result}")
elif(operator == "*"):
    result = firstNumber * secondNumber
    print(f"{firstNumber} {operator} {secondNumber} = {result}")
elif(operator == "/"):
    if(secondNumber == 0):
        print("You can not divide by Zero")
    else:
        result = firstNumber / secondNumber
        print(f"{firstNumber} {operator} {secondNumber} = {result}")
else:
    print("Please Enter in Correct format")
