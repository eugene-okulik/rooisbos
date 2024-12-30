import datetime

date_to_change = 'Jan 15, 2023 - 12:05:33'
python_date = datetime.datetime.strptime(date_to_change, '%b %d, %Y - %H:%M:%S')
month_from_python_date = python_date.strftime('%B')
another_format_of_the_date = python_date.strftime('%d.%m.%Y, %H:%M')

print('Full month name from python_date:', month_from_python_date)
print('Another format of the date:', another_format_of_the_date)
