def line():
    
    coefa = float(input("Ingrese coeficiente A: "))
    coefb = float(input("Ingrese coeficiente B: "))
    coefx1 = float(input("Ingrese coeficiente X1: "))
    coefx2 = float(input("Ingrese coeficiente X2: "))
    oper1 = (coefa*coefx1+coefb)
    oper2 = (coefa*coefx2+coefb)
    hip = (((oper2-oper1)**2 + (coefx2-coefx1)**2)**(0.5))
    print(f"El coeficiente A de su ecuación de la recta es: {coefa}")
    print(f"El coeficiente B de su ecuación de la recta es: {coefb}")
    print(f"El coeficiente X1 de su ecuación de la recta es: {coefx1}")
    print(f"El coeficiente X2 de su ecuación de la recta es: {coefx2}")
    print()
    print("Para la siguiente ecuación:")
    print (f"\tY = {coefa}X + {coefb}")
    print()
    print("Dados los siguientes puntos:")
    print(f"\tP1 ({coefx1}, {oper1})")
    print(f"\tP2 ({coefx2}, {oper2})")
    print("")
    print(f"La distancia entre ellos es: {hip}")


