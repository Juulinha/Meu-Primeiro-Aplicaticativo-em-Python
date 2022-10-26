# coletando dados do usuario
nome = input("digite seu nome: ")
idade = int(input("digite sua idade: "))
altura = float(input("digite sua altura: "))
peso = float(input("digite sua peso: "))
imc = peso/altura**2

print("-" * 30)
print("Os Dados coletados foram:")
print("nome: ", nome)
print("idade: ", idade, " anos")
print("altura: ", altura)
print("peso: ", peso," quilos")
print("IMC: ", imc)

if imc < 16:
    print("Magreza Grave")
elif imc < 18.5:
    print("Magreza Leve")
elif imc < 24.9:
    print("Peso Normal")
elif imc < 29.9:
    print("Excesso de peso")
elif imc < 34.9:
    print("Obesidade classe 1")
elif imc < 39.9:
    print("Obesidade classe 2")
else: 
    print("Obesidade classe 3")