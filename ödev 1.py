import math

op = input("enter op = ")

if op == "+":
    a = float(input("enter a = "))
    b = float(input("enter b = "))

if op == "-":
    a = float(input("enter a = "))
    b = float(input("enter b = "))

if op == "*":
    a = float(input("enter a = "))
    b = float(input("enter b = "))

if op == "/":
    a = float(input("enter a = "))
    b = float(input("enter b = "))

if op == "sin":
    x = float(input("enter x = "))

if op == "cos":
    x = float(input("enter x = "))

if op == "tan":
    x = float(input("enter x = "))

if op == "cot":
    x = float(input("enter x = "))

if op == "factorial":
    c = int(input("enter c = "))

if op == "radical":
    c = float(input("enter c = "))

if op == "+":
    result = a + b

if op == "-":
    result = a - b

if op == "*":
    result = a * b

if op == "/":
    if b == 0:
        result = "error"
    else:
        result = a / b

if op == "sin":
    result = math.sin(x)

if op == "cos":
    result = math.cos(x)

if op == "tan":
    result = math.tan(x)

if op == "cot":
    result = (math.cos(x) * math.sin(x) )
    

if op == "factorial":
    result = math.factorial(c)

if op == "radical":
    result = math.sqrt(c)

print(result)
