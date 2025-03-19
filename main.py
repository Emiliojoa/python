print("hola mundo")

#declaraciones
mi_variable = "hola variable"
print(mi_variable)
mi_variable=3
print(mi_variable)
#declaracion de constantes
MI_PRIMERA_CONSTNTE ="Hola soy una constante"

print(MI_PRIMERA_CONSTNTE)

MI_PRIMERA_CONSTNTE = 3.212
print(MI_PRIMERA_CONSTNTE)

#tipos de datos 

#integer
mi_int=3
print(type(mi_int))
#float
mi_float=3.2
print(type(mi_float))

#string
mi_string= f"hola {mi_int}"
print(mi_string)

#boolean
True
False

#none
undefined=None
print(undefined)

#list
mi_list=[1,"funciono",3,4,5,["otra lista adentro", "numero 2",3]] #la lista tiene corchetes
print(mi_list)

mi_list.append("me agregue algo")
print(mi_list)

#dict 
mi_dict={"nombre": "Emilio", "edad": 19, "status": "Capo"} #el diccionario tiene llaves
print(mi_dict["nombre"])

#tupla
mi_tupla=(1,2,3) #la tupla tiene parentesis
print(mi_tupla)

mi_tupla=(1,4,3)
print(mi_tupla)

#operaciones
mi_suma=3+3
print(mi_suma)

mi_resta=3-3
print(mi_resta)

mi_multiplicacion=3*3
print(mi_multiplicacion)

mi_division=3/3
print(mi_division)

mi_modulo=3%3
print(mi_modulo)

mi_potencia=3**3
print(mi_potencia)

mi_division_entera=3//7
print(mi_division_entera) #devuelve la parte entera de la division

#condicionales
condicion=True

if condicion:
    pass #sirve para que no de error y sirva el codigo
elif condicion:
    pass

#operadores logicos 
if condicion and condicion:
    print("es verdadero")
elif condicion or condicion:
    print("es falso")
elif not condicion:
    print("es falso")

##estructuras de control
#for
for i in range(0, 11, 5): #range(inicio, fin, paso)
    print(i)


##while



#algo que hizo Marce
nombres = ["Emilio", "Marcelo", "Juan", "Pedro", "Pablo"]
edades=[19, 20, 21, 22, 23]



for nombres, edades in zip(nombres, edades):
    print(f"{nombres} tiene {edades} años de edad")