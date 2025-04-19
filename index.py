def cleanExp(exp:str):
    calculations = ["+", "-", "*", "/"]
    result = []
    number = ""
    for e in exp:
        if e.isnumeric() or e == ".":
            number += e
        elif e in calculations:
            if number:
                result.append(float(number))
                number = ""
            result.append(e)
    if number:
        result.append(float(number))
    return result

def changeOperators(exp: list):
    i = 1
    if exp[0] == "+":
        exp[0:2] = [exp[1]]
    elif exp[0] == "-":
        exp[0:2] = [exp[1] * -1]
    while i < len(exp):
        if exp[i-1] in ["-", "+"] and exp[i] in ["-", "+"]:
            if exp[i-1] == "+" and exp[i] == "-":
                exp[i-1:i+1] = "-"
            elif exp[i-1] == "-" and exp[i] == "+":
                exp[i-1:i+1] = "-"
            elif exp[i-1] == "+" and exp[i] == "+":
                exp[i-1:i+1] = "+"
            elif exp[i-1] == "-" and exp[i] == "-":
                exp[i-1:i+1] = "+"
        i += 1
    return exp

def processExpression(exp):
    i = 1
    while i < len(exp):
        isNum = isinstance(exp[i-1], (float, int)) and isinstance(exp[i+1], (float, int))
        if exp[i] in ["*", "/"] and isNum:
            if exp[i] == "*":
                result = exp[i-1] * exp[i+1]
                exp[i-1:i+2] = [result]
            elif exp[i] == "/":
                if exp[i+1] == 0:
                    return "Error: Divition By Zero"
                result = exp[i-1] / exp[i+1]
                exp[i-1:i+2] = [result] 
        else:   
            i += 1
    i = 1
    result = exp[0]
    while i < len(exp):
        if exp[i] == "+":
            result += exp[i+1]
        elif exp[i] == "-":
            result -= exp[i+1]
        i += 2
    return result


print("- Welcome to the Python Calculator")
print("- You can enter a math expression using numbers and these operators: +  -  *  /")
print("- Example: 2 + 3 * 5 - 4 / 2")
print("- Decimal numbers are supported too (e.g., 3.5 * 2.1)")
print("- Note: Parentheses () and power ** are not supported yet")
print("- write a exit to stop calculate")
print("- Type your calculation and press Enter")
print("-" * 50)

while True:
    expression = input("Write your calculation: ").strip()
    if expression.lower() == "exit":
        print("-> nice to meet you")
        break
    preparedExp = cleanExp(expression)
    preparedExp = changeOperators(preparedExp)
    finalResult = processExpression(preparedExp)
    print(f"the final result equal = {finalResult}")

