
vocales = ['a', 'e', 'i', 'o', 'u']

nombre_usuario = input("Ingrese su nombre: ")

count = 0
for item in nombre_usuario:
    if item in vocales:
        count += 1
    
if count >= 3:
    print("nombre tiene más de 3 vocales") 
else: 
    print("no tiene 3 vocales")