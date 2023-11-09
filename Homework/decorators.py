import time
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


print('*' * 3, '1', '*' * 3)


def first_dec(funk):
    def wrapper():
        print('Початок функії')
        funk()
        print('Кінець фугкції')

    return wrapper


@first_dec
def const_funk():
    print('Огого, це що, я потрапив в декоратор!?')


const_funk()


def WriteINFile(file_name):
    def decorator(funk):
        def wrapper():
            with open(file_name, 'a', encoding='UTF-8') as file:
                file.write(f'{funk()}\n')

        return wrapper

    return decorator


@WriteINFile('test.txt')
def text_in_file():
    return 'Я потрапив в файл!!!!!!!!!'


@WriteINFile('test.txt')
def text_in_file2():
    return 'А я тут'


text_in_file()
text_in_file2()

print('*' * 3, '3', '*' * 3)


def catch_decorator(funk):
    def wrapper():
        try:
            return funk()
        except Exception as E:
            return (f'Тут невелична плоблем: {E}')

    return wrapper


@catch_decorator
def problem_func():
    return 1 / 0


print(problem_func())

print('*' * 3, '4', '*' * 3)



def timer_decorator(funk):
    def wrapper():
        start=time.time()
        funk()
        end=time.time()
        print(f'Time: {end-start}')

    return wrapper

@timer_decorator
def sleep_funk():
    time.sleep(3)

sleep_funk()

print('*' * 3, '5', '*' * 3)

def log_decorator(funk):
    def wrapper():
        logging.info(funk())

    return wrapper

@log_decorator
def log_tester():
    return 33-2+13

log_tester()



print('*' * 3, '6', '*' * 3)


def limit_calls(max_calls):                      #не можу придумати як зберігати call.(можливо якось через yuild)...
    def decorator(func):
        call=0
        def wrapper():
            call=+1
            if call<max_calls:
                return func()
            else:
                raise Exception

        return wrapper
    return decorator

@limit_calls(3)
def some_function():
    print("Виклик функції")

some_function()
some_function()
some_function()
some_function()


print('*' * 3, '7', '*' * 3)

def cache_results(func):
    cache={}
    def wrapper(*args):
        if args not in cache:
            cache[args]=func(*args)
        return cache[args]

    return wrapper
@cache_results
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))  # Обчислюється
print(fibonacci(10))  # Використання кешу