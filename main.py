
def user_input():
    """
    Checks if the user input is in ["too small", "too big", "you win"].
    :return: Returns correct response from the list
    """
    anwsers = ["too small", "too big", "you won"]
    user_input = input().lower()
    if user_input not in anwsers:
        print(f'{user_input} is not in ["too small", "too big", "you won"]')
    else:
        return user_input

print("Think of a number  between 0 and 1000, and i will guess it in max. 10 tries.")
print('Use "too big", "too small", "you won" to hint me :)')

min = 0
max = 1000

while True:
    guess = int((max - min) / 2) + min
    print("I'm guessing: " + str(guess))
    hint = user_input()
    if hint == "you won":
        print("I Won!")
        break
    elif hint == "too big":
        max = guess
    elif hint == "too small":
        min = guess
