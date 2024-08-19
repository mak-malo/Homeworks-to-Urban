def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')
    inner_function()

test_function() #Вызов основной функции. В результате получим вывод фразы в консоли.
inner_function() #Вызов вложенной функции снуружи функции test_function. В консоли выводится ошибка