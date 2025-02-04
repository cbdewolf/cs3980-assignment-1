# fib.py
import time
from functools import lru_cache
import matplotlib.pyplot as plt

fibTimes = []


def timer(func):
    def wrapper(*args, **kwargs):
        startTime = time.perf_counter()
        result = func(*args, **kwargs)
        endTime = time.perf_counter()
        timePassed = endTime - startTime
        fibTimes.append(timePassed)
        print(f"Finished in {timePassed:.8f}s: {func.__name__}({args[0]}) -> {result}")
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


def plotFib(n: int) -> None:
    plt.grid(axis="y", linestyle="-")
    plt.xticks([i for i in range(0, n + 1, 10)])
    plt.xlim(0, n)
    plt.ylim(0, max(fibTimes))
    x = list(range(n + 1))
    y = fibTimes
    plt.plot(x, y)
    plt.show()


if __name__ == "__main__":
    fib(100)
    plotFib(100)
