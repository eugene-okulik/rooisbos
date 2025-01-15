import os
import datetime

base_path = os.path.dirname(__file__)
homework_path = os.path.dirname(os.path.dirname(base_path))
eugene_file_path = os.path.join(homework_path, "eugene_okulik", "hw_13", "data.txt")


def read_file():
    with open(eugene_file_path, "r") as data_file:
        for line in data_file.readlines():
            yield line


data_line = read_file()


def generating_datetime_object(line_from_file):
    return datetime.datetime.strptime(next(line_from_file)[3:29], "%Y-%m-%d %H:%M:%S.%f")


print(generating_datetime_object(data_line) + datetime.timedelta(days=7))
print(generating_datetime_object(data_line).today().weekday())
print((datetime.datetime.today() - generating_datetime_object(data_line)).days)
