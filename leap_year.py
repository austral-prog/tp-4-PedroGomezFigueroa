def leap_year():
    ano = int(input("Ingrese un año:"))
    cuatro = ((float(ano/4))-(int(ano/4)))
    cien = ((float(ano/100))-(int(ano/100)))
    cuatrociento = ((float(ano/400))-(int(ano/400)))

    if (cuatrociento==0):
        print(f"El año {ano} es bisiesto")
    elif(cien > 0) and (cuatro==0):
        print(f"El año {ano} es bisiesto")
    else:
        print(f"El año {ano} no es bisiesto")




