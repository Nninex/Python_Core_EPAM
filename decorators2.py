'''
Functions. Decorators. Decorators. Task 2 
Write a decorator which logs information about calls of decorated function, values of its arguments, values of keyword arguments and execution time.
Log should be written to a file. 
Example of using 
@log
def foo(a, b, c):
...
 foo(1, 2, c=3)

log.txt 
...
foo; args: a=1, b=2; kwargs: c=3; execution time: 0.12 sec.
...
'''
import time

def log(fn):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = fn(*args, **kwargs)
        time.sleep(0.05)
        end = time.time()
        running_time = end - start

        args_str = ", ".join(f"{name}={value}" 
                             for name, value in zip(fn.__code__.co_varnames, args))
        kwargs_str = ", ".join(f"{k}={v}" for k, v in kwargs.items())

        with open("log.txt", "a") as f:
            f.write(
                f"{fn.__name__}; "
                f"args: {args_str}; "
                f"kwargs: {kwargs_str}; "
                f"execution time: {running_time:.2f} sec.\n"
            )
        return result
    return wrapper
