#inbilt python solution for LRU cache decorators
from functools import lru_cache
import time

@lru_cache(maxsize=None)   # unlimited cache size
def long_function(a, b):
    time.sleep(4)
    return a + b

print(long_function(2,3))
print(long_function(5,2))
print(long_function(2,3))  # instant
print(long_function(5,2))  # instant
