from enum import Enum
from math import ceil

def main():
    mode = Modes.TWO_PLAYER

    if mode is Modes.TWO_PLAYER:
        tiktaktoe_player_vs_player()

def tiktaktoe_player_vs_player():
    is_game_over = False
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    game_over = False
    turn = Modes.P1

    while not game_over:
        if turn == Modes.P1:
            input_p1 = int(input("Player 1 take your turn: "))
        else:
            input_p1 = int(input("Player 2 take your turn: "))

        if input_p1 not in set(board):
            print("You must enter a number between 1-9")
            continue

        if turn == Modes.P1:
            board[input_p1-1] = 'x'
            turn = Modes.P2
        else:
            board[input_p1-1] = 'o'
            turn = Modes.P1

        print(generate_board_string(board))

        if set(board) == set(['x','o']):
            print(generate_board_string(board))
            print("Game tied")
            game_over = True

        for i in [0, 3, 6]:
            if set(board[i:i+3]) == set(['o']):
                print("Player 2 has won the game")
                game_over = True
                break
            elif set(board[i:i+3]) == set(['x']):
                print("Player 1 has won the game")
                game_over = True
                break

def generate_board_string(board):
    square_width = 9
    square_height = 5
    board_string = """
            |         |         
      {}     |    {}    |     {}   
            |         |         
   ---------+---------+---------
            |         |         
            |         |         
      {}     |    {}    |    {}     
            |         |         
            |         |         
   ---------+---------+---------
            |         |         
            |         |         
       {}    |    {}    |      {}   
            |         |         
            |         |         
    """


    return board_string.format(*board)

class Modes(Enum):
    TWO_PLAYER = "Player vs Player"
    VS_AI = "Player vs A.I."
    P1 = "x"
    P2 = "o"

if __name__ == "__main__":
    main()