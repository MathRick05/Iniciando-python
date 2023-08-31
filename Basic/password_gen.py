#Esse é um gerador de senha aleatório, onde ele pede aonde você deseja usar
# a senha e quantos dígitos você quer na sua senha, e ele gera uma senha aleatória
# e segura, e salva em um arquivo txt, para que você possa ver suas senhas depois.
from random import choice
import string


print("Bem vindo ao gerador de senhas!")
escolha = input("deseja gerar uma senha nova(1) ou apenas olhar suas senhas(2)?")
escolha = int(escolha)
if (escolha == 1) :
    arquivo = open("senhas.txt", "a")
    nomeDaSenha = input("Aonde você deseja usar a senha?")
    tamanho_da_senha = int(input("Quantos dígitos você quer na sua senha? "))
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha_segura = ''
    for i in range(tamanho_da_senha):
        senha_segura += choice(caracteres)
    print("A senha (segura) gerada é: ",senha_segura)
    arquivo.write(nomeDaSenha + ": " + senha_segura + "\n")
    arquivo.close()
    escolha = 0

if (escolha == 2):
    arquivo = open("senhas.txt", "r")
    print(arquivo.read())
        