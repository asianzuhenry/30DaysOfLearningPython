# Functions

def SayHello():
    print("Hello")

def SayHelloTo(name):
    print("Hello " + name)

def AddTwoNumbers(num1, num2):
    return num1 + num2

def SubtractTwoNumbers(num1, num2):
    return num1 - num2

def MultiplyTwoNumbers(num1, num2):
    return num1 * num2

def DivideTwoNumbers(num1, num2):
    if num2 == 0:
        return "Cannot divide by zero"
    return num1 / num2


SayHello()
SayHelloTo("Henry")
result1 = AddTwoNumbers(5, 15)
result2 = SubtractTwoNumbers(5, 3)
result3 = MultiplyTwoNumbers(5, 4)
result4 = DivideTwoNumbers(5, 2)

print("5 + 15 = " + str(result1))
print("5 - 3 = " + str(result2))
print("5 * 4 = " + str(result3))
print("5 / 2 = " + str(result4))


number = 12

def printGlobalNumber():
    number2 = 32
    print(number)

printGlobalNumber()