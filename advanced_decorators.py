import time
from functools import wraps

def cache(func):
    cache_value = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        # Create a unique key from args + sorted kwargs
        key = (args, tuple(sorted(kwargs.items())))

        if key in cache_value:
            return cache_value[key]

        result = func(*args, **kwargs)
        cache_value[key] = result
        return result

    wrapper.cache = cache_value   # expose cache dictionary
    wrapper.clear_cache = lambda: cache_value.clear()  # manual clearing
    return wrapper
@cache
def long_function(a, b, delay=3):
    time.sleep(delay)
    return a + b

print(long_function(2, 3))            # slow
print(long_function(2, 3))            # fast (cached)
print(long_function(2, 3, delay=5))   # slow because different args
long_function.clear_cache()           # clear cache manually
