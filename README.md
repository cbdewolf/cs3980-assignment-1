# cs3980-assignment-1
The first assignment for CS:3980 contains two parts: a simple python scipt imitading that of an echo from a mountain, and an implementation of the fibonacci sequence to highlight the use of decorators in Python.

<ins> **echo.py** </ins> 

In echo.py, you will find a method named echo(), which takes a user inputted string, as well as a fixed number of repititions. The echo() method takes the text and repeats it the specified number of times, and imitates that of an echo effect in real life.
The example outputs provided are 

   Yell something at a mountain: Helloooo <br>
   ooo <br>
   oo <br>
   o <br>
   . <br>
and <br>
   Yell something at a mountain: echo 123 <br>
   123 <br>
   23 <br>
   3 <br>
   . <br>

<ins> **fib.py** </ins>

In fib.py, you will find a method fib() which calculates the nth fibonacci value in the sequence. The fib() method has two decorators associated with it, first of which is **@lru_cache**, which is imported from the Python package "functools." This decorator optimizes the execution time of fib(). The second decorator is **@timer**, an implemented decorator inside of fib.py. The purpose of this decorator is to calculate the time it takes to solve fib() for a given n value. The time will be stored in a list "fibTimes" which will be used to plot the data later, and the time will be outputted to the console.

Lastly, there will be method plot_fib() to visualize the relationship between n, the nth number of the fibonacci sequence, and the time it took to calculate that value. The results of the graph are relatively similar, but vary slightly per execution. I have added 3 different outputs to demonstrate the relationship. We find that the rate between n and its time increases in a linear fashion, and we can expect that increasing n will take longer to complete the operation.

![assignment1plot1](https://github.com/user-attachments/assets/9642676c-bfe4-4519-b8b5-6079674765eb)

![assignment1plot2](https://github.com/user-attachments/assets/37bebb00-9f62-426f-862f-1e21922f648a)

![assignment1plot3](https://github.com/user-attachments/assets/d0f5498c-8093-4580-a4c4-a8d743ed2693)
