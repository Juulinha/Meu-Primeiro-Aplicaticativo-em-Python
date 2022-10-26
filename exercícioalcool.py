alcool = float(input("Digite o valor da alcool: "))
gasolina = float(input("Digite o valor da gasolina: "))
formula = alcool/gasolina

print("Resultado do calculo: ",formula)
if formula <= 0.70:
    print("COMPENSA ALCOOL")
else:
    print("COMPENSA GASOLINA")