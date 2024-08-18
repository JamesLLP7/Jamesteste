#Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
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
