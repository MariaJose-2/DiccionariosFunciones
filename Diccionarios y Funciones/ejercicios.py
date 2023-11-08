print("                                 Ejercicios Funciones                               ")
#Escriba una función en Python que reproduzca lo siguiente:
#𝑓(𝑥, 𝑦) = 𝑥2 + 𝑦2 Valor para X=3 y valor para Y=5
#se define la funcion calcular que toma dos argumentos (x, y)
def calcular(x, y):
    return x**2 + y**2 #realiza el calculo del resultado y devuelve el valor calculado
x = 3
y = 5
#llama la funcion con los valores de x,y como argumentos
resultado = calcular(x, y)

print(f'El resultado entre x:{x}, y:{y} es {resultado}')

print("------------------------------------------------")

#Tomé el presente ejercicio, y pasé a la función la lista con los días de la semana restantes

#se define la funcion lista y toma dos argumentos: arg(un valor a agregar a la lista) y resultado(una lista que se pasara a la funcion, con un valor por defecto de None)
def lista(arg, resultado=None):
    if resultado is None: #verifica que la variable sea none
        resultado = []
    resultado.append(arg) #se agrega el valor de arg a la lista resultado
    return resultado

#lista con los dias de la semana
diasSemana = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]

#se crea la lista vacia que se utilizara para almacenar el resultado de la funcion
respuesta = []

#se inicia un bucle for que recorre la lista diasSemana y toma cada dia de la semana uno por uno
for dias in diasSemana:
    resultado = lista(dias, respuesta)

#despues de completar el bucle, se imprime la lista respuesta, que ahora contiene todos los dias de la semana 
print("Dias de la semana:", respuesta)