# 1. Создайте новую функцию def test_function
def test_function():

    # 2. Создайте другую функцию внутри функции inner_function,
    # функция должна печатать значение "Я в области видимости функции test_function"
    def inner_function():
        print('Я в области видимости функции test_function')

    # 3. Вызовите функцию inner_function внутри функции test_function
    inner_function()

# 4. Попробуйте вызывать inner_function вне функции test_function и посмотрите на результат выполнения программы
inner_function() #- NameError: name 'inner_function' is not defined. Did you mean: 'test_function'?
test_function()
# 5. Полученный код напишите в ответ к домашему заданию
