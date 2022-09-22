from time import perf_counter, perf_counter_ns

def execution_func_second(func):
    def wrapper(*args, **kwargs):
        start_time = perf_counter()
        func(*args, **kwargs)
        finish_time = perf_counter()
        lead_time = finish_time - start_time
        print(f'Время выполнения функции составило {lead_time} секунд')
        return func
    return wrapper

def execution_func_nanosecond(func):
    def wrapper(*args, **kwargs):
        start_time = perf_counter_ns()
        func(*args, **kwargs)
        finish_time = perf_counter_ns()
        lead_time = finish_time - start_time
        print(f'Время выполнения функции составило {lead_time} наносекунд')
        return func
    return wrapper

@execution_func_nanosecond
@execution_func_second
def func_sum(a, b):
    return a + b
func_sum(8, 4)

# stdout:
# Время выполнения функции составило 1.00000761449337e-06 секунд
# Время выполнения функции составило 57900 наносекунд
