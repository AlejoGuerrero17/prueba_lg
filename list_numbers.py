#First program [Calculate numbers cousins from a list given]
input('Ingrese lista de números separados por coma: ')
numbers = numbers.replace(" ","")
if len(my_numbers) >0:
      pares = []
  else:
        pares = [numero for numero in my_numbers if float(numero) %2 == 0]
print (f'Lista de número pares {pares}')
#Second program [Calculate divisor from a given number]
numero = int(input('Ingrese un número para conocer sus divisores: '))
divisores = [divisor for divisor in range(1,numero+1) if numero % divisor == 0]
print(divisores)
