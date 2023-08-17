def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

n = 10  
print(f"El número de Fibonacci en la posición {n} es {fibonacci(n)}")
