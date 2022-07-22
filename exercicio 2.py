y = int(input("Digite um número para saber se ele está na Sequência de Fibonacci: "))

x = 0
lista = [0]
while y > x:
  if x == 0 or x == 1:
    x = x + 1
    lista.append(x)
  else:
    z = lista[len(lista) - 2]
    x = x + z
    lista.append(x)

if y == x:
  print("Ele pertence a sequência de Fibonacci")
else:
  print("Ele não pertence a sequência de Fibonacci")  
    

  

