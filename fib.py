#!/usr/bin/python
def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input("Number? : "))

for i in range(1, n + 1):
    fib = fibonacci(i)
print(fib)



