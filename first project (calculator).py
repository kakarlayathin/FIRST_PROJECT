print("===welcome to my calculator")
def calculator(a, b ,operator):
    if operator == "+":
        return a+b
    elif operator == "-":
        return a-b
    elif operator == "%":
        return a % b
    elif operator == "**":
        return a**b
    elif operator == "*":
        return a*b
    elif operator == "/":
        return a/b
    else:
        return "error: no result"

while True:
    print("=== new calculation===")
    num1 =(float(input("Enter your first number:")))
    op = (input("Enter operator (+,-,*,%,**):"))
    num2 = (float(input("Enter your second number:")))

    result = calculator(num1, num2, op)
    print("result:" , result)

    again = input("do u want to couninue (yes/no): ")
    if again != "yes":
        print("goodbye see u tomorrow")
        break