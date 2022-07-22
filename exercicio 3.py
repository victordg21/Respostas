lista = [1, 22174.1664, 2, 24537.6698, 3, 26139.6134, 4, 0.0, 5, 0.0,
       6, 26742.6612, 7, 0.0, 8, 42889.2258, 9, 46251.174, 10, 11191.4722,
       11, 0.0, 12, 0.0, 13, 3847.4823, 14, 373.7838, 15, 2659.7563,
       16, 48924.2448, 17, 18419.2614, 18, 0.0, 19, 0.0,
       20, 35240.1826, 21, 43829.1667, 22, 18235.6852, 23, 4355.0662,
       24, 13327.1025, 25, 0.0, 26, 0.0, 27, 25681.8318,
       28, 1718.1221, 29, 13220.495, 30, 8414.61]


def menor_faturamento(lista):
    n = 1
    z = lista[1]
    x = len(lista) - 1
    while n <= x:
        if lista[n] != 0:
            if lista[n] < z:
                z = lista[n]
                k = lista[n - 1]
                n = n + 2
            else:
                n = n + 2
        else:
            n = n + 2

    print("O menor faturamento foi no dia", k, " e faturou R$", z)

def maior_faturamento(lista):
    n = 1
    z = lista[1]
    x = len(lista) - 1
    while n <= x:
            if lista[n] > z:
                z = lista[n]
                k = lista[n - 1]
                n = n + 2
            else:
                n = n + 2

    print("O maior faturamento foi no dia", k, " e faturou R$", z)

def media_faturamento(lista):
    n = 1
    z = lista[1]
    x = len(lista) - 1
    soma = 0
    d = 0

    while n <= x:
        soma = soma + lista[n]
        if lista[n] != 0:
            d = d + 1
        n = n + 2
    media = soma / d
    n = 1
    d = 0
    while n <= x:
        if lista[n] > media:
            d = d + 1

        n = n + 2

    print("O faturamento foi maior que a média em", d, "dias")
            




menor_faturamento(lista)
maior_faturamento(lista)
media_faturamento(lista)


    

    


	
    
