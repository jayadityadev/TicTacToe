import os

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def playground(values):
    cls()
    print(f"  {values[1]}  |  {values[2]}  |  {values[3]}")
    print("-----------------")
    print(f"  {values[4]}  |  {values[5]}  |  {values[6]}")
    print("-----------------")
    print(f"  {values[7]}  |  {values[8]}  |  {values[9]}")
    print()


def get_player_input(player, values):
    while True:
        try:
            position = int(input(f"Player {player} -> Position to place {'X' if player == 1 else 'O'} [1-9]: "))
            if position not in range(1, 10):
                print("Invalid position. Try again.")
            elif values[position] != ' ':
                print("Position already occupied. Try again.")
            else:
                return position
        except ValueError:
            print("Invalid input. Please enter a number.")


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


def main():
    print("""
    Tic-Tac-Toe Game:

    How to Play:
    1. The game starts with an empty grid.
    2. Players take turns entering the position where they want to place their mark ('X' or 'O').
       Positions are numbered from 1 to 9, corresponding to the grid layout as follows:

            1 | 2 | 3
           -----------
            4 | 5 | 6
           -----------
            7 | 8 | 9

    3. To place your mark, enter the position number when prompted.
    4. The first player to get three of their marks in a row (horizontally, vertically, or diagonally) wins.
    5. If all spaces are filled without any player achieving three in a row, the game ends in a tie.

    Have fun playing Tic-Tac-Toe!
    """)
    begin = input("Press Enter to start the game...")
    if begin == '':
        placeholders = {i: ' ' for i in range(1, 10)}
        while True:
            for player in range(1, 3):
                playground(placeholders)
                position = get_player_input(player, placeholders)
                placeholders[position] = 'X' if player == 1 else 'O'
                if check_winner(placeholders):
                    playground(placeholders)
                    print(f"Player {player} wins!")
                    return
                if ' ' not in placeholders.values():
                    playground(placeholders)
                    print("It's a tie!")
                    return


if __name__ == "__main__":
    main()
