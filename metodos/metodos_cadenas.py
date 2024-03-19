cadena1='Hola soy yo'
cadena2='Bienvenido máquina'

resultado=cadena1.upper()
#upper convierte a mayusculas
#lower convierte en minusculoas
#capitalize convierte primera letra en mayuscula
#find buscar una cadena en otra cadena, devuelve el lugar que ocupa el texto
buscar=cadena1.find('Hola')
#index es igual una busqueda de una cadena dentro de otra, pero si no encuentra concidencia lanza excepción
#isnumeric, indica si el valor es un número o no con true y false
#isalpha, si es alfanumérico arroja true
#count, nos dice cuantas veces existe una coincidencia
#len, cuenta la cantidad de caracteres que tiene una cadena es una función
contar_caracteres=len(cadena1)
#startswith, verifica si la cadena empieza con otra cadena dada
#endswith, verifica si la cadena termina con otra cadena dada
#replace, reemplaza un valor por otro
reemplaza=cadena2.replace('a','tosh')
#
print(resultado)
print(reemplaza)
