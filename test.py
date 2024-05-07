import tkinter as tk
from tkinter import messagebox
import os

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def button_click(row, col):
    position = row * 3 + col + 1
    if placeholders[position] == ' ':
        placeholders[position] = 'X' if player == 1 else 'O'
        button_texts[position].set(placeholders[position])
        if check_winner(placeholders):
            messagebox.showinfo("Winner!", f"Player {player} wins!")
            root.quit()
        elif ' ' not in placeholders.values():
            messagebox.showinfo("Tie!", "It's a tie!")
            root.quit()
        else:
            switch_player()

def switch_player():
    global player
    player = 2 if player == 1 else 1

def create_button(row, col):
    position = row * 3 + col + 1
    button_texts[position] = tk.StringVar()
    button = tk.Button(root, textvariable=button_texts[position], width=10, height=5, command=lambda r=row, c=col: button_click(r, c))
    button.grid(row=row, column=col, padx=5, pady=5)

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

def start_game():
    global root, player, placeholders, button_texts
    root = tk.Tk()
    root.title("Tic Tac Toe")

    player = 1
    placeholders = {i: ' ' for i in range(1, 10)}
    button_texts = {}

    for row in range(3):
        for col in range(3):
            create_button(row, col)

    root.mainloop()

def main():
    cls()
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

    3. To place your mark, click the corresponding button on the GUI.
    4. The first player to get three of their marks in a row (horizontally, vertically, or diagonally) wins.
    5. If all spaces are filled without any player achieving three in a row, the game ends in a tie.

    Press Enter to start the game...
    """)

    input("")

    start_game()

if __name__ == "__main__":
    main()
