# Tic-Tac-Toe Game

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Contributing](#contributing)
- [Acknowledgement](#acknowledgement)

## Overview

The Tic-Tac-Toe Game is a Python program that allows users to play the classic game of Tic-Tac-Toe against either another player or an AI opponent. It provides a simple and interactive interface for users to enjoy the game.

## Features

- Play against another player or against an AI opponent.
- Clear and colored display for enhanced user experience.
- Ability to choose game mode: single player or multiplayer.
- Interactive interface guiding users through each step of the game.

## Getting Started

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/jayadityadev/TicTacToeGame.git
    ```

2. Run the main.py file to start the game:

    ```bash
    python3 main.py
    ```

## Usage

The game starts with an empty grid. Players take turns (w/ or w/o AI) entering the position where they want to place their mark ('X' or 'O'). Positions are numbered from 1 to 9, corresponding to the grid layout as follows:

     1 | 2 | 3
    -----------
     4 | 5 | 6
    -----------
     7 | 8 | 9

To place your mark, enter the position number when prompted. The first player to get three of their marks in a row (horizontally, vertically, or diagonally) wins. If all spaces are filled without any player achieving three in a row, the game ends in a tie.


## Contributing

Contributions are welcome! If you would like to improve this program, please follow these steps:

1. Fork the repository.
   
2. Create a new branch for your feature or bugfix:
   
   ```bash
   git checkout -b new-feature.
   ```
   
3. Make your changes and commit them (ensure they are well documented):
   
    ```bash
    git commit -m 'Add new feature'.
   ```
    
4. Push to the branch:
   
    ```bash
    git push origin new-feature
   ```
    
5. Create a pull request from your fork's branch to the main repository's main branch.

## Acknowledgement

Thank you for playing Tic-Tac-Toe! If you have any feedback or suggestions, feel free to open an issue on this repository.