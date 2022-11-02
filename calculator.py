"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )

print("Please enter an operand and 2 digits")
tokens = input().split(' ')

while tokens[0] != "q":
    if tokens[0] == "+":
        print(add(int(tokens[1]),int(tokens[2])))
        tokens = input().split(' ')

    elif tokens[0] == "-":
        print(subtract(int(tokens[1]),int(tokens[2])))
        tokens = input().split(' ')

    elif tokens[0] == "*":
        print(multiply(int(tokens[1]),int(tokens[2])))
        tokens = input().split(' ')

    elif tokens[0] == "/":
        print(divide(int(tokens[1]),int(tokens[2])))
        tokens = input().split(' ')

    elif tokens[0] == "square":
        print(square(int(tokens[1])))
        tokens = input().split(' ')

    elif tokens[0] == "cube":
        print(cube(int(tokens[1])))
        tokens = input().split(' ')

    elif tokens[0] == "pow":
        print(power(int(tokens[1]),int(tokens[2])))
        tokens = input().split(' ')

    elif tokens[0] == "mod":
        print(mod(int(tokens[1]),int(tokens[2])))
        tokens = input().split(' ')

    else:
        print("Please enter a valid operand: \n + , - , / , * , mod , square , cube , or pow seperated by spaces")
        tokens = input().split(' ')
