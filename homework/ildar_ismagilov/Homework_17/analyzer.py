import os
import argparse


def analyzer(path, text_to_find):
    list_of_files = os.listdir(path)
    for file in list_of_files:
        full_file_path = os.path.join(path, file)
        with open(full_file_path) as f:
            for line_number, line in enumerate(f.readlines(), start=1):
                index_of_line = line.find(text_to_find)
                if index_of_line != -1:
                    slice = line[index_of_line - 5:len(text_to_find) + index_of_line + 5]
                    yield slice, file, line_number


def print_results(found_result):
    slice, file, line_number = found_result
    print(f'Line = {slice}')
    print(f'File = {file}')
    print(f'Line number = {line_number}')


parser = argparse.ArgumentParser()
parser.add_argument('path', help='Path to files')
parser.add_argument('--text', help='Text to find in files')
parser.add_argument('--find_all', help='Flag to create generator of all finds', action='store_true')
args = parser.parse_args()

formed_sequence = analyzer(args.path, args.text)

if args.find_all:
    for result in formed_sequence:
        print_results(result)
else:
    try:
        print_results(next(formed_sequence))
    except StopIteration:
        print("No matches found.")
