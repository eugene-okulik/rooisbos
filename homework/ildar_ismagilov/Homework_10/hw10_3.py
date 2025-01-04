def calc_decor(func):
    def wrapper(*args):
        if args[0] < 0 or args[1] < 0:
            return func(*args, operation='*')
        elif args[0] == args[1]:
            return func(*args, operation='+')
        elif args[0] > args[1]:
            return func(*args, operation='-')
        elif args[0] < args[1]:
            return func(*args, operation='/')

    return wrapper


@calc_decor
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '*':
        return first * second
    elif operation == '/':
        return first / second


first_input = int(input('Enter the first number: '))
second_input = int(input('Enter the second number: '))

print(calc(first_input, second_input))
