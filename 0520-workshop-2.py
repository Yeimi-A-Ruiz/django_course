# exercise 1

municipios = {
    'bucaramanga': 581,
    'floridablanca': 267,
    'giron': 260,
    'piedecuesta': 163,
}

poblacion = sum(municipios.values())

print('')
print('*'*10)
print('Exercise 1')
print('*'*10)
print('')
print('diccionario')
print('')
for key, value in municipios.items():
    print(key, value)
print('')
print('funcion sumatoria')
print('')
print(f'En total en el AMB hay una población de {poblacion} miles de personas')

pop = 0
for values in municipios.values():
    pop = pop + values

print('')
print('ciclo for')
print('')
print(f'En total en el AMB hay una población de {pop} miles de personas')

# exercise 2

print('')
print('*'*10)
print('Exercise 2')
print('*'*10)
print('')

hijos_jose = 3
mascotas_hijo = 2

mascotas_hogar = hijos_jose * mascotas_hijo
print(f'Jose tiene {hijos_jose} hijos')
print(f'Cada hijo tiene {mascotas_hijo} mascotas')
print('')
print(f'Jose en su hogar tiene {mascotas_hogar} mascotas en total')

# exercise 3

print('')
print('*'*10)
print('Exercise 3')
print('*'*10)
print('')

def prom_mascota(n):
    resultado = (n/10)*3
    print(f'En total en el AMB se estima un total de {int(resultado)} mascotas')

prom_mascota(pop)

# challenge

print('')
print('*'*10)
print('Challenge')
print('*'*10)
print('')

def incremento_anual(n):
    solve = n*(1.03)
    total_proyectado = solve + poblacion
    print('')
    print(f'La población total proyectada para {proyectado} años, es de {total_proyectado} miles de personas')
  
print('')
print(f'En total en el AMB hay una población de {poblacion} miles de personas')
print('')
proyectado = int(input('Ingrese el numero de años que desea proyectar: '))

incremento_anual(proyectado)