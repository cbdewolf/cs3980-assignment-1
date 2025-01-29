# fib.py
import time
from functools import lru_cache
import matplotlib as plt


@lru_cache
@timer
def fib(n: int) -> int:
    if n == 0:
        return n
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)
