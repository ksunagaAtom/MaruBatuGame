import tkinter as tk

#Frameを拡張したクラス
class MyFrame(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.turnFlag = 1
        self.turnCount = 0
        self.board = [[0,0,0],[0,0,0],[0,0,0]]

        self.b1 = tk.Button(self, text='　', command=lambda:self.key(1,0,0))
        self.b2 = tk.Button(self, text='　', command=lambda:self.key(2,0,1))
        self.b3 = tk.Button(self, text='　', command=lambda:self.key(3,0,2))
        self.b4 = tk.Button(self, text='　', command=lambda:self.key(4,1,0))
        self.b5 = tk.Button(self, text='　', command=lambda:self.key(5,1,1))
        self.b6 = tk.Button(self, text='　', command=lambda:self.key(6,1,2))
        self.b7 = tk.Button(self, text='　', command=lambda:self.key(7,2,0))
        self.b8 = tk.Button(self, text='　', command=lambda:self.key(8,2,1))
        self.b9 = tk.Button(self, text='　', command=lambda:self.key(9,2,2))
        self.message = tk.Label(self, text='メッセージ')


        self.b1.grid(row=1, column=0)
        self.b2.grid(row=1, column=1)
        self.b3.grid(row=1, column=2)
        self.b4.grid(row=2, column=0)
        self.b5.grid(row=2, column=1)
        self.b6.grid(row=2, column=2)
        self.b7.grid(row=3, column=0)
        self.b8.grid(row=3, column=1)
        self.b9.grid(row=3, column=2)
        self.message.grid(row=4, column=0, columnspan=4)

    #水平方向での勝ちの判定
    def check_board_horizontal(self,turnFlag):
        for i in range (3):
            if (self.board[i][0] == self.turnFlag) and (self.board[i][1] == self.turnFlag) and (self.board[i][2] == self.turnFlag):
                return True
        return False
    #垂直方向での勝ちの判定
    def check_board_vertical(self,turnFlag):
        for j in range (3):
            if (self.board[0][j] == self.turnFlag) and (self.board[1][j] == self.turnFlag) and (self.board[2][j] == self.turnFlag):
                return True
        return False
    #対角方向での勝ちの判定
    def check_board_diagonal(self,turnFlag):
        if (self.board[0][0] == self.turnFlag) and (self.board[1][1] == self.turnFlag) and (self.board[2][2] == self.turnFlag):
            return True
        return False
    #逆対角方向での勝ちの判定
    def check_board_inverse_diagonal(self,turnFlag):
        if (self.board[0][2] == self.turnFlag) and (self.board[1][1] == self.turnFlag) and (self.board[2][0] == self.turnFlag):
            return True
        return False
    #勝利判定メソッド    
    def is_win_simple(self,turnFlag):
        if self.check_board_horizontal(self.turnFlag):
            return True
        if self.check_board_vertical(self.turnFlag):
            return True
        if self.check_board_diagonal(self.turnFlag):
            return True
        if self.check_board_inverse_diagonal(self.turnFlag):
            return True
        return False

    def key(self,n,row,column):
        #表示文字の入れ替え
        if self.turnFlag == 1:
            text = "○"
        elif self.turnFlag == -1:
            text = "✗"
        #ボタンの表示文字切り替え
        if n == 1:
            self.b1['text'] = text
        elif n == 2:
            self.b2['text'] = text
        elif n == 3:
            self.b3['text'] = text
        elif n == 4:
            self.b4['text'] = text
        elif n == 5:
            self.b5['text'] = text
        elif n == 6:
            self.b6['text'] = text
        elif n == 7:
            self.b7['text'] = text
        elif n == 8:
            self.b8['text'] = text
        elif n == 9:
            self.b9['text'] = text

        #リストに代入
        self.board[row][column] = self.turnFlag
        print(self.board)
        
        #勝敗判定
        WoL = self.is_win_simple(self.turnFlag)
        print(WoL)

        #メッセージに勝者表示
        if WoL == True:
            if self.turnFlag == 1:
                self.message['text'] = '○の勝利'
            elif self.turnFlag == -1:
                self.message['text'] = '✗の勝利'
        
        #ターン入れ替え
        if self.turnFlag == 1:
            self.turnFlag = -1
        elif self.turnFlag == -1:
            self.turnFlag = 1


#メインプログラム
root = tk.Tk()
f = MyFrame(root)
f.pack()
root.mainloop()
