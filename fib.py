# fib.py
import time
from functools import lru_cache
import matplotlib.pyplot as plt


def timer(func):
    def wrapper(*args, **kwargs):
        startTime = time.time()
        result = func(*args, **kwargs)
        endTime = time.time()
        print(
            f"Finished in {endTime - startTime}s: {func.__name__}({args[0]}) = {result}"
        )
        return result

    return wrapper


@lru_cache
@timer
def fib(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)


def fibTime(n: int) -> float:
    startTime = time.time()
    fib(n)
    endTime = time.time()
    return endTime - startTime


def plot_fib(n: int) -> None:
    x = list(range(n))
    y = [fibTime(i) for i in x]
    plt.plot(x, y)
    plt.show()


if __name__ == "__main__":
    fib(100)
    plot_fib(100)
