import random
import os

def generate_code():

    master_code = []
    for i in range(4):
        master_code.append(random.randint(1, 6))
    return master_code

code = generate_code()


attempts = []
os.system('clear')

while len(attempts) < 10:
    guess_code = []
    hints = []
    seen = []
    i = 1
    print(code)
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



    def process_guess(a, b):

        if a == b:
            return ['B', 'B', 'B', 'B']

        for i in range(4):
            # is the current number in the code?
            if a[i] in b:
                # is the current number in this location?
                if a[i] == b[i]:
                    hints.append("B")
                # if the the count of current are equal
                elif a.count(a[i]) == b.count(a[i]):
                    # give the white hint
                    hints.append("W")
                    # mark current number as seen
                    seen.append(a[i])
                    continue
                else:
                    # if not already seen this number
                    if not a[i] in seen:
                        for _ in range(abs(a.count(a[i]) - b.count(a[i]))):
                            hints.append("W")
        return hints

    # the arguments of this function need to be in the correct order...else it breaks
    hints = process_guess(code, guess_code)

    if hints == ['B', 'B', 'B', 'B']:
        print("YOU WIN!!!!!!!!!")
        break


    attempts.append([[guess_code, hints]])

    os.system('clear')

    for _ in range(len(attempts)):
        print(str(i) + ": " + str(attempts[_][0][0]) + "\t" + str(attempts[_][0][1]))

if hints != ['B', 'B', 'B', 'B']:
    print("The code was " + str(code))
    print("YOU LOST!!!!")
