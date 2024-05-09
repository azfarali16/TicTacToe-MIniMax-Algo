from game.module import Board
from game.module import Mark
from dataclasses import dataclass
from enum import Enum
import random


@dataclass
class EndState(int,Enum):
    CROSS_WINS = -1
    CIRCLE_WINS = 1
    TIE = 0


@dataclass
class GameState(int,Enum):
    Playing = 1
    Ended = 0

Score = {'X': -1, 'O': 1}



@dataclass
class GameLogic:
    def __post_init__(self):
        self.gameboard = Board()
        self.player_mark = Mark.CROSS
        self.ai_mark = self.player_mark.other
        self.game_state = GameState.Playing
        self.end_state = None
        self.cells_filled = 0 
    

    def make_move(self,row,col,mark):
        self.gameboard.set_cell(row,col,mark.value)
        self.cells_filled += 1
        # print(self.cells_filled)
        

    def is_legal_move(self,row,col)->bool:
        return self.gameboard.get_cell(row,col) == " "
        
        

    def update_game_state(self):
        """checks for either winning patterns or weather all cells are filled"""
        
        winner = self.check_winner()

        if winner:
            self.game_state = GameState.Ended
            if winner == 'X':
                self.end_state = EndState.CROSS_WINS
            elif winner == 'O':
                self.end_state = EndState.CIRCLE_WINS
            
    

        elif self.cells_filled == 9:
            # print('game ended')
            self.game_state = GameState.Ended
            self.end_state = EndState.TIE

    
    def check_winner(self):
        # Check rows
        for row in range(3):
            if (self.gameboard.get_cell(row, 0) == self.gameboard.get_cell(row, 1) == self.gameboard.get_cell(row, 2) != ' '):
                return self.gameboard.get_cell(row,0)

        # Check columns
        for col in range(3):
            if (self.gameboard.get_cell(0, col) == self.gameboard.get_cell(1, col) == self.gameboard.get_cell(2, col) != ' '):
                return self.gameboard.get_cell(0,col)

        # Check diagonals
        if (self.gameboard.get_cell(0, 0) == self.gameboard.get_cell(1, 1) == self.gameboard.get_cell(2, 2) != ' '):
            return self.gameboard.get_cell(0,0)
        
        if (self.gameboard.get_cell(0, 2) == self.gameboard.get_cell(1, 1) == self.gameboard.get_cell(2, 0) != ' '):
            return self.gameboard.get_cell(0,2)
            

        # No winner
        return None




    def ai_move(self):
        possible_moves = self.gameboard.get_possible_moves()
        random_move = random.choice(possible_moves)
        return random_move
    


    def best_move(self):
        best_score = float('-inf')
        b_move = None
        possible_moves = self.gameboard.get_possible_moves()

        for move in possible_moves:
            row,col = move
            self.gameboard.set_cell(row,col,self.ai_mark.value)
            score = self.minimax(self.gameboard,float('-inf'),float('+inf'),False)
            self.gameboard.set_cell(row,col,' ')
            if score > best_score:
                best_score = score
                b_move = move

        return b_move


   

    # def minimax(self,board,isMaximizing):
    #     winner = self.check_winner()  #eval
    #     if winner:
    #         return Score[winner]
        
    #     possible_moves = board.get_possible_moves()

    #     if not possible_moves:
    #         return 0
        
    #     if isMaximizing: #AI turn

    #         best_score = float('-inf')
    #         for move in possible_moves:
    #             row,col = move
    #             board.set_cell(row,col,self.ai_mark.value)
    #             score = self.minimax(board,not isMaximizing)
    #             board.set_cell(row,col,' ')
    #             best_score = max(score, best_score)
    #         return best_score

    #     else: #Player Turn

    #         best_score = float('inf')
    #         for move in possible_moves:
    #             row,col = move
    #             board.set_cell(row,col,self.player_mark.value)
    #             score = self.minimax(board,not isMaximizing)
    #             board.set_cell(row,col,' ')
    #             best_score = min(score, best_score)
    #         return best_score


    def minimax(self,board,alpha,beta,isMaximizing): # ALPHA - BETA PRUNING
        winner = self.check_winner()  #eval
        if winner:
            return Score[winner]
        
        possible_moves = board.get_possible_moves()

        if not possible_moves:
            return 0
        
        if isMaximizing: #AI turn

            best_score = float('-inf')
            for move in possible_moves:
                row,col = move
                board.set_cell(row,col,self.ai_mark.value)
                score = self.minimax(board,alpha,beta,not isMaximizing)
                board.set_cell(row,col,' ')
                best_score = max(score, best_score)
                alpha = max(alpha,score)
                if beta <= alpha:
                    break
            return best_score

        else: #Player Turn

            best_score = float('inf')
            for move in possible_moves:
                row,col = move
                board.set_cell(row,col,self.player_mark.value)
                score = self.minimax(board,alpha,beta,not isMaximizing)
                board.set_cell(row,col,' ')
                best_score = min(score, best_score)
                beta = min(beta,score)
                if beta <= alpha:
                    break
            return best_score
