lista = ["SP", 67836.43, "RJ", 36678.66, "MG", 29229.88, "ES", 27165.48, "outros", 19849.53]

soma = lista[1] + lista[3] + lista[5] + lista[7] + lista[9]
n = 0

while len(lista) > n:
    porcentagem = 100 * lista[n + 1] / soma
    print("O percentual de", lista[n], "foi de", porcentagem,"%")
    n = n + 2

