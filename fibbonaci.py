def program(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return program(num - 1) + program(num - 2)

def program1(num):
    if num == 0:
        return 1
    return (num * program1(num - 1))
