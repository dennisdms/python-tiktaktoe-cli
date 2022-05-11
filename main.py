from enum import Enum


def main():
    mode = Modes.TWO_PLAYER

    if mode is Modes.TWO_PLAYER:
        tiktaktoe_player_vs_player()

def tiktaktoe_player_vs_player():
    is_game_over = False
    board = [[1,2,3],[4,5,6],[7,8,9]]

    display_board(board)

def display_board(board):
    square_width = 9
    square_height = 5
    board_string = ''

    for i in range(3):
        for j in range(square_height):
            board_string += ' ' * square_width + '|'
            board_string += ' ' * square_width + '|'
            board_string += ' ' * square_width + '\n'

        if i == 2:
            break

        board_string += '-' * (square_width ) + '+'
        board_string += '-' * (square_width ) + '+'
        board_string += '-' * (square_width ) + '\n'
    print(board_string)

class Modes(Enum):
    TWO_PLAYER = "Player vs Player"
    VS_AI = "Player vs A.I."

if __name__ == "__main__":
    main()