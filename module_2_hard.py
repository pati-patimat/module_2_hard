def pairs_of_numbers(rand_number):
    pairs_numb = list()
    limit_first_numb = (rand_number + 1) // 2
    for i in range(1, limit_first_numb):
        j = i + 1
        while i + j <= rand_number:
            if rand_number % (i + j) == 0:
                tuple_numbers = (i, j)
                pairs_numb.append(tuple_numbers)
            j += 1
    return pairs_numb

l = True
while l:
    first_number = int(input('Введите число от 3 до 20: '))
    if first_number in range(3, 21):
        l = False
    else:
        print('Введено число за пределами интервала (от 3 до 20)')
        print('Пожалуйста, повторите ввод')
print('Для числа', first_number, 'подходят следующие пароли:', *pairs_of_numbers(first_number))