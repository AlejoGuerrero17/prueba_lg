input('Ingrese lista de números separados por coma: ')
numbers = numbers.replace(" ","")
if len(my_numbers) >0:
      pares = []
  else:
        pares = [numero for numero in my_numbers if float(numero) %2 == 0]
print (f'Lista de número pares {pares}')

