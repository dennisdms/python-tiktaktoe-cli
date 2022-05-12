class TikTackToeGame:
    def __init__(self):
        self.board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.status = "IDLE"
        self.current_player = None
        self.current_player_symbol = None

    def start(self):
        self.status = "RUNNING"
        self.current_player = "Player 1"
        self.current_player_symbol = 'x'

    def take_turn(self, space):
        self.board[space-1] = self.current_player_symbol
        self.check_board()

        if self.status == "TIE" or self.status == "WON":
            return None

        self.switch_players()

    def check_board(self):
        if set(self.board) == set(['x', 'o']):
            self.status = "TIE"
            return None

        winning_indices = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]
        
        for index in winning_indices:
            line = set([self.board[index[0]], self.board[index[1]], self.board[index[2]]])
            if line == set('x') or line == set('o'):
                self.status = "WON"
                return None

        return None

    def switch_players(self):
        if self.current_player == "Player 1":
            self.current_player = "Player 2"
            self.current_player_symbol = 'o'
        else:
            self.current_player = "Player 1"
            self.current_player_symbol = 'x'

    def generate_board_string(self):
        board_string = """
                |         |         
                |         |         
        {}       |    {}    |     {}  
                |         |         
       ---------+---------+---------
                |         |         
                |         |         
        {}       |    {}    |    {}   
                |         |         
                |         |         
       ---------+---------+---------
                |         |         
                |         |         
        {}       |    {}    |      {}  
                |         |         
                |         |         """


        return board_string.format(*self.board)
        
def tik_tack_toe_runner(mode):
    game = TikTackToeGame(mode)

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

def main():
    tik_tack_toe_runner("Player vs Player")

if __name__ == "__main__":
    main()