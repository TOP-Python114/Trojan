from time import perf_counter, perf_counter_ns

# ДОБАВИТЬ: аннотации типов параметров и возвращаемого значения, документацию для функции
def execution_func_second(func):
    def wrapper(*args, **kwargs):
        start_time = perf_counter()
        # ДОБАВИТЬ: сохранение возвращаемого значения декорируемой функции
        func(*args, **kwargs)
        finish_time = perf_counter()
        lead_time = finish_time - start_time
        # ИСПОЛЬЗОВАТЬ: возможности f-строк — например, округление
        print(f'Время выполнения функции составило {lead_time:.7f} секунд')
        # ИСПРАВИТЬ: вы возвращает объект декорируемой функции, в то время как необходимо вернуть возвращаемое значение декорируемой функции
        return func
    return wrapper

# ДОБАВИТЬ: аннотации типов параметров и возвращаемого значения, документацию для функции
def execution_func_nanosecond(func):
    def wrapper(*args, **kwargs):
        start_time = perf_counter_ns()
        # ДОБАВИТЬ: сохранение возвращаемого значения декорируемой функции
        func(*args, **kwargs)
        finish_time = perf_counter_ns()
        lead_time = finish_time - start_time
        print(f'Время выполнения функции составило {lead_time} наносекунд')
        # ИСПРАВИТЬ: вы возвращает объект декорируемой функции, в то время как необходимо вернуть возвращаемое значение декорируемой функции
        return func
    return wrapper


# КОММЕНТАРИЙ: это хороший подход, разделить на несколько декораторов
@execution_func_nanosecond
@execution_func_second
def func_sum(a, b):
    return a + b

# КОММЕНТАРИЙ: если бы вы попытались, например, напечатать возвращаемое значение этой функции, то вместо числа увидели бы None
func_sum(8, 4)


# stdout:
# Время выполнения функции составило 1.00000761449337e-06 секунд
# Время выполнения функции составило 57900 наносекунд


# ИТОГ: внимательнее с возвращаемыми объектами — 4/6