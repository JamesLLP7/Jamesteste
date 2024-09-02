

# Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

# nota = float(input("Insira uma nota 0 até 10: "))

# while (nota < 0) or (nota > 10):
#     nota = float(input("Não pode ser menor que 0 ou maior que 10 meu jovem!\n \
#     Tente novamente:"))
# print("Nota válida")
    
    
# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
# nome = input("Digite o seu nome: ")
# senha = input("Digite a sua senha: ")
# while  senha == nome:
#     senha = input("Digite a sua senha novamente: ")
    
#     if senha != nome:
#         break

    
# print("Valor valido") 


# Faça um programa que leia 5 números e informe a soma e a média dos números.
# soma = 0
# for numeros in range(5):
#     numero = float(input("Digite um numero: "))
#     soma += numero
# media = soma / numero
# print (media)

# Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.
# for numero in range (1,51):
#     if numero % 2 == 1:
#         print(numero)

# Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:
# numero = int(input("Qual numero da tabuada voce desja ver: "))
# for x in range(numero):
#     for y in range(1,11):
#         multiplicaçao = numero * y
#         print(f"{numero} X {y} = {multiplicaçao}")
#     break    

# Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. Depois modifique o programa para que ele mostre os números um ao lado do outro.
       
# for i in range(1, 21):
#     print(i)

# print(list(range(1, 21)))

# Faça um programa que leia 5 números e informe o maior número.

# n1 = float(input("Número 1: "))
# n2 = float(input("Número 2: "))
# n3 = float(input("Número 3: "))
# n4 = float(input("Número 4: "))
# n5 = float(input("Número 5: "))
# maior = max(n1,n2,n3,n4,n5)
# print(f"O maior numero é: {maior}")

# Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1.
# # numero = int(input("Digite um numero inteiro: "))
# # while numero % 2 == 0:
# #     print("Numero nao primo")
# #     numero = int(input("Digite um numero inteiro: "))
# # print("Numero primo")

# ou
    
# while True:
#     numero = int(input("Digite um numero inteiro: "))
#     if numero % 2 == 1:
#         print("Numero primo")
#         break
#     else:
#         print("Numero nao primo")
#         numero = int(input("Digite um numero inteiro novamente: "))
 
 
# crie um algoritmo que solicite ao usuário que crie uma senha. Em seguida, use um loop para pedir que o usuário confirme a senha. O loop deve continuar até que a senha de confirmação seja igual à senha original. Quando isso acontecer, exiba uma mensagem de confirmação.
       
# senha = input("Crie uma senha: ")   
# while True:
#     confirme_senha = input("Confirme a senha novamente: ")
    
#     if senha == confirme_senha:
#         print (f"Senha Correta!")
#         break
#     else:
#         senha = input("Crie uma senha: ")
       
# Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';

# nome = input("Digite o seu nome: ")
# while len(nome) > 3:
#     print("Infomraçao valida")
#     break
# else: 
#     print("Informaçao invalida")
# idade = int(input("Digite a sua idade: "))
# while idade <= 150:
#     print("Infomraçao valida")
#     break
# else: 
#     print("Informaçao invalida")
    
# salario = float(input("Digite o seu salario: "))
# while salario > 0:
#     print("Infomraçao valida")
#     break
# else: 
#     print("Informaçao invalida")

# sexo = input("Digite o seu sexo (f ou m): ")
# if sexo == "f":
#     print("Infomraçao valida")
# else:
#     print("Informaçao invalida")

# estado_civil = input("Digite o seu estado civil (s, c, v, d): ")
# if estado_civil == "s":
#     print("Infomraçao valida")
    
# elif estado_civil == "c":
#     print("Infomraçao valida")
    
# elif estado_civil == "v":
#     print("Infomraçao valida")
    
# elif estado_civil == "d":
#     print("Infomraçao valida")
    
# else:
#     print("Informaçao invalida")
    
    
# Criação de uma calculadora basica  

# operador = input("Digite o operador (*, +, -, /): ")
# num1 = float(input("Digite um numero: "))
# num2 = float(input("Digite um numero: "))

# if operador == "*":
#     print(num1 * num2)
# if operador == "+":
#     print(num1 + num2)
# if operador == "-":
#     print(num1 - num2)
# if operador == "/":
#     print(num1 / num2)
