#Aqui fiz um sistema de calculadora, em que vc escolhe qual calculo deseja fazer
# e depois insere os numeros, e no fim mostra o resultado.

calc = input("Selecione o calculo que deseja:\
 1-Adição\
 2-Subtração\
 3-Multiplicação\
 4-Divisão")


num1 = input("Digite um numero: ")
num2 = input("Digite outro numero: ")

adc = int(num1) + int(num2)
sub = int(num1) - int(num2)
mult = int(num1) * int(num2)
div = int(num1) / int(num2)

if calc == "1":
    resultado = adc
    adc = resultado
if  calc == "2":
    resultado = sub
    sub = resultado
if calc == "3":
    resultado = mult
    mult = resultado
if calc == "4":
    resultado = div
    div = resultado

print(resultado)
