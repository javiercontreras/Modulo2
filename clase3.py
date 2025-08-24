"""
a = (lambda b:b**2)(2)
print(a)

z = (lambda x,y:x**y)(2,3)

print(z)
"""
"""
r = (lambda x,y:"x es mayor" if (x>y) else "x es menor que y")(4,5)
print(r)
"""
# B1E1.Valor Absoluto
#  Escriba una función lambda que reciba un número y retorne su valor absoluto.
# • Recuerde que el valor absoluto realiza lo siguiente: si el número es positivo o cero,
# devuelve el mismo número; si el número es negativo, devuelve el mismo número
# pero como valor positivo.

"""
v = float(input("Ingrese un numero, se retornara el valor absoluto : "))
r =(lambda x: x*-1 if(x<0) else x)(v)
print(r)
"""
#  B1E2 Escriba nuevamente la función de distancia euclidiana.
# • Transforme la función a una función anónima (lambda).
# • Su programa debe recibir las coordenadas por la entrada estándar y luego llamar a
# la función anónima.
# • La función anónima debe retornar la distancia euclidiana (presente el resultado
# por la salida estándar)
"""
px1 = float(input("Ingrese la cordenada x del punto 1 :"))
py1 = float(input("Ingrese la cordenada y del punto 1 :"))
px2 = float(input("Ingrese la cordenada x del punto 2 :"))
py2 = float(input("Ingrese la cordenada y del punto 2 :"))

d_euclidiana =(lambda x1,y1,x2,y2:((x2-x1)**2+(y2-y1)**2)**(0.5) )(px1,py1,px2,py2)
print(d_euclidiana)
"""

# B1E3 Escriba una función lambda que retorne el dígito verificador de un RUT.
# • La lambda debe recibir como parámetro un RUT sin dígito verificador y retornar
# este último.
# • Revise el algoritmo para dígito verificador en:
# https://es.wikipedia.org/wiki/Rol_%C3%9Anico_Tributario (sección “Procedimiento
# para obtener el dígito verificador

#Ingresa el rut sin digito verificador
rut = str(input("Ingrese rut sin puntos y sin digito verificador : "))
len_rut = len(rut)
list_chr_rut = list(rut)
sn = [2,3,4,5,6,7]
sum = 0
flag = True
while (flag):
    for i in range(len(sn)):  
        if (len(list_chr_rut) > 0):
            x = int(list_chr_rut.pop()) * sn[i]
            sum = sum + x
        else:
            flag = False
print(sum)
# #Individualizas los numeros del rut
mod11_rest = 10#-(sum%11)
digito = mod11_rest
if mod11_rest == 11 or mod11_rest == 10:
    digito = (lambda x: 0 if mod11_rest == 10 else "K")(digito)

print(digito)


#aplicar multiplicado algoritmo modulo11 y realizar suma
#Extraer digito verificador
#Entregar digito verificador si resultado es 11 se retorna un cero si es 10 una K