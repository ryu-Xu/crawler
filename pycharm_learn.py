from random import randint

def play():
    random_int = randint(0,10)
    while True:
        user_guess = int(input("what number did we guess (0-10)?"))

        if user_guess == random_int:
            print(f"you found the number({random_int}). congrats!")
            break

        if user_guess < random_int:
            print("猜小了")
            continue

        if user_guess > random_int:
            print("猜大了")
            continue

if __name__ == "__main__":
    play()
