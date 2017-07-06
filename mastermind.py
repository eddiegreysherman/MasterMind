import random
import os
import collections

def generate_code():

    master_code = []
    for i in range(4):
        master_code.append(random.randint(1, 6))
    return master_code

code = generate_code()
#code = [2, 2, 1, 6]

attempts = []
os.system('clear')

while len(attempts) < 10:
    guess_code = []
    hints = []
    seen = []
    i = 1
    #print(code)
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
                if a[i] not in seen:
                    b_idx = [idx for idx, num in enumerate(b) if num == a[i]]
                    a_idx = [idx for idx, num in enumerate(a) if num == a[i]]
                    w_list = [x for x in a_idx if x not in b_idx]
                    b_list = [x for x in a_idx if x in b_idx]
                    if len(a_idx) > len(b_idx):
                        for _ in range(len(b_list)):
                            hints.append("B")
                    else:
                        for _ in range(len(w_list)):
                            hints.append("W")
                        for _ in range(len(b_list)):
                            hints.append("B")
                seen.append(a[i])
        return hints

    # the arguments of this function need to be in the correct order...else it breaks
    hints = process_guess(code, guess_code)

    if hints == ['B', 'B', 'B', 'B']:
        print("YOU WIN!!!!!!!!!")
        break


    attempts.append([[guess_code, hints]])

    os.system('clear')

    for _ in range(len(attempts)):
        print(str(len(attempts)) + ": " + str(attempts[_][0][0]) + "\t" + str(attempts[_][0][1]))

if hints != ['B', 'B', 'B', 'B']:
    print("The code was " + str(code))
    print("YOU LOST!!!!")
