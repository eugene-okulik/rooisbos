def find_add10_print(string):
    resulting_number = int(string[string.index(':') + 1:]) + 10
    print(resulting_number)


result_1 = 'результат операции: 42'
find_add10_print(result_1)

result_2 = 'результат операции: 54'
find_add10_print(result_2)

result_3 = 'результат операции: 209'
find_add10_print(result_3)

result_4 = 'результат операции: 2'
find_add10_print(result_4)
