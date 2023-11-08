print("                                  Funciones                               ") 
print("--------------------------------------------------------------------------")
print("Definir una función")

#define una funcion saludar y la imprime
def saludar():
 print("saludo")
 
#define una funcion llamada retornarnumero que devuelve (retorna) 1.
def retornarnumero():
 return 1

#llama la funcion saludar e imprime saludo
saludar()

#llama la funcion retornarnumero pero no muestra su resultado
retornarnumero()

#comprueba si el resultado de la funcion retornarnumero es igual a 1, imprimira un mensaje "devolvio un uno" de lo contrario el mensaje sera "no devolvio un uno"
if retornarnumero()==1:
 print("devolvió un uno")
else:
 print("No devolvió un uno")
 

print("-----------------------funciones con parametros---------------------------")

#se define una función llamada raiz que toma un valor y devuelve su raiz cuadrada.
def raiz(value):
 return value ** (1/2)

#llama a la función raiz con el valor 4 e imprime el resultado del valor 4
print(f'La raiz cuadrada es: {raiz(4)}')

#define una funcion llamada validarsiexiste que va a verificar si un objeto es verdadero o falsso y en consecuencia muestra el mensaje
def validarsiexiste(obj):
 if obj:
    print(f"{obj} is True")
 else: 
     print(f"{obj} is False")

#llama la funcion con el valor de 1 y determina si es verdadero o falso segun el valor
validarsiexiste(1)


print("---------------funciones con parametros posicionales----------------------")

#define una funcion llamada compra con tres parametros: marca, cantidad y valor. Y devuelve un diccionario con la informacion sobre una compra
def compra(marca,cantidad,valor):
 return dict(
 marca=marca,
 cantidad=cantidad,
 valor=valor*cantidad
 )
#llama la funcion compra con valores especificos e imprime la imformacion de la compra
print(f' lo comprado fue:{compra("AMD",3,2500000)}')

print("---------------funciones con parametros nominales----------------------")

#define nuevamente la función compra con los mismos parametros, pero esta vez utilizando los nombres de los parametros y esto permite llamar a la función en cualquier orden ya que son nominales.
def compra(marca,cantidad,valor):
 return dict(
 marca=marca,
 cantidad=cantidad,
 valor=valor*cantidad
 )
#llama la funcion compra especificando los parametros por nombre
print(f' lo comprado fue:{compra(marca="AMD",cantidad=3,valor=2500000)}')

print("---------------parametros por defecto----------------------")

#define nuevamente la función compra, pero esta vez el parametro valor tiene un valor por defecto si no se proporciona un valor para 'valor', se usara el valor por defecto.
def compra(marca,cantidad,valor=2500000):
 return dict(
 marca=marca,
 cantidad=cantidad,
 valor=valor*cantidad
 )
#llama la función compra sin especificar el valor y usa el valor por defecto(2500000)
print(f' lo comprado fue:{compra("AMD",3)}')


print("---------------modificando parametros mutables----------------------")

#define una funcion llamada lista que toma un argumento y una lista como segundo argumento (por defecto, una lista vacía)y agrega el argumento a la lista y la imprime
def lista(arg, result=[]):
 result.append(arg)
 print(result)

#llama la funcion lista con la cadena "domingo" y una lista vacia
lista('domingo', [])

print("--------------------------------")

#define una funcion llamada 'listalimpia' que toma un argumento y una lista como segundo argumento (que por defecto es None) Si la lista es None, crea una nueva lista vacia y luego, agrega el argumento a la lista y la imprime
def listalimpia(arg, result=None):
 if result is None:result = []
 result.append(arg)
 print(result)

#llama la funcion con la cadena "a" y luego con la cadena "b" que es lo que imprimira
listalimpia("a")
listalimpia("b")


print("---------------funciones anonimas lambda----------------------")
#ejemplo 1
#define una funcion lambda llamada numero_palabras que cuenta las palabras en una cadena.
#len: cuenta el numero de elementos en la cadena
#t.strip: Se elimina cualquier espacio en blanco al principio y al final de la cadena
#split: se utiliza para dividir una cadena en una lista de palabras (o elementos) utilizando un caracter especifico como separador.
numero_palabras = lambda t: len(t.strip().split())
numero_palabras = lambda t: len(t.strip().split())

#llama la funcion lambda con una cadena y muestra el numero de palabras
print(numero_palabras("hola, esto es una prueba con lambda"))

print("--------------------------------")

#ejemplo 2
#define una funcion lambda llamada operadorand que realiza una operacion de AND entre dos numeros, luego itera a traves de dos bucles para aplicar la funcion lambda e imprime los resultados
operadorand = lambda x, y: x & y
for j in range(2): #El bucle se ejecutara con j tomando los valores 0 y 1.
   for i in range(2): #dentro del bucle anterior, se inicia otro bucle for y este bucle tambien se ejecutara dos veces, con i tomando los valores 0 y 1.
      print(f"{i} & {j} = {operadorand(i, j)}")
#la operación AND devuelve 1 (verdadero) solo cuando ambos i y j son iguales a 1. 