def validar_retirar(efectivo, saldo):
    if efectivo % 20 != 0 and efectivo % 50 != 0:
        raise ValueError("La cantidad debe ser divisible por 20 o 50.")

    if efectivo > saldo:
        raise Exception("No dispone de esa cantidad.")

    return efectivo
retirada_efectivo = False
contador = 0
while not retirada_efectivo or contador < 3:
    try:
        saldo_inicial = 1000
        efectivo_entrada = int(input("Indique la cantidad a retirar: "))
        print(efectivo_entrada)
        efectivo = validar_retirar(efectivo_entrada, saldo_inicial)
        saldo_inicial -= efectivo
        retirada_efectivo = True
    except ValueError as e:
        print(e)
        contador += 1
    except Exception as error:
        print(error)
        contador += 1
    else:
        print("Nuevo saldo:", saldo_inicial)
    finally:
        if contador > 2:
            retirada_efectivo = True

    finally:
        print("Gracias por usar nuestro cajero")