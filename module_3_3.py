def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)


values_list_2 = [45673.78, 'Строка', 45]
values_dict = {'a': 45, 'b': 'string', 'c': False}
values_list_3 = [54.32, 'Строка' ]

print_params(*values_list_3, 42)
print_params(*values_list_2)
print_params(**values_dict)