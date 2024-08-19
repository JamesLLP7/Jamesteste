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

# Captura a entrada do usuário
n = int(input("Digite um número inteiro: "))

# Gera o dicionário com pares (i, i*i)
resultado = {i: i*i for i in range(1, n+1)}

# Imprime o dicionário
print(resultado)
