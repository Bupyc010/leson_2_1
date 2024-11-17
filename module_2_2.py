first, second, third = (int(input('Введите первое число для сравнения: ')),
                        int(input('Введите второе число для сравнения: ')),
                        int(input('Введите третье число для сравнения: ')))
count_compare = 0
if(first == second or first == third):
    count_compare += 1
if(second == first or second == third):
    count_compare += 1
if(third == first or third == second):
    count_compare += 1

print(f'кол-во одинаковых чисел среди 3-х введённых: {count_compare}')