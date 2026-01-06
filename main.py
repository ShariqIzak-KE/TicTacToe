from subprocess import call
from time import sleep
from random import randint
import time
import string
import random

# Global Variables
array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
GAME_OVER = False
player_turn = False
name = ''
symbol = 'X'
comp_started = False
comp_symbol = 'O'
comp_turn_number = 0

# Winning line Combinations
win1 = [0, 1, 2]
win2 = [3, 4, 5]
win3 = [6, 7, 8]
win4 = [0, 3, 6]
win5 = [1, 4, 7]
win6 = [2, 5, 8]
win7 = [0, 4, 8]
win8 = [2, 4, 6]


# Clear Screen Function
def clear_screen():
    # check and make call for specific operating system
    _ = call('clear')


# Check Win Combinations
def check_win(symbol, player_turn):
    # Check for draw
    global array

    if player_turn:
        winner = 'You Win!'
    else:
        winner = 'Computer wins!'

    if all(type(x) is str for x in array):
        print('Draw')
        return end_game()
    if array[0] == symbol and array[1] == symbol and array[2] == symbol:
        print(f"{winner}")
        return end_game()
    if array[3] == symbol and array[4] == symbol and array[5] == symbol:
        print(f"{winner}")
        return end_game()
    if array[6] == symbol and array[7] == symbol and array[8] == symbol:
        print(f"{winner}")
        return end_game()
    if array[0] == symbol and array[3] == symbol and array[6] == symbol:
        print(f"{winner}")
        return end_game()
    if array[1] == symbol and array[4] == symbol and array[7] == symbol:
        print(f"{winner}")
        return end_game()
    if array[2] == symbol and array[5] == symbol and array[8] == symbol:
        print(f"{winner}")
        return end_game()
    if array[0] == symbol and array[4] == symbol and array[8] == symbol:
        print(f"{winner}")
        return end_game()
    if array[2] == symbol and array[4] == symbol and array[6] == symbol:
        print(f"{winner}")
        return end_game()


def header():
    print("Tic Tac Toe V1.0")
    print("****************")


# Print Screen Function
def print_screen():
    clear_screen()
    header()
    print('\n')
    print(f"   {array[0]} | {array[1]} | {array[2]}")
    print("   ---------")
    print(f"   {array[3]} | {array[4]} | {array[5]}")
    print("   ---------")
    print(f"   {array[6]} | {array[7]} | {array[8]}")
    print('\n')


# Startup - Ask user for name, and symbol

def startup():
    global name
    global symbol
    global comp_symbol

    clear_screen()
    header()
    name = input("What is your name?")

    clear_screen()
    header()
    print(f"Welcome {name},")
    symbol = input("What is your Symbol X or O?")
    # TODO Ensure choice is one of two either small or caps
    symbol = check_symbol(symbol)
    clear_screen()
    header()
    print(f"{name} will be playing {symbol}")
    comp_symbol = opp_symbol(symbol)

    # Flip Coin
    flip_coin(name)
    main(symbol, name)


# Check symbol to be either X or O

def check_symbol(symbol):
    if symbol.upper() == 'X' or symbol.upper() == 'O':
        return symbol.upper()
    else:
        new_symbol = input("Please enter either X or O:")
        return check_symbol(new_symbol)


# Returns opposing symbol
def opp_symbol(symbol):
    if symbol == 'X':
        return 'O'
    else:
        return 'X'


# Flip Coin and assign players
def flip_coin(name):
    print("Flipping Coin")
    sleep(1)
    dice = randint(0, 1)

    global player_turn
    global comp_started
    global comp_turn_number

    if dice == 0:
        player_turn = False
        comp_started = True
    else:
        player_turn = True
        comp_started = False
    starter = convert_dice(dice, name)
    comp_turn_number = 1
    print(f"{starter} will start")
    sleep(1)
    return


# Converts dice to player name
def convert_dice(dice, name):
    if dice:
        return name
    else:
        return 'Computer'




# Check if a symbol has one left to make a 3 streak
def two_streak(symbol, array):
    # Returns an index position after iterating through win combinations else none
    # Win 1
    plays = []

    empty_slots = []
    count = 0
    for x in win1:
        if array[x] == symbol:
            count += 1
        if array[x] != symbol and array[x] != opp_symbol(symbol):
            empty_slots.append(x)
    if count == 2:
        plays.append(empty_slots)

    # Win 2
    empty_slots = []
    count = 0
    for x in win2:
        if array[x] == symbol:
            count += 1
        if array[x] != symbol and array[x] != opp_symbol(symbol):
            empty_slots.append(x)
    if count == 2:
        plays.append(empty_slots)

    # Win 3
    empty_slots = []
    count = 0
    for x in win3:
        if array[x] == symbol:
            count += 1
        if array[x] != symbol and array[x] != opp_symbol(symbol):
            empty_slots.append(x)
    if count == 2:
        plays.append(empty_slots)

    # Win 4
    empty_slots = []
    count = 0
    for x in win4:
        if array[x] == symbol:
            count += 1
        elif array[x] != symbol and array[x] != opp_symbol(symbol):
            empty_slots.append(x)
    if count == 2:
        plays.append(empty_slots)

    # Win 5
    empty_slots = []
    count = 0
    for x in win5:

        if array[x] == symbol:
            count += 1

        if array[x] != symbol and array[x] != opp_symbol(symbol):
            empty_slots.append(x)
    if count == 2:
        plays.append(empty_slots)

    # Win 6
    empty_slots = []
    count = 0
    for x in win6:
        if array[x] == symbol:
            count += 1
        if array[x] != symbol and array[x] != opp_symbol(symbol):
            empty_slots.append(x)
    if count == 2:
        plays.append(empty_slots)

    # Win 7
    empty_slots = []
    count = 0
    for x in win7:
        if array[x] == symbol:
            count += 1
        if array[x] != symbol and array[x] != opp_symbol(symbol):
            empty_slots.append(x)
    if count == 2:
        plays.append(empty_slots)

    # Win 8
    empty_slots = []
    count = 0
    for x in win8:
        if array[x] == symbol:
            count += 1
        if array[x] != symbol and array[x] != opp_symbol(symbol):
            empty_slots.append(x)

    if count == 2:
        plays.append(empty_slots)

    # BUG FIX: Checks special case when an empty list is added to plays
    if len(plays) == 1 and plays[0] == []:
        return None


    elif len(plays) != 0:
        plays = [ele for ele in plays if ele != []]
        try:
            move = random.choice(plays)
            return move.pop()
        except IndexError:
            return random_play(array)
    else:
        return None


