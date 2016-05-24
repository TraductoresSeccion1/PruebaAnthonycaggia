
import math
opc = 's'

while opc == 's':

 operacion = raw_input('Que desea realizar: 1. Calcular longitud. 2.Calcular raiz cuadrada ')
 if operacion == '1':
  palabra = raw_input('Ingrese una palabra: ')
  print 'La longitud es: '
  print  len(palabra)

 elif operacion == '2':

  num = input('Ingrese Numero: ')
  raiz = math.sqrt(num)
  print 'La raiz es: '
  print raiz

 opc = raw_input('Desea continuar: (S/N): ')