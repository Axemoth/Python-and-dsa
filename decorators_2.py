import time

def cache(func):
    cache_value = {}
    def wrapper(*args):
        if args in cache_value:
            return cache_value[args]
        result = func(*args)
        cache_value[args] = result
        return result
    return wrapper










@cache
def long_function(a,b):
    time.sleep(4)
    return a+b

print(long_function(2,3))
print(long_function(5,2))
print(long_function(2,3))
print(long_function(5,2))