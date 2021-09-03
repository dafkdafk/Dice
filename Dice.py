import random

intro = True
ready = False

def dice_roll(first, second):
    rolling = random.randint(first, second)
    return rolling


running = True
while running:
    while intro:
        print("""
>dice to create a dice
>role to roll the dice
>quit to quit""")
        intro = False
    ask = input("> ").lower()
    if ask == "quit":
        running = False
    elif ask == "dice":
        try:
            ask2 = int(input("how many dices: "))
            if ask2 == 1 or ask2 % 1 == 0:
                e_word = "st"
            elif ask2 == 2 or ask2 % 2 == 0:
                e_word = "nd"
            elif ask2 == 3 or ask2 % 3 == 0:
                e_word = "rd"
            else:
                e_word = "th"
            while True:
                for i in range(1, ask2 + 1):
                    try:
                        print(f"enter {i}{e_word} dice number")
                        ask3 = int(input("from: "))
                        ask4 = int(input("to: "))
                    except ValueError:
                        print("that is not a number")
                        ready = False
                        break
                    ready = True
                if ready:
                    print("ready to roll")
                break
        except ValueError:
            print("that is not a number")
            intro = True
    elif ask == "roll":
        try:
            print(f"({dice_roll(ask3, ask4)})")
            print("""
>roll to roll again
>quit to quit playing
>create to create new dice""")
            while True:
                aqc = input("> ")
                if aqc == "roll":
                    print(f"({dice_roll(ask3, ask4)})")
                elif aqc == "create":
                    intro = True
                    break
                elif aqc == "quit":
                    running = False
                    break
                else:
                    print("sorry, i don't understand that")
        except NameError:
            print("sorry you don't have a dice yet")
        except ValueError:
            print("sorry dice is can't be roll")
    elif ask == "roll":
        print("sorry dice haven't been created")
    else:
        print("sorry, i don't understand that")
