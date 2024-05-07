import os
import random
import time


# Colored text functions

def red_text(text):
    return f"\033[91m{text}\033[0m"

def green_text(text):
    return f"\033[92m{text}\033[0m"

def yellow_text(text):
    return f"\033[93m{text}\033[0m"

def blue_text(text):
    return f"\033[94m{text}\033[0m"

def orange_text(text):
    return f"\033[38;5;208m{text}\033[0m"


# Function to clear the console screen

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


# Function to print the Tic Tac Toe board

def print_board(values):
    clear_screen()
    print(f"  {values[1]}  |  {values[2]}  |  {values[3]}")
    print("-----------------")
    print(f"  {values[4]}  |  {values[5]}  |  {values[6]}")
    print("-----------------")
    print(f"  {values[7]}  |  {values[8]}  |  {values[9]}")
    print()


# Function to get player input

def get_player_input(player, values):
    while True:
        try:
            position = int(input(blue_text(f"Player {player} -> Position to place {'X' if player == 1 else 'O'} [1-9]: ")))
            if position not in range(1, 10):
                print("Invalid position. Try again.")
            elif values[position] != ' ':
                print("Position already occupied. Try again.")
            else:
                return position
        except ValueError:
            print(yellow_text("Invalid input. Please enter a number."))


# Function to check if there's a winner

def check_winner(values):
    winning_combinations = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9],
        [1, 4, 7], [2, 5, 8], [3, 6, 9],
        [1, 5, 9], [3, 5, 7]
    ]
    for combination in winning_combinations:
        if values[combination[0]] == values[combination[1]] == values[combination[2]] != ' ':
            return True
    return False


# Function to choose game mode

def game_mode():
    try:
        print(orange_text("Game Modes: \n1. Single Player\n2. Multiplayer"))
        print(red_text('\nPress Ctrl+C to exit the game at any time.'))
        while True:
            choice = input("\nEnter your choice: ")
            if choice in ('1', '2'):
                return int(choice)
            else:
                print(f"\n{yellow_text('Invalid input. Please enter 1 or 2.')}")
    except KeyboardInterrupt:
        print(red_text("\n\nExiting the game...\n"))
        exit()


# Function for single player mode

def single_player_mode(placeholders):
    try:
        begin = input(orange_text("\nPress Enter to start the game..."))
        if begin == '':
            while True:
                for player in [1, 2]:
                    print_board(placeholders)
                    if player == 1:
                        position = get_player_input(player, placeholders)
                    else:
                        position = random.choice([i for i in range(1, 10) if placeholders[i] == ' '])
                        print(orange_text(f"AI (O) selects position: {position}"))
                        time.sleep(1)
                    placeholders[position] = 'X' if player == 1 else 'O'
                    if check_winner(placeholders):
                        print_board(placeholders)
                        print(green_text("\nPlayer 1 wins!\n")) if player == 1 else print(green_text("\nAI wins!\n"))
                        return
                    if ' ' not in placeholders.values():
                        print_board(placeholders)
                        print(green_text("\nIt's a tie!\n"))
                        return
        else:
            print(yellow_text("\nInvalid input. Exiting..."))
            exit()
    except KeyboardInterrupt:
        print(red_text("\n\nExiting the game...\n"))
        exit()


# Function for multiplayer mode

def multi_player_mode(placeholders):
    try:
        begin = input(orange_text("\nPress Enter to start the game..."))
        if begin == '':
            while True:
                for player in range(1, 3):
                    print_board(placeholders)
                    position = get_player_input(player, placeholders)
                    placeholders[position] = 'X' if player == 1 else 'O'
                    if check_winner(placeholders):
                        print_board(placeholders)
                        print(green_text(f"\nPlayer {player} wins!\n"))
                        return
                    if ' ' not in placeholders.values():
                        print_board(placeholders)
                        print(green_text("\nIt's a tie!\n"))
                        return
        else:
            print(yellow_text("\nInvalid input. Exiting..."))
            exit()
    except KeyboardInterrupt:
        print(red_text("\n\nExiting the game...\n"))
        exit()
