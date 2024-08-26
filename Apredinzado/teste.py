'''Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
#between 2000 and 3200 (both included).
#the numbers obtained should be printed in a comma-separated sequence on a single line.



# Initialize an empty list to store the numbers
result = []

# Iterate over the range from 2000 to 3200 (inclusive)
for number in range(2000, 3201):
    # Check if the number is divisible by 7 but not a multiple of 5
    if number % 7 == 0 and number % 5 != 0:
        result.append(str(number))  # Append the number as a string to the list

# Join the list into a comma-separated string and print it
print(",".join(result))
'''



'''Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:

import math

# Capture the input numbers from the user as a comma-separated string
input_numbers = input("Enter numbers separated by commas: ")

# Split the input string into a list of numbers (as strings)
numbers = input_numbers.split(',')

# Initialize an empty list to store the factorials
factorials = []

# Calculate the factorial for each number and store it in the factorials list
for num in numbers:
    factorial = math.factorial(int(num))  # Convert the string to an integer and compute the factorial
    factorials.append(str(factorial))  # Convert the result back to a string and add it to the list

# Join the factorials list into a comma-separated string and print it
print(",".join(factorials))
'''

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
       