import tkinter as tk
from sudoku import Solver
import numpy as np

def pick_one():
    with open('samples.txt', 'r') as file:
        out = file.readlines()

    pick = np.random.randint(len(out))

    return [list(map(lambda i: int(i), y)) for y in [x.split(', ') for x in out[pick].strip()[2:-2].split('], [')]]

class Window():
    size = 400
    def __init__(self, master):
        self.root = master
        self.main_window()
        self.inp = []

    def main_window(self):
        button_font = ('Cooper black', 12)

        self.frame_title = tk.Frame(self.root)
        self.frame_title.pack(fill='x',padx=10, pady=5)
        
        self.frame_cells = tk.Frame(self.root, bg='gray', cursor='tcross')
        self.frame_cells.pack(padx=10)

        self.frame_text = tk.Frame(self.root)
        self.frame_text.pack(fill='x')

        self.frame_buttons = tk.Frame(self.root, bg='green', cursor='target')
        self.frame_buttons.pack(fill='x', padx=10, pady=5)

        self.label_title = tk.Label(self.frame_title, text='SUDOKU SOLVER', font=('Showcard gothic', 25))
        self.label_title.pack()

        self.label_text = tk.Label(self.frame_text, text='')
        self.label_text.pack()
        
        self.squares = []
        c = ['#ccffcc','#b3ffff']
        color_used = c[0]
        vcmd = self.root.register(self.callback)
        for i in range(9):
            temp = []
            if i%3 == 0:
                color_used = self.swap(color_used, c)
            for j in range(9):
                if j%3 == 0 and j!= 0:
                    color_used = self.swap(color_used, c)
                e = tk.Entry(self.frame_cells, width=2, justify='center', bg=color_used, cursor='tcross', font=('Verdana Pro Black', 14),
                 validate='key', validatecommand=(vcmd, "%P"))
                e.grid(row=i, column=j, ipadx=4, ipady=5, padx=1, pady=1)
                temp.append(e)
            self.squares.append(temp)

        self.frame_buttons.grid_columnconfigure(0, weight=1)
        self.frame_buttons.grid_columnconfigure(1, weight=1)
        self.frame_buttons.grid_columnconfigure(2, weight=1)

        self.button_solve = tk.Button(self.frame_buttons, width=5, cursor='target', text='Solve', font=button_font, command=self.start_solving)
        # self.button_solve.pack(side='right', fill='x', expand=True)
        self.button_solve.grid(row=0, column=2, sticky='ew')

        self.button_exit = tk.Button(self.frame_buttons, width=5, cursor='target', text='Exit', font=button_font, command=lambda: self.root.quit())
        # self.button_exit.pack(side='left', fill='x', expand=True)
        self.button_exit.grid(row=0, column=0, sticky='ew')

        self.button_clear = tk.Button(self.frame_buttons, width=5, cursor='target', text='Clear', font=button_font, command=self.clear_e)
        # self.button_clear.pack(side='left', fill='x', expand=True)
        self.button_clear.grid(row=0, column=1, sticky='ew')

        self.button_test = tk.Button(self.frame_buttons, text='Testing board', cursor='target', font=button_font, command=lambda: self.fill_board(pick_one(), colors=False))
        self.button_test.grid(row=1, column=0, columnspan=3, sticky='we')

    def clear_e(self):
        for i in range(len(self.squares)):
            for j in range(len(self.squares[0])):
                self.squares[i][j].delete(0,'end')
                self.squares[i][j].config(fg='black')

        self.label_text.config(text='')

    def start_solving(self):
        boa = []
        self.inp = []
        for i in range(len(self.squares)):
            row = []
            for j in range(len(self.squares[0])):
                if self.squares[i][j].get() == "":
                    row.append(0)
                else:
                    self.inp.append((i,j))
                    row.append(int(self.squares[i][j].get()))
            boa.append(row)
        print(boa)
        self.s = Solver(boa)
        if [list(row) for row in self.s.board_orig] == self.s.board and any([(0 in set(row)) for row in boa]):
            self.label_text.config(text="Board can't be solved.", fg='red')
        else:
            self.fill_board(self.s.board)
            self.label_text.config(text="Sudoku solved!", fg='green')

    def fill_board(self, new_board, colors=True):
        self.clear_e()
        for i in range(len(new_board)):
            for j in range(len(new_board[0])):
                self.squares[i][j].insert(0, str(new_board[i][j]))
                if colors and (i, j) not in set(self.inp):
                    self.squares[i][j].config(fg='#bfbfbf')

    def callback(self, P):
        if P.isdigit() or P == "":
            if (len(P) == 1 or len(P)==0) and P!="0":
                return True
            else:
                return False
        else:
            return False

    @staticmethod
    def swap(act, opt):
        ind = opt.index(act)

        if ind < len(opt)-1:
            return opt[ind+1]
        else:
            return opt[0]
    

WIDTH, HEIGHT = 380, 450

root = tk.Tk()
root.geometry(f"+{int(root.winfo_screenwidth()/2-WIDTH/2)}+{int(root.winfo_screenheight()/2-HEIGHT/2)}")
root.resizable(False, False)
root.title("Sudoku solver")

app = Window(root)

tk.mainloop()