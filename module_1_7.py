#Словари
my_dict = {'Zorro': 1557456, 'Abracan': 789654123}
print(my_dict)
print(my_dict.get('Zorro'))
print(my_dict.get('Kisa'))
my_dict.update({'Villain': 45698755, 'Jim': 45621123})
print(my_dict)
del my_dict['Zorro']
print(my_dict)

#Множества
my_set = {0, 2, 5 , 5, 8, 9, 'f', 8}
print(my_set)
my_set.add((4, 'g', 8))
my_set.add(1)
print(my_set)
my_set.discard(6)
print(my_set)