# Returns a random playable index
def random_play(array):
    available = []
    print('The computer is thinking...')
    sleep(1)
    for c in range(0, 9):
        if array[c] != 'X' and array[c] != 'O':
            available.append(c)
    if len(available) != 0:
        return random.choice(available)
    else:
        return None


# Check availability of corner slot to play
def check_corners(array):
    # checks the corners of the table and return a random playable corner
    corners = [0, 2, 6, 8]
    available = []
    for c in corners:
        if array[c] != 'X' and array[c] != 'O':
            available.append(c)

    if len(available) != 0:
        return random.choice(available)
    else:
        return None


# Generates next move for computer
def generate_play():
    global array
    global comp_started
    global comp_symbol
    global comp_turn_number

    player_symbol = opp_symbol(comp_symbol)

    if comp_started:
        # first move = pos 0 always
        if comp_turn_number == 1:
            return 0
        # second move = check for either 3,7 or 9 whichever is empty
        if comp_turn_number == 2:
            if array[2] != player_symbol:
                return 2
            elif array[6] != player_symbol:
                return 6
            elif array[8] != player_symbol:
                return 9
        # third move  = check for wi
        if comp_turn_number == 3:
            if two_streak(comp_symbol, array) is not None:
                return two_streak(comp_symbol, array)
            else:
                return check_corners(array)
        if comp_turn_number > 3:
            return two_streak(comp_symbol, array)

    else:
        # if player started...
        if comp_turn_number == 1:
            return check_corners(array)
        if comp_turn_number == 2:
            if two_streak(player_symbol, array) is not None:
                return two_streak(player_symbol, array)
            else:
                return check_corners(array)
        if comp_turn_number >= 3:
            if two_streak(comp_symbol, array) is not None:
                return two_streak(comp_symbol, array)
            else:
                return two_streak(player_symbol, array)


# Check choice is within range
def check_choice(choice, num_list):
    # Check if choice is within num_list and not existing choice
    # get options of choice

    temp_list = num_list
    # remove X and O from num_list to remain with playable options
    temp_list = [ele for ele in temp_list if ele != 'X']
    temp_list = [ele for ele in temp_list if ele != 'O']

    # Draw - no further playable
    if len(temp_list) == 0:
        print("DRAW")
        return end_game()

    if choice.isnumeric():
        # check if choice is in temp_list
        if int(choice) in temp_list:
            return choice
        # Else ask user for new choice
        else:
            new_choice = input("It's not even on the screen! Enter a box number to mark:")
            return check_choice(new_choice, num_list)
    else:
        new_choice = input("I see what you did there! Don't be cocky:")
        return check_choice(new_choice, num_list)


# Main Game
def main(symbol, name):
    global player_turn
    global GAME_OVER
    global array
    global comp_started
    global comp_symbol
    global comp_turn_number

    array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    while not GAME_OVER:
        clear_screen()
        header()
        print_screen()
        if player_turn:
            #  Debug states
            # print(
            #     f"Computer is: {comp_symbol} \nComputer started: {comp_started} \nComp Turn Number: {comp_turn_number}.")
            choice = input(f"{name}, enter the box number \nto mark {symbol}?")
            # check that the character is one of available boxes
            position = check_choice(choice, array)
            array[int(position) - 1] = symbol
            print_screen()

            GAME_OVER = check_win(symbol, player_turn)

        else:
            print("Computer will play now.")
            next_move = generate_play()
            array[int(next_move)] = opp_symbol(symbol)
            comp_turn_number += 1
            sleep(1)
            print_screen()
            GAME_OVER = check_win(opp_symbol(symbol), player_turn)

        player_turn = not player_turn

# End Game Sequence
def end_game():
    global GAME_OVER
    print("Game Over!"
         "New Game in")
    print("3")
    sleep(0.5)
    print("2")
    sleep(0.5)
    print("1")
    sleep(0.5)
    flip_coin(name)
    GAME_OVER = False
    main(symbol, name)


# Running sequence
startup()
end_game()
