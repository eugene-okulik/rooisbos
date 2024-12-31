temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27, 22, 22, 23, 25, 29, 29, 31, 33, 31, 30,
                32, 30, 28, 24, 23]

high_temperatures = list(filter(lambda x: x > 28, temperatures))
max_temperature = max(high_temperatures)
min_temperature = min(high_temperatures)
average_temperature = round(sum(high_temperatures) / len(high_temperatures), 1)

print(f'Max temperature in the list is {max_temperature}')
print(f'Min temperature in the list is {min_temperature}')
print(f'Average temperature in the list is {average_temperature}')
