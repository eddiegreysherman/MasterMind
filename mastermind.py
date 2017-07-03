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

print(code)

def process_guess(a,b):
    for i in range(4):
        if a[i] == b[i]:
            hints.append("B")
        elif a[i] in b:
            hints.append("W")
    return hints

# trying to get a nested list going for display purposes...
hints = process_guess(code, guess_code)

attempts = [guess_code, hints]

print(attempts)

