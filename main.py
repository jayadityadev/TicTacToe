from functions import game_mode, single_player_mode, multi_player_mode


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
    
    global placeholders
    placeholders = {i: ' ' for i in range(1, 10)}
    
    mode = game_mode()
    if mode == 1:
        single_player_mode(placeholders)
    elif mode == 2:
        multi_player_mode(placeholders)


if __name__ == "__main__":
    main()
