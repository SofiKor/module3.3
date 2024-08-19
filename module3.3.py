def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

# print_params( )
# print_params(1, 2, 4, )
# print_params(b = 25)
# print_params(c = [1,2,3])
values_list_2 = [54.32, 'Строка']
values_dict = {'a': 6, 'b': 9, 'c': 34}
values_list = [1, 5, 9]
# print_params(*values_list)
# print_params(**values_dict)
print_params(*values_list_2, 42)

