

# # Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

# # nota = float(input("Insira uma nota 0 até 10: "))

# # while (nota < 0) or (nota > 10):
# #     nota = float(input("Não pode ser menor que 0 ou maior que 10 meu jovem!\n \
# #     Tente novamente:"))
# # print("Nota válida")
    
    
# # Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
# # nome = input("Digite o seu nome: ")
# # senha = input("Digite a sua senha: ")
# # while  senha == nome:
# #     senha = input("Digite a sua senha novamente: ")
    
# #     if senha != nome:
# #         break

    
# # print("Valor valido") 


# # Faça um programa que leia 5 números e informe a soma e a média dos números.
# # soma = 0
# # for numeros in range(5):
# #     numero = float(input("Digite um numero: "))
# #     soma += numero
# # media = soma / numero
# # print (media)

# # Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.
# # for numero in range (1,51):
# #     if numero % 2 == 1:
# #         print(numero)

# # Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:
# # numero = int(input("Qual numero da tabuada voce desja ver: "))
# # for x in range(numero):
# #     for y in range(1,11):
# #         multiplicaçao = numero * y
# #         print(f"{numero} X {y} = {multiplicaçao}")
# #     break    

# # Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. Depois modifique o programa para que ele mostre os números um ao lado do outro.
       
# # for i in range(1, 21):
# #     print(i)

# # print(list(range(1, 21)))

# # Faça um programa que leia 5 números e informe o maior número.

# # n1 = float(input("Número 1: "))
# # n2 = float(input("Número 2: "))
# # n3 = float(input("Número 3: "))
# # n4 = float(input("Número 4: "))
# # n5 = float(input("Número 5: "))
# # maior = max(n1,n2,n3,n4,n5)
# # print(f"O maior numero é: {maior}")

# # Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1.
# # # numero = int(input("Digite um numero inteiro: "))
# # # while numero % 2 == 0:
# # #     print("Numero nao primo")
# # #     numero = int(input("Digite um numero inteiro: "))
# # # print("Numero primo")

# # ou
    
# # while True:
# #     numero = int(input("Digite um numero inteiro: "))
# #     if numero % 2 == 1:
# #         print("Numero primo")
# #         break
# #     else:
# #         print("Numero nao primo")
# #         numero = int(input("Digite um numero inteiro novamente: "))
 
 
# # crie um algoritmo que solicite ao usuário que crie uma senha. Em seguida, use um loop para pedir que o usuário confirme a senha. O loop deve continuar até que a senha de confirmação seja igual à senha original. Quando isso acontecer, exiba uma mensagem de confirmação.
       
# # senha = input("Crie uma senha: ")   
# # while True:
# #     confirme_senha = input("Confirme a senha novamente: ")
    
# #     if senha == confirme_senha:
# #         print (f"Senha Correta!")
# #         break
# #     else:
# #         senha = input("Crie uma senha: ")
       
# # Faça um programa que leia e valide as seguintes informações:
# # Nome: maior que 3 caracteres;
# # Idade: entre 0 e 150;
# # Salário: maior que zero;
# # Sexo: 'f' ou 'm';
# # Estado Civil: 's', 'c', 'v', 'd';

# # nome = input("Digite o seu nome: ")
# # while len(nome) > 3:
# #     print("Infomraçao valida")
# #     break
# # else: 
# #     print("Informaçao invalida")
# # idade = int(input("Digite a sua idade: "))
# # while idade <= 150:
# #     print("Infomraçao valida")
# #     break
# # else: 
# #     print("Informaçao invalida")
    
# # salario = float(input("Digite o seu salario: "))
# # while salario > 0:
# #     print("Infomraçao valida")
# #     break
# # else: 
# #     print("Informaçao invalida")

# # sexo = input("Digite o seu sexo (f ou m): ")
# # if sexo == "f":
# #     print("Infomraçao valida")
# # else:
# #     print("Informaçao invalida")

# # estado_civil = input("Digite o seu estado civil (s, c, v, d): ")
# # if estado_civil == "s":
# #     print("Infomraçao valida")
    
# # elif estado_civil == "c":
# #     print("Infomraçao valida")
    
# # elif estado_civil == "v":
# #     print("Infomraçao valida")
    
# # elif estado_civil == "d":
# #     print("Infomraçao valida")
    
# # else:
# #     print("Informaçao invalida")
    
    
# # Criação de uma calculadora basica  

# # operador = input("Digite o operador (*, +, -, /): ")
# # num1 = float(input("Digite um numero: "))
# # num2 = float(input("Digite um numero: "))

# # if operador == "*":
# #     print(num1 * num2)
# # if operador == "+":
# #     print(num1 + num2)
# # if operador == "-":
# #     print(num1 - num2)
# # if operador == "/":
# #     print(num1 / num2)

# # Construa um programa no qual o usuário cadastre um número
# # indeterminado de alunos de sua turma.

# # Ao fim do cadastro, o usuário deve informar qual aluno deseja
# # excluir do cadastro. Caso o aluno informado não tenha sido
# # localizado, o programa deve apresentar uma mensagem
# # informando “Aluno não cadastrado.”. Caso contrário, o programa
# # deve apagar o nome do aluno do cadastro e informar a
# # mensagem “Aluno excluído com sucesso.”. Por fim, o programa
# # deve imprimir o cadastro dos alunos ordenado alfabeticamente.


# # alunos = []

