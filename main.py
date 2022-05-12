class TikTackToeGame:
    def __init__(self):
        self.board = None
        self.status = None
        self.current_player = None
        self.current_player_symbol = None

    def start(self):
        self.board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.status = "RUNNING"
        self.current_player = "Player 1"
        self.current_player_symbol = 'X'

    def take_turn(self, space):
        self.board[space-1] = self.current_player_symbol
        self.check_board()

        if self.status == "TIE" or self.status == "WON":
            return None

        self.switch_players()

    def check_board(self):
        if set(self.board) == set(['X', 'O']):
            self.status = "TIE"
            return None

        winning_indices = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]
        for index in winning_indices:
            line = set([self.board[index[0]], self.board[index[1]], self.board[index[2]]])
            if line == set('X') or line == set('O'):
                self.status = "WON"
                return None

        return None

    def switch_players(self):
        if self.current_player == "Player 1":
            self.current_player = "Player 2"
            self.current_player_symbol = 'O'
        else:
            self.current_player = "Player 1"
            self.current_player_symbol = 'X'

    def generate_board_string(self):
        s = """
         {} | {} | {} 
        ---|---|---
         {} | {} | {} 
        ---|---|---
         {} | {} | {}
        """

        return s.format(*self.board)

def main():
    while True:
        user_input = input("\nPick your action (number from 1-3):\n    1) Player vs Player\n    2) Player vs A.I.\n    3) Quit\n \nAction: ")

        if str(user_input) == '1':
            print("Starting Player vs Player...\n")
            tik_tack_toe_pvp_runner()
            continue

        elif str(user_input) == '2':
            print("Game mode not implemented yet...\n")
            continue

        elif str(user_input) == '3':
            print("Quitting game...\n")
            break

        else :
            print("Invalid Input\n")
            continue

def tik_tack_toe_pvp_runner():
    game = TikTackToeGame()

    game.start()
    print(game.generate_board_string() + '\n')
    while game.status == "RUNNING":
        player_input = input(game.current_player + " take your turn... ")

        if player_input not in str(game.board) or player_input == 'x' or player_input == 'o':
            print(f"Invalid input. Choose an available space: {*[x for x in game.board if str(x).isnumeric()],}")
            continue
        
        game.take_turn(int(player_input))

        print(game.generate_board_string() + '\n')

    if game.status == "TIED":
        print("Tie Game!")
    else:
        print(f"Congratulations {game.current_player}, You've Won!")

    return None

if __name__ == "__main__":
    main()