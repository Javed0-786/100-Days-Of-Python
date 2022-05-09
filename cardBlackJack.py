import random


choice = input("Do you want to play a game of Blackjack? type 'y' or 'no': ")


while (choice == 'y'):
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    i = 1
    j = 2
    player = []
    computer = []
    player.append(cards[random.randint(0, 12)])
    player.append(cards[random.randint(0, 12)])
    computer.append(cards[random.randint(0, 12)])
    score = player[0] + player[1]
    comp = computer[0]
    print("Your cards: ", player, " current score: ", score)
    print("Computer's first card is: ", computer[0])

    while (comp < 17):
        computer.append(cards[random.randint(0, 12)])
        comp = comp + computer[i]
        i = i+1

    ch = input("Type 'y' to get another card, type 'n' to pass: ")
    while (score < 21 and ch == 'y'):

        if (comp > 21):
            print("Your final hand:", player, "final score: ", score)
            print("Computer's final hand:", computer, "final score: ", comp)
            print("Win with a Blackjack 😎")
            ch = 'n'
            break

        elif(ch == 'y'):

            player.append(cards[random.randint(0, 12)])
            score = score + player[j]
            j = j+1
            if (score > 21):
                print("Your final hand:", player, "final score: ", score)
                print("Computer's final hand:",
                      computer, "final score: ", comp)
                print("You went over. You lose 😭")
                ch = 'n'
                break

            elif (comp < score or score == 21):
                print("Your final hand:", player, "final score: ", score)
                print("Computer's final hand:",
                      computer, "final score: ", comp)
                print("You win 😃")
                ch = 'n'
                break

            print("Your cards: ", player, " current score: ", score)
            print("Computer's first card is: ", computer[0])

            ch = input("Type 'y' to get another card, type 'n' to pass:")

    if (comp > 21):
        print("Your final hand:", player, "final score: ", score)
        print("Computer's final hand:", computer, "final score: ", comp)
        print("Win with a Blackjack 😎")

    elif (score > 21):
        print("Your final hand:", player, "final score: ", score)
        print("Computer's final hand:", computer, "final score: ", comp)
        print("You went over. You lose 😭")

    elif (comp > score):
        print("Your final hand:", player, "final score: ", score)
        print("Computer's final hand:", computer, "final score: ", comp)
        print("You lose 😭")

    else:
        print("Your final hand:", player, "final score: ", score)
        print("Computer's final hand:", computer, "final score: ", comp)
        print("You win 😃")
    choice = input(
        "Do you want to play a game of Blackjack? type 'y' or 'no': ")
