repeticiones = int(input("Digita la cantidad de veces que deseas iterar"))

while repeticiones <=5:
    variable = input("Pon el mensaje a destacar: ")
    variable_numerica = int(input("Escribe un numero: "))

    if variable == variable_numerica:
        result= variable + variable_numerica
        print('no es igual')
    else:
        print("son diferentes")
        
    