#testes para vaga de estágio 

# 1º - RESPOSTA: 
def fibonacci_sequence(n):
    fib_sequence = [0, 1]
    while fib_sequence[-1] < n:
        next_value = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_value)
    return fib_sequence

def is_in_fibonacci(n):
    fib_sequence = fibonacci_sequence(n)
    if n in fib_sequence:
        return f"O número {n} pertence à sequência de Fibonacci."
    else:
        return f"O número {n} não pertence à sequência de Fibonacci."

numero = int(input("Informe um número: "))
resultado = is_in_fibonacci(numero)
print(resultado)


# A função fibonacci_sequence(n) gera a sequência de Fibonacci até que o último numero seja maior ou igual a n,
# A função is_in_fibonacci(n) verifica se o número informado está na sequência gerada.
# O programa principal pede ao usuário um número, chama a função de verificação e imprime o resultado.


# 2º - RESPOSTA 
def verificar_letra_a(string):
    contador = 0
    
  
    for caractere in string:
        if caractere.lower() == 'a':
            contador += 1
    
    if contador > 0:
        return f"A letra 'a' aparece {contador} vezes na string."
    else:
        return "A letra 'a' não está presente na string."

string = input("Digite uma string: ")
resultado = verificar_letra_a(string)
print(resultado)

# Esse codigo primeiro Inicializa um contador para contar as ocorrências da letra ‘a’.
# conta sobre cada caractere da string, verificando se é ‘a’ ou ‘A’ (usando caractere.lower() para tratar nos dois cenarios).
# Incrementa o contador sempre que encontra a letra ‘a’.
# Retorna uma mensagem informando quantas vezes a letra ‘a’ aparece ou se ela não está no codigo.


# 3 - RESPOSTA 

77

# 4 - RESPOSTA

9 , 128, 49, 100, 13, 27
