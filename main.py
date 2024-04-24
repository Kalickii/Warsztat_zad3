
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
