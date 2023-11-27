def bin2dec(binario):
    dec = int(str(binario), 2)
    return dec

def dec2bin(decimal):
    bina = bin(decimal)
    return bina[2:]

def errorOperacion():
    regresar = input("¿Quiere realizar una nueva operación [S/N]? ")
    return regresar

# Main program
dec = 0
numerobinario = 0
numerodecimal = 0

opc = int(input("Seleccione una opción (1: Decimal a binario, 2: Binario a decimal): "))

if opc == 1:
    numero = int(input("Dame un número entero: "))
    numerodecimal = dec2bin(numero)
    numerobinario = bin2dec(numerodecimal)
    print("Número binario: {}".format(numerodecimal))
    print("Número decimal: {}".format(numerobinario))

    nuevaOperacion = errorOperacion()
    while nuevaOperacion.upper() == "S":
        numero = int(input("Dame un número entero: "))
        numerodecimal = dec2bin(numero)
        numerobinario = bin2dec(numerodecimal)
        print("Número binario: {}".format(numerodecimal))
        print("Número decimal: {}".format(numerobinario))
        nuevaOperacion = errorOperacion()

    print("Adiós")

elif opc == 2:
    # Add logic for Binario a Decimal
    pass

else:
    print("Opción no válida")
