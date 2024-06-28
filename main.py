
def summ(a, b):
    return a + b


def dif(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a // b


def calculator(num1, num2, op):
    if op == "+":
        return summ(num1, num2)
    if op == "-":
        return dif(num1, num2)
    if op == "*":
        return mul(num1, num2)
    if op == ":":
        return div(num1, num2)
    return "Введен некорректный оператор"

print(calculator(5, 7, '+'))

# firstNumber = int(input("Введите первое число: "))
# secondNumber = int(input("Введите второе число: "))
# operand = input("Введите оператор: ")
#
# answer = calculator(firstNumber, secondNumber, operand)
#
# print("Ответ: ", answer)