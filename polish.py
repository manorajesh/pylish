def calculator(expression):
    ops = {
        "+": lambda x,y: x+y, 
        "-": lambda x,y: x-y, 
        "*": lambda x,y: x*y, 
        "/": lambda x,y: x/y, 
        "**": lambda x,y: x**y, 
        "//": lambda x,y: x//y, 
        "%": lambda x,y: x%y
        }

    stack = []
    for arg in expression[::-1]:
        if arg in ops:
            stack.append(ops[arg](stack.pop(), stack.pop()))
        else:
            stack.append(float(arg))
    return stack.pop()

while (ch := input("> ")) != 'q':
    print(calculator(ch.split()))