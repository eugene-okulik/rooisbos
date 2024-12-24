import pprint

# creating my_dict
my_dict = {
    'tuple': (1, 2, True, 'test', "OK, let's go!"),
    'list': [False, 'test2', '', 0, 1.5],
    'dict': {
        1: True,
        2: False,
        3: None,
        4: 'test_str',
        5: 0
    },
    'set': {100, 200, '100', '200', None}
}
# manipulations with tuple-key
print(my_dict['tuple'][-1])
print('-' * 25)
# manipulations with list-key
my_dict['list'].append('another element')
my_dict['list'].pop(1)
# manipulations with dict-key
my_dict['dict'][('i am a tuple',)] = 'asdf'
del my_dict['dict'][3]
# manipulations with set-key
my_dict['set'].add(True)
my_dict['set'].remove('200')

# pretty printing
pprint.pprint(my_dict)
