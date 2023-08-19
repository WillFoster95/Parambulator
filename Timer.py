import functools
import time

def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        t1=time.time()
        value = func(*args, **kwargs)
        t2=time.time()
        print(f"{func.__name__}: {round(t2-t1, 3)}   ")
        return value
    return wrapper