# # while True:
# #     cadastro = input("Cadastre o nome do aluno (ou digite '0' para terminar): ")
# #     if cadastro == "0":
# #         break
# #     alunos.append(cadastro)
 
# # print("Cadastro atual dos alunos:", alunos)
    
# # usuario = input("Qual aluno você quer excluir: ")

# # if usuario in alunos:
# #     alunos.remove(usuario)
# #     print(f"O aluno {usuario} foi excluído com sucesso.")
# # else:
# #     print("Aluno não cadastrado.")
    
# # alunos.sort()
# # print(f"Cadastro atualizado dos alunos: {alunos}" )

# # 1) Crie um programa que carregue uma lista para armazenar N
# # números inteiros positivos (considere que o usuário sempre
# # informará valores distintos e inteiros positivos). Ao fim, mostre o
# # menor e o maior número e em qual índice eles se encontram.

# # numero = int(input("Digite N numeros inteiros distintos ou positivos: "))
# # N =[]
# # for i in range(numero):
# #     numeros = int(input("Digite os numeros: "))
# #     N.append(numeros)
     
# # x = N.index(max(N)) 
# # Y = N.index(min(N)) 


# # print(f"O maior numero é: {(max(N))} e o seu indice é: {N.index(max(N))} ")
# # print(f"O menor numero é: {(min(N))} e o seu indice é: {N.index(min(N))} ")

# 2) Construa um programa que crie uma lista A para armazenar 5
# números informados pelo usuário. O programa também deve
# preencher uma lista B, contendo 5 números, cujos valores
# também são informados pelo usuário. Por fim, o programa deve

# colocar os valores que estão na lista A para a lista B e vice-
# versa.

# listaA = []
# listaB = []

# for i in range(5):
#     n1 = float(input("Digite um valor (Lista A): "))
#     listaA.append(n1)

# for i in range(5):
#     n2 = float(input("Digite um valor (Lista): "))
#     listaB.append(n2)
    
# listaA.extend(listaB)
# print(listaA)

# listaB.extend(listaA)
# print(listaB)

# 1 - Faça um Programa que leia um conjunto de 5 números inteiros, mostre-os na ordem inversa e apresente a soma desses números.
# # soma = 0
# # lista = []
# # for i in range(1,6):
# #     numero = int(input("Digite um numero inteiro: "))
# #     soma += numero
# #     lista.append(numero)


# # lista.reverse()
# # print(lista)
# # print(f"A soma total dos numeros são: {soma}")

# 2-  Inicialize um programa com 20 números inteiros. Armazene os números pares em coleção de dados com nome PAR e os números ímpares com nome IMPAR. Imprima essas coleções de dados.
# PAR = []
# IMPAR = []
# for i in range(1,20):
#     if i % 2 == 0:
#         PAR.append(i)
        
#     else:
#         IMPAR.append(i)
        
# print(PAR)
# print(IMPAR)


# pessoas = {'nome': 'Gustavo', 'idade': '18'}
# print(f" O nome é {pessoas['nome']} e idade é {pessoas['idade']}")

# pessoas = {'nome': 'Gustavo', 'idade': '18'}
# for k, v in pessoas.items():
#     print(f" {k} = {v}")


# pessoas = {'nome': 'Gustavo', 'idade': '18'}
# del pessoas ['idade']
# for k, v in pessoas.items():
#     print(f" {k} = {v}")


# pessoas = {'nome': 'Gustavo', 'idade': '18'}
# pessoas ['nome'] = 'Leandro' #mudar o valor dentro
# for k, v in pessoas.items():
#     print(f" {k} = {v}")
    
    
# pessoas = {'nome': 'Gustavo', 'idade': '18'}
# pessoas ['peso'] = '98' #tambem pode adicionar um valor dentro
# for k, v in pessoas.items():
#     print(f" {k} = {v}")

# estado = dict()
# brasil = list()
# for c in range(0,3):
#     estado['UF'] = str(input('Unidade Federativa: '))
#     estado['sigla'] = str(input('Sigla do Estado: '))
#     brasil.append(estado.copy())
# # print(brasil)
# for e in brasil:
#     # print(e)
#     for k, c in e.items():
#         print(f' O campo {k} tem valor {c}')

# aluno = dict()
# aluno ['nome'] = str(input('Digite o nome do aluno: '))
# aluno ['media'] = float(input(f'Digite a media do {aluno["nome"]}: '))
# if aluno['media'] >= 7:
#     aluno ['situaçao'] = 'Aprovado'
# elif 5 <= aluno['media'] < 7:
#     aluno ['situaçao'] = 'Recuperação'
# else:
#     aluno ['situaçao'] = 'Reprovado'

# print(aluno)

# Crie um programa onde 4 jogadores joguem um dado e tenham resulatados aleatorios. Guarde
# esses resultadados em um dicionario. No final, coloque esse dicionario em ordem, sabendo
# que o vencedor tirou o maior dado.

# from random import randint
# from time import sleep
# from operator import itemgetter
# jogo = {'jogador1': randint(1,6),
#         'jogador2': randint(1,6),
#         'jogador3': randint(1,6),
#         'jogador4': randint(1,6)}

# ranking = dict()
# print('Valores sorteados')
# for k, v in jogo.items():
#     print(f'{k} tirou {v} no dado')
#     sleep(1)
    
# ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
# print(ranking)
# for i, v in enumerate(ranking):
#     print(f'{i+1} lugar: {v[0]} com {v[1]}')
#     sleep(1)