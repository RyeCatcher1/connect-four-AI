class ConnectFourBoard:
    def __init__(self):
        self.width = 7
        self. heigth = 6
        self.board = [[0 for column in range(self.width)] for row in range(self.heigth)]
        self.winner = None
        self.game_over = False
        self.current_player = 1

    def display_board(self):
        print(self.board)
    def check_winner(self):
        pass
    def display_winner(self):
        pass
    def check_valid_move(self):
        pass
    def drop_piece(self, move):
        self.board[move][0] = self.current_player

class Game:
    def __init__(self):
        self.board = ConnectFourBoard()

    def play(self):
        while not self.board.game_over:
            self.board.display_board()
            move = self.get_player_move()
            self.board.drop_piece(move)


        

    def get_player_move(self):
        while True:
            try:
                move = int(input(f"Player {self.board.current_player}, choose column (0-{self.board.width-1}): "))
                return move
            except ValueError:
                print("Invalid")


juego = Game()
juego.play()

