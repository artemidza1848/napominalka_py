def plus(number1, number2):
    print(number1 + number2)

def minus(number1, number2):
    print(number1 - number2)

def multiply(number1, number2):
    print(number1 * number2)

def devision(number1, number2):
    print(number1 / number2)

number1 = int(input("Введите число: "))
number2 = int(input("Введите число: "))
access = input("Выберите +, -, * или /")

if access=="+":
    plus(number1, number2)
elif access=="-":
    minus(number1, number2)