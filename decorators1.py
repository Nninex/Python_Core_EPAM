'''
Functions. Decorators. Decorators. Task 1. 
 Create a decorator function time_decorator which has to calculate decorated function execution time and put this time value to execution_time
dictionary where key is decorated function name and value is this function execution time. For example: ```python @time_decorator def func_add(a, b):
sleep(0.2) return a + b 
func_add(10, 20) 30 
execution_time[‘func_add’] 0.212341254 ``
'''
from typing import Dict
import time

execution_time: Dict[str, float] = {}


def time_decorator(fn):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = fn(*args, **kwargs)
        end = time.time()
        execution_time[fn.__name__] = round(end - start, 9)
        return result
    return wrapper


@time_decorator
def func_add(a, b):
    time.sleep(0.2)
    return a + b


func_add(2, 3)  # call the function
print(execution_time['func_add'])
