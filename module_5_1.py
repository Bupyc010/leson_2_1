def test_function():
    def inner_function():
        return 'Я в области видимости функции test_function'
    print(inner_function())

test_function()
#print(inner_function()) - выдаст ошибку "name 'inner_function' is not defined. Did you mean: 'test_function'" это говорит
#что данная функция находится в облости видимости 'test_function'
