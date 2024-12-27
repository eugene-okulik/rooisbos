import random

random_number = random.randint(0, 9)
while True:
    input_from_user = input('Enter a number: ')
    if input_from_user.isnumeric():
        input_from_user = int(input_from_user)
        if input_from_user == random_number:
            print("Bull's eye!")
            break
        else:
            print('Try again!')
    else:
        print('Enter a number, please!')
