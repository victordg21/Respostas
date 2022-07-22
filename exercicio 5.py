x = input("Escreve uma palavra: ")

y = len(x) - 1
z = ""
while y >= 0:
    z = z + x[y]
    y = y - 1

x = z

print(x)
    

