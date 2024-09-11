'''
#1) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores
#(exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número,
#ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

def pertence_fibonacci(n):
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    if b == n or a == n:
        return f"O número {n} pertence à sequência de Fibonacci."
    else:
        return f"O número {n} não pertence à sequência de Fibonacci."


numero = int(input("Digite um número para verificar se pertence à sequência de Fibonacci: "))
print(pertence_fibonacci(numero))
-----------------------------------------------------------------------------------------------------------------------------
#2) Escreva um programa que verifique, em uma string, a existência da letra ‘a’,
#seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre.

def contar_a(string):
    c = string.lower().count('a')
    if c > 0:
        return f"A letra 'a' aparece {c} vezes na string."
    else:
        return "A letra 'a' não aparece na string."


string = input("Digite uma frase: ")
print(contar_a(string))
-----------------------------------------------------------------------------------------------------------------------------


#3) Observe o trecho de código abaixo: int INDICE = 12, SOMA = 0, K = 1;
# enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; } imprimir(SOMA);

def calcular_soma():
    INDICE = 12
    SOMA = 0
    K = 1
    while K < INDICE:
        K = K + 1
        SOMA = SOMA + K
    return SOMA


print("O valor de soma será:", calcular_soma())
-----------------------------------------------------------------------------------------------------------------------------

#4) Descubra a lógica e complete o próximo elemento:

def completar_sequencias():
    sequencia_a = [1, 3, 5, 7]
    sequencia_a.append(sequencia_a[-1] + 2)

    sequencia_b = [2, 4, 8, 16, 32, 64]
    sequencia_b.append(sequencia_b[-1] * 2)

    sequencia_c = [0, 1, 4, 9, 16, 25, 36]
    sequencia_c.append((len(sequencia_c)) ** 2)

    sequencia_d = [4, 16, 36, 64]
    sequencia_d.append((len(sequencia_d) * 2) ** 2)

    sequencia_e = [1, 1, 2, 3, 5, 8]
    sequencia_e.append(sequencia_e[-1] + sequencia_e[-2])

    sequencia_f = [2, 10, 12, 16, 17, 18, 19]
    sequencia_f.append(sequencia_f[-1] + 1)

    return {
        "a)": sequencia_a,
        "b)": sequencia_b,
        "c)": sequencia_c,
        "d)": sequencia_d,
        "e)": sequencia_e,
        "f)": sequencia_f
    }


resultado = completar_sequencias()
for chave, sequencia in resultado.items():
    print(f"{chave} {sequencia}")
-----------------------------------------------------------------------------------------------------------------------------

#5) Você está em uma sala com três interruptores, cada um conectado a uma lâmpada em salas diferentes.
# Você não pode ver as lâmpadas da sala em que está, mas pode ligar e desligar os interruptores quantas vezes quiser.
# Seu objetivo é descobrir qual interruptor controla qual lâmpada. Como você faria para descobrir, usando apenas duas idas
# até uma das salas das lâmpadas, qual interruptor controla cada lâmpada?


def descobrir_interruptores():
    lampadas = {
        "Lampada 1": {"estado": "desligada", "temperatura": "fria"},
        "Lampada 2": {"estado": "desligada", "temperatura": "fria"},
        "Lampada 3": {"estado": "desligada", "temperatura": "fria"}
    }

    lampadas["Lampada 1"]["estado"] = "ligada"
    lampadas["Lampada 1"]["temperatura"] = "quente"

    lampadas["Lampada 1"]["estado"] = "desligada"
    lampadas["Lampada 2"]["estado"] = "ligada"

    print("Visitando a sala das lâmpadas...")
    for lampada, propriedades in lampadas.items():
        if propriedades["estado"] == "ligada":
            print(f"{lampada} está acesa - Controlada pelo segundo interruptor")
        elif propriedades["estado"] == "desligada" and propriedades["temperatura"] == "quente":
            print(f"{lampada} está desligada, mas está quente - Controlada pelo primeiro interruptor")
        else:
            print(f"{lampada} está desligada e fria - Controlada pelo terceiro interruptor")


descobrir_interruptores()
'''




