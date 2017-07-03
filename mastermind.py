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
attempts = []

while len(attempts) < 10:
    i = 1
    while i <= 4:
        num = input("Guess number {} in the pattern (Must be 1-6): ".format(i))
        if not num.isnumeric():
            print("Please enter a NUMBER, 1 - 6.")
            continue
        else:
            num = int(num)

        if num in [1, 2, 3, 4, 5, 6]:
            guess_code.append(num)
            i += 1
        else:
            print("The number must be 1 through 6.")

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

    #attempts.append([[guess_code, hints]])
    attempts.append(list([guess_code, hints]))

    for _ in range(len(attempts)):
        print(attempts)
