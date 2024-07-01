"""
WAP to create a decorator function which when applied to a function gives the execution time
of the function
"""
import time

def time_taken(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Taken time is {end_time - start_time} seconds")
        return result
    return wrapper

@time_taken
def long_loop():
    for i in range(100000000):
        pass

long_loop()
