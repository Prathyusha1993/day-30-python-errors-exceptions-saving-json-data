# FileNotFoundError
# with open('a_file.txt', 'r') as file:
#     file.read()
from importlib.resources import as_file

try:
    file = open('a_file.txt')
    a_dict={'key':'value'}
    print(a_dict['key'])
except FileNotFoundError:
    file = open('a_file.txt', 'w')
    file.write('Something')
except KeyError as error_message:
    print(f'the key {error_message} does not exists.')
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print('file was closed.')
    # raise KeyError
    # raise TypeError('this is an error')



# KeyError
# a_dictionary= {'key':'value'}
# value = a_dictionary['non_existent_key']

# IndexError
# fruit_list = ['Apple', 'Banana', 'Pear']
# fruit = fruit_list[3]

# TypeError
# text = 'abc'
# print(text + 5)