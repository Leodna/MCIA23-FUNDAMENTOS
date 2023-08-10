import math
#Ejercicio 1
payaso = 112
muneca = 75

cantidad_p = int(input('Cuantos payasos pidieron: '))
cantidad_m = int(input('Cuantas munecas pidieron: '))

peso_paquete = (cantidad_p*payaso) + (cantidad_m*muneca)
print ('El paquete pesara {} g'.format(peso_paquete))


#Ejercicio 2
dominio = '@alumnos.uaq.mx'
correo = input('Ingrese su correo: ')
while '@' not in correo:
    print ('Correo no valido')
    correo =input('Ingrese un correo valido: ')

c = correo.split('@')
print ('Su nuevo correo sera: {}'.format(c[0]+dominio))

#Ejercicio 3
renta_actual = float(input('Cuanto paga actualmente de renta'))
if renta_actual < 10000:
    print ('Le corresponde un impositivo de 5%')
elif renta_actual >= 10000 and renta_actual < 20000:
    print ('Le corresponde un impositivo de 15%')
elif renta_actual >= 20000 and renta_actual < 35000:
    print ('Le corresponde un impositivo de 20%')
elif renta_actual >= 35000 and renta_actual < 60000:
    print ('Le corresponde un impositivo de 30%')
else:
    print ('Le corresponde un impositivo de 45%')

#Ejercicio 4
contrasena = '123'

while True:
    _contrasena = input('Introduzca la contrsena: ')
    if contrasena == _contrasena:
        print('Contrsena correcta !!!!')
        break
    else:
        print('Contrasena Incorrecta xxxxxx')

#Ejercicio 5
abc = 'abcdefghiklmnñopqrstuvxyz'
labc = list(abc) 
for x in range(len(labc)):
    if x%3 == 0:
        print (labc[x])

#Ejercicio 6
carrito = {}
while True:
    articulo = input('Agrege un articulo: ')
    precio =float( input ('Cual es el precio de {}: $'.format(articulo)) )
    carrito.update({articulo:precio})
    continuar = input('Si desea agregar mas articulos oprima y/s')[0]
    if not (continuar == 'y' or continuar == 's'):
        break
print('Lista de Compras')
total = 0.0
for articulo in carrito:
    print ('| {} | {} |'.format(articulo,carrito[articulo]))
    total += carrito[articulo]
print ('| Total | {} |'.format(total))

#Ejercicio 7
def estadistica (datos):
    media = sum(datos)/len(datos)
    varianza = 0.0
    for dato in datos:
        varianza += (dato-media)*(dato-media)
    varianza = varianza / len(datos)
    desviacion = math.sqrt(varianza)
    resultados = {
        'media': round(media,2),
        'varianza':round(varianza,2),
        'desviacion':round(desviacion,2)

    }    
    return resultados

a = [23,45,12,10,55,100,45]
print (estadistica(a))
#Ejercicio 8
frutas = {'Plátano':1.35, 'Manzana':0.8, 'Pera':0.85,'Naranja':0.70}
fruta = input("Ingrese una fruta")
if fruta not in (frutas):
    print ("{} no esta registrada".format(fruta))
else:    
    peso = float(input(('Cuantos kg quiere')))
    precio = round(frutas[fruta] * peso,2)
    print ('Por {} kg de {} son ${}'.format(peso,fruta,precio))

#Ejercicio 9
precios = [50,75,46,22,80,65,8]
print ('El precio más alto es {} y el más bajo es {}'.format(max(precios),min(precios)))

#Ejercicio 10
asignaturas = ['matematicas','fisica','quimica','historia','lenguas']
notas = {}
for asignatura in asignaturas :
    nota = float(input('Cual es su calificacion en {}'.format(asignatura)))
    notas.update({asignatura:nota})
print ('Tus notas son las siguientes: ')
for nota in notas:
    print ('En {} has sacado {}'.format(nota,notas[nota]))

#Ejercicio 11
def mcd (a, b):
    temporal = 0
    while b != 0:        
        temporal = b
        b = a % b
        a = temporal
    return a

def mcm (x,y):
    n = 1
    while  not  (n%x== 0 and n%y ==0):                           
        n += 1
    return n
print ('El mcm {}'.format(mcm(6,21)))
print ('El mcd {}'.format(mcd(12,24)))