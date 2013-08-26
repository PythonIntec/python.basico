#coding: utf-8
print "Saludos aprendiz, a continuación una variable"
variable = "Soy una variable"
print variable

print "Las variables pueden tener cualquier nombre"
aguacate = "Soy un aguacate"
print aguacate

print "Los nombres pueden tener cualquier longitud"
print "Cuando el nombre incluye más de un sustantivo, separar con _"
nombre_largo = "Tengo un nombre largo"
print nombre_largo
print "Pero no es conveniente que sean tan largos"
el_nombre_mas_largo_de_todos = "Yeah"
print el_nombre_mas_largo_de_todos

print "También pueden contener cualquier tipo de dato, nativo del lenguaje y creado por el usuario (se verá luego)"
entero = 21
decimal = 3.2
caracter = 'o'
cadena_caracteres = "Esto es interesante"
print entero, decimal, caracter, cadena_caracteres

print "No se pueden crear variables sin ningún valor, descomenta la siguiente línea y corre el script"
print "Resultará en un error del tipo NameError: name is not defined"
print "no_tengo_valor"

print "Al proceso de asignarle un valor a la variable se le llama asignación"
tengo_valor = 1
print tengo_valor

print "Las variables son muy codiciosas y aceptan cualquier valor que se le asigne"
tengo_valor = "otro valor"
print tengo_valor #Imprime "otro valor"
tengo_valor = 3.9 
print tengo_valor #Imprime "3.9"

print "Se pueden crear varias variables en una misma línea"
uno, dos, tres, cuatro = 1, 2, 3, 4
print uno, dos, tres, cuatro
