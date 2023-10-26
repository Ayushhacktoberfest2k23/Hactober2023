import random

snakes = {16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}

def roll_dice():
    return random.randint(1, 6)

def move_player(player, dice_value):
    new_position = player + dice_value
    if new_position > 100:
        return player
    if new_position in snakes:
        print("Oops! Snake at position", new_position, "takes you down to", snakes[new_position])
        return snakes[new_position]
    elif new_position in ladders:
        print("Yay! Ladder at position", new_position, "takes you up to", ladders[new_position])
        return ladders[new_position]
    else:
        return new_position

def snake_ladder_game():
    player1, player2 = 0, 0
    turn = 0
    while player1 < 100 and player2 < 100:
        if turn % 2 == 0:
            input("Player 1: Press enter to roll the dice ")
            dice_value = roll_dice()
            print("Player 1 rolled the dice and got:", dice_value)
            player1 = move_player(player1, dice_value)
            print("Player 1 current position:", player1)
        else:
            input("Player 2: Press enter to roll the dice ")
            dice_value = roll_dice()
            print("Player 2 rolled the dice and got:", dice_value)
            player2 = move_player(player2, dice_value)
            print("Player 2 current position:", player2)
        turn += 1

    if player1 >= 100:
        print("Player 1 wins!")
    else:
        print("Player 2 wins!")

snake_ladder_game()
