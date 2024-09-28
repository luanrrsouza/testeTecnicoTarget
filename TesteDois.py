def fibonacci(n):
    fib_sequence = [0, 1]
    
    while fib_sequence[-1] < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    
    return fib_sequence

def pertence_fibonacci(n):
    if n in fibonacci(n):
        return f"O número {n} pertence à sequência de Fibonacci."
    return f"O número {n} não pertence à sequência de Fibonacci."


numero = int(input("Informe um número: "))
print(pertence_fibonacci(numero))
