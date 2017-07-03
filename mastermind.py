import random

def generate_code():
    master_code = []
    for i in range(4):
        master_code.append(random.randint(1, 6))
    return master_code

code = generate_code()

print(code)

guess_code = []
hints = []

for i in range(4):
   num = int(input("Guess a number (1-6): "))
   if num in [1, 2, 3, 4, 5, 6]:
    guess_code.append(num)

print(guess_code)

def process_guess(a,b):
    for i in range(4):
        if a[i] == b[i]:
            hints.append("B")
        elif a[i] in b:
            hints.append("W")
    return hints

print(process_guess(code, guess_code))