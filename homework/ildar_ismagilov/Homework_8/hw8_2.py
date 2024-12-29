import sys

sys.set_int_max_str_digits(100000)


def fibonacci_generator():
    first_term = 0
    second_term = 1
    while True:
        yield first_term
        first_term, second_term = second_term, first_term + second_term


generated_sequence = fibonacci_generator()
wished_positions = (5, 200, 1000, 100000)
counter = 1

for fibonacci_number in generated_sequence:
    if counter in wished_positions:
        print(fibonacci_number)
        if counter == wished_positions[-1]:
            break
    counter += 1
