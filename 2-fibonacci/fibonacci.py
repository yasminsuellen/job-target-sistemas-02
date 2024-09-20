def fibonacci(n):
    # Inicializa os dois primeiros números da sequência de Fibonacci
    fib_seq = [0, 1]

    # Calcula a sequência até que o último valor seja maior ou igual ao número inserido
    while fib_seq[-1] < n:
        proximo_valor = fib_seq[-1] + fib_seq[-2]
        fib_seq.append(proximo_valor)

    # Verifica se o número digitado pertence à sequência
    if n in fib_seq:
        return f"O número {n} pertence à sequência de Fibonacci."
    else:
        return f"O número {n} não pertence à sequência de Fibonacci."


# Solicita entrada do usuário
numero = int(input("Insira um número: "))

# Exibe o resultado
print(fibonacci(numero))
