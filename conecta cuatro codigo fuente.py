import sys
import random

class ConnectFourBoard:
    def __init__(self):
        self.width = 7
        self. heigth = 6
        self.data = [[0 for column in range(self.width)] for row in range(self.heigth)] # so self.board[1][3] is second row, fourth column
        self.winner = None
        self.game_over = False
        self.current_player = 1
        self.player_count = 2



    def display_board(self):
        symbols = {0: ".", 1: "X", 2: "O"}
        for row in reversed(range(self.heigth)):
            print("|" + "|".join(symbols[self.data[row][column]] for column in range(self.width)) + "|")
    def check_winner(self):
            for player in range(1,1+self.player_count):
                for row in range(self.heigth):
                    for column in range(self.width):
                        count = 0
                        for i in range(4):
                            if -1<row + i<self.heigth and 0<=column + i<self.width and self.data[row+i][column] == player:
                                count = count + 1
                        if count ==4:
                            return player

                for row in range(self.heigth):
                    for column in range(self.width):
                        count = 0
                        for i in range(4):
                            if -1<row + i<self.heigth and 0<column + i<self.width and self.data[row][column+i] == player:
                                count = count + 1
                        if count ==4:
                            return player
                    
            # now let's check diagonals
                for row in range(self.heigth):
                    count = 0
                    for i in range(4):
                        if -1<row + i<self.heigth and 0<=column + i<self.width and self.data[row+i][column+i] == player:
                            count = count + 1
                    if count ==4:
                        return player
                    
                for row in range(self.heigth):
                    count = 0
                    for i in range(4):
                        if -1<row - i<self.heigth and 0<=column + i<self.width and self.data[row-i][column+i] == player:
                            count = count + 1
                    if count ==4:
                        return player                    
            return 0
                    
    def display_winner(self):
        pass

    def check_valid_move(self, move):
        if type(move) is not int:
            print("Invalid")
            return False
        if move<0 or move>=self.width:
            return False
        for row in reversed(range(self.heigth)):
            if self.data[row][move]==0:
                #self.data[row][move] = self.current_player
                return True
        return False


    def drop_piece(self, move):
        #assumes input is correct
        for row in range(self.heigth):
            if self.data[row][move]==0:
                self.data[row][move] = self.current_player
                break
    def get_board_state(self):
        #print (tuple(tuple(self.data[row]) for row in range(self.heigth)))
        return tuple(tuple(self.data[row]) for row in range(self.heigth))
        
 


class Game:
    def __init__(self):
        self.board = ConnectFourBoard()
        self.time = 0
        self.winner = 0 #-1 for ties.
        self.game_over = False

    def play(self):
        while not self.board.game_over:
            self.board.display_board()
            move = self.get_player_move()
            self.board.drop_piece(move)
            self.board.current_player = 3-self.board.current_player
            self.time = self.time + 1
            if self.is_game_over():
                print("Game Over. It's a Tie")
                self.winner = -1
                sys.exit(0)
            self.winner = self.board.check_winner()

            if self.winner != 0:
                self.board.display_board()
                print("Player",self.winner, " Wins")
                sys.exit(0)

    def get_player_move(self):
        while True:
            try:
                move = int(input(f"Player {self.board.current_player}, choose column (0-{self.board.width-1}): "))
                if self.board.check_valid_move(move):
                    return move
                elif move == 9:
                    print("Game Stopped")
                    sys.exit(0)
                else:
                    print("Invalid Movement")
            except ValueError:
                raise ValueError("Invalid Movement")
            
    def random_move(self):
        move_attempt = random.randint(0,self.board.width)
        if self.board.check_valid_move(move_attempt):
            return move_attempt
        else:
            not_full = []
            for i in range(self.board.width):
                if self.board.data[self.board.heigth-1][i] == 0:
                    not_full.append(i)
            if len(not_full) == 0:
                print("estaba lleno y se pidió un movimiento")
                return None
            return random.choice(not_full)
            

    def auto_play(self, mode,printing):
            while not self.game_over:
                move = self.random_move()
                self.board.drop_piece(move)
                self.time = self.time + 1
                self.board.current_player = 3-self.board.current_player
                self.winner = self.board.check_winner()
                if self.winner != 0:
                    if printing:
                        print(self.board.get_board_state())
                        print("Player",self.winner, " Wins")
                    return None
                if self.is_game_over():
                    self.winner = -1
                    if printing:
                        print(self.board.get_board_state())
                        print("Tie")
                    return None
                self.game_over = self.is_game_over()


            
    def is_game_over(self):
        for cell in range(self.board.width):
            if self.board.data[self.board.heigth-1][cell] == 0:
                return False
        return True


class AI:
    def __init__(self):
        self.time = 0
        self.memory = []
    
    def run(self,length,printing):
        for iter in range(length):
            j = Game()
            j.auto_play(printing=printing,mode="random")
            #self.memory.append(j.board.get_board_state())
            del j

    


#juego = Game()
#juego.auto_play(random,printing=True)

J = AI()
J.run(length=500,printing=False)




