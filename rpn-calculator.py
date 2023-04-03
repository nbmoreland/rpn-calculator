import os

# Operands for our function
OPERANDS = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b
}

# Calculate our result for the given RPN expression
def calculate_result( expression ):
    stack = []

    for key in expression:
        if key in OPERANDS:
            b = stack.pop()
            a = stack.pop()

            result = OPERANDS[key](a, b)
            stack.append(result)
        else:
            stack.append( int( key ))
    return stack.pop()

with open( os.path.join( os.getcwd(), "input_RPN.txt"), "r" ) as file:
    for line in file:
        line = line.rstrip("\n")
        expression = line.split()

        result = calculate_result( expression )
        print( result )