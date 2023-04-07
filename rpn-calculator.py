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
    # Init our stack
    stack = []

    # Looping through each char in the expression
    for key in expression:
        # Checking if it matches one of our operands
        if key in OPERANDS:
            # Popping b & a from the stack
            b = stack.pop()
            a = stack.pop()

            # Performing our operand function with a & b
            result = OPERANDS[key](a, b)
            # Adding the result to the stack
            stack.append(result)
        else:
            # Adding integers to our stack
            stack.append( int( key ))
    # Returning the result
    return stack.pop()

# Opening our input_RPN.txt file
with open( os.path.join( os.getcwd(), "input_RPN.txt"), "r" ) as file:
    # Looping through each line in the file
    for line in file:
        # Splitting each line with the \n char
        line = line.rstrip("\n")
        expression = line.split()

        # Passing our expression to our function to calculate
        result = calculate_result( expression )
        # Printing out our result
        print( result )