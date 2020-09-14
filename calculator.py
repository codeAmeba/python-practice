def calculator(a, operator, b):
    if type(a) != int or type(b) != int:
        return "Please input only number."

    if operator == "plus":
        return a + b

    if operator == "minus":
        return a - b

    if operator == "multiply":
        return a * b

    if operator == "division":
        return a / b

    if operator == "reminder":
        return a % b

    if operator == "power":
        return a ** b


multiply6and7 = calculator(a="6", operator="multiply", b="7")
print(multiply6and7)

plus5and6 = calculator(a=5, operator="plus", b=6)
print(plus5and6)

division32and5 = calculator(a=32, operator="division", b=5)
print(division32and5)

power7and3 = calculator(a=7, operator="power", b=3)
print(power7and3)
