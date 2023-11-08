print("                     Diccionarios y funciones en python                   ")
print("--------------------------------------------------------------------------")
#declaracion de un diccionario vacio usando la funcion dict() 
print("Declaracion de un diccionario")
diccionario = dict()

#diccionario inicializado con llaves
diccionario= {}

#Diccionario inicializado con valores iniciales: clave-valor
Diccionario = {'nombre':'Sandra' , 'edad': 44}

print("---------------Accediendo a los elementos de un diccionario---------------")

#accede al valor con la clave "nombre" en el diccionario
print(Diccionario ['nombre'])

#accede al valor con la clave "nombre" utilizando el metodo .get() y si la clave no existe imprime que el "nombre no existe".
print(Diccionario.get('nombre','No existe'))

print("--------------------------tecnicas de iteracion---------------------------")

#se crea un diccionario llamado calificaciones con una clave "nombre" y un valor "notafinal" 
calificaciones = {
 'nombre': 'Sandra',
 'notafinal': 5.0
 }

#actualiza el diccionario con un nuevo conjunto de claves y valores
calificaciones = {
 'Sandra': 5.0,
 'Adriana':5.0,
 'Mauricio':4.5,
 'Jose':2.5
 }

#itera a traves del diccionario y se utiliza .items para que imprima las claves y los valores del diccionario
for i, j in calificaciones.items(): 
 print(i,j)

print("--------------Agregar datos al diccionario después de creado--------------")

#actualiza el diccionario agregando un nuevo elemento que sera Rosa y German
calificaciones.update({"Rosa": 3.7, "German": 4.8})

print("-------------------tecnicas de iterar los diccionarios--------------------")

print("Técnicas por clave")
#itera a traves del diccionario utilizando .keys() para que solo imprima las claves
for i in calificaciones.keys():
 print(i)
 
print("--------------------------------")

print("Iterar por valor")
#itera a traves del diccionario utilizando .values() para que solo imprima los valores
for j in calificaciones.values():
 print(j)

print("--------------------------------")

#crea dos listas una de nombres y la otra de edades
nombres = ['Maria', 'Sebastian', 'Ana']
edades = ['18', '25', '30']

# Itera a través de las listas nombres y edades utilizando zip que sirve para unir dos listas y las imprime juntas.
for n, e in zip(nombres, edades):
#el cero y el uno son las posiciones de los elementos de la lista
 print('Tú nombre es {0} y tu edad {1}.'.format(n, e))
 
print("-------------------operaciones sobre los diccionarios---------------------")

#crea un nuevo diccionario utilizando una comprensión y lo que va hacer es elevar el 2, 4 y el 6 al cuadrado
dicaleatorio={x: x**2 for x in (2, 4, 6)}
print(dicaleatorio)


print("------------------------Imprimir numeros en reversa-----------------------")

print("Números en reversa")
#va a imprimir numeros en orden inverso (reversa), en un rango especifico el cual es(1, 10, 2) para lograrlo se utiliza reversed.
for i in reversed(range(1, 10, 2)):
 print(i)
 
print("--------------------------------")

print("Borrar un elemento del diccionario")
#elimina el elemento con la clave Rosa del diccionario de calificaciones
del(calificaciones['Rosa'])
#itera a traves del diccionari e imprime las claves y los valores ya que utiliza el .items()
for i, j in calificaciones.items():
 print(i,j)