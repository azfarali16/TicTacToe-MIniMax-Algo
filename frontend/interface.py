import tkinter as tk
from tkinter import messagebox
from game.logic import GameLogic



class Frontend:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")

        self.label = tk.Label(root, text="Welcome to Tic Tac Toe")
        self.label.pack(pady=10)

        self.start_button = tk.Button(root, text="Start Game", command=self.start_game)
        self.start_button.pack()

        self.buttons = [[None for _ in range(3)] for _ in range(3)]

        self.frame = tk.Frame(root)
        self.frame.pack()

        self.gamelogic = None

    
    def start_game(self):
        self.start_button.pack_forget()
        self.label.pack_forget()
        self.setup()


    def draw_board(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.frame,text=' ',font=('Helvetica',20),height=3, width=4,background='light gray',command=lambda row=i, col=j: self.on_click(row, col))
                self.buttons[i][j].grid(row = i , column = j)


    def on_click(self,row,col):
        if self.gamelogic.game_state.value == 1 :
            if self.gamelogic.is_legal_move(row,col):
                self.buttons[row][col].config(text=self.gamelogic.player_mark.value, state='disabled')
                self.gamelogic.make_move(row,col,self.gamelogic.player_mark)
            
            self.gamelogic.update_game_state()
            


        if self.gamelogic.game_state.value == 1 :  
            row,col = self.gamelogic.best_move()
            self.buttons[row][col].config(text=self.gamelogic.ai_mark.value, state='disabled')
            self.gamelogic.make_move(row,col,self.gamelogic.ai_mark)

            self.gamelogic.update_game_state()
        
        self.show_end_state()
        

   
    def show_end_state(self):
        if self.gamelogic.game_state == 0:
            terminal_state = self.gamelogic.end_state.value
            msg = ''
            if terminal_state == -1 :
                msg = 'X has Won!'
            if terminal_state == 1:
                msg = 'O has Won!'
            if terminal_state == 0:
                msg = 'Tie!'
            
            messagebox.showinfo("Game Ended" , msg)
            
            # for restart
            self.setup()


    def setup(self):
        #setup
        self.draw_board()
        self.gamelogic = GameLogic()
        print("Gamelogic initialised!")


def main():
    root = tk.Tk()
    frontend = Frontend(root)
    root.mainloop()

if __name__ == "__main__":
    main()
