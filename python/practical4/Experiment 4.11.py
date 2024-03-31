# factorial of a number
print("Name:Bharati Raja Swami\nRoll No: 2210997058")

num = int(input("Enter a number: "))
fact = 1
i = 1
while i <= num:
    fact = fact * i
    i = i + 1
print(f"Factorial of {num} is {fact}")