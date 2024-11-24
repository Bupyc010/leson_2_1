def generator_password(n):
    result = ''

    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            pair_sum = i + j
            if n % pair_sum == 0:
                result += f"{i}{j}"
    return result


while True:
    n = int(input('Ведите число от 3 до 20: '))
    if 3 <= n <= 20:
        break
    else:
        print('Введите правельное число.')

print(f"Нужный пароль для числа {n}: " + generator_password(n))

