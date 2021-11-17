import tkinter as tk
import time

#Frameを拡張したクラス
class MyFrame(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.turnFlag = 1
        self.turnCount = 0
        self.board = [[0,0,0],[0,0,0],[0,0,0]]
        self.boardRe = []
        self.boardFlag = [[True]*3,[True]*3,[True]*3]

        self.b1 = tk.Button(self, text='　', command=lambda:self.key(1,0,0))
        self.b2 = tk.Button(self, text='　', command=lambda:self.key(2,0,1))
        self.b3 = tk.Button(self, text='　', command=lambda:self.key(3,0,2))
        self.b4 = tk.Button(self, text='　', command=lambda:self.key(4,1,0))
        self.b5 = tk.Button(self, text='　', command=lambda:self.key(5,1,1))
        self.b6 = tk.Button(self, text='　', command=lambda:self.key(6,1,2))
        self.b7 = tk.Button(self, text='　', command=lambda:self.key(7,2,0))
        self.b8 = tk.Button(self, text='　', command=lambda:self.key(8,2,1))
        self.b9 = tk.Button(self, text='　', command=lambda:self.key(9,2,2))
        self.b_clear = tk.Button(self, text='C', command=lambda:self.c_key())
        self.b_replay = tk.Button(self, text='R', command=lambda:self.r_key())
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
        self.b_clear.grid(row=5, column=0)
        self.b_replay.grid(row=5, column=1)

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

    #オプション以外のボタンメソッド
    def key(self,n,row,column):
        #keyメソッドの制限
        if self.turnCount < 9 and self.boardFlag[row][column] == True:
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

            #勝敗判定
            WoL = self.is_win_simple(self.turnFlag)

            #メッセージに勝者表示
            if WoL == True:
                if self.turnFlag == 1:
                    self.message['text'] = '○の勝利'
                elif self.turnFlag == -1:
                    self.message['text'] = '✗の勝利'
                print('boardFlagをすべてFalseに')
                for i in range(len(self.boardFlag)):
                    for j in range(len(self.boardFlag[i])):
                        self.boardFlag[i][j] = False
            
            #リプレイ配列に押されたボタンと挿入
            self.boardRe.append(n)

            #ターン入れ替え
            if self.turnFlag == 1:
                self.turnFlag = -1
            elif self.turnFlag == -1:
                self.turnFlag = 1

            self.boardFlag[row][column] = False
            self.turnCount += 1
        
    #ゲームの初期化
    def c_key(self):
        self.turnFlag = 1
        self.turnCount = 0
        self.board = [[0,0,0],[0,0,0],[0,0,0]]
        self.b1['text'] = '　'
        self.b2['text'] = '　'
        self.b3['text'] = '　'
        self.b4['text'] = '　'
        self.b5['text'] = '　'
        self.b6['text'] = '　'
        self.b7['text'] = '　'
        self.b8['text'] = '　'
        self.b9['text'] = '　'
        self.boardFlag = [[True]*3,[True]*3,[True]*3]
        self.boardRe = []
        self.message['text'] = 'ゲームをリセットしました'
    """
    #ゲームのリプレイ
    def r_key(self):
        print('ボタンの文字初期化')
        self.b1['text'] = '　'
        self.b2['text'] = '　'
        self.b3['text'] = '　'
        self.b4['text'] = '　'
        self.b5['text'] = '　'
        self.b6['text'] = '　'
        self.b7['text'] = '　'
        self.b8['text'] = '　'
        self.b9['text'] = '　'
        tk.after(1)
        self.message['text'] = 'リプレイ中'

        for i in range(len(self.boardRe)):
            if i%2 == 0:
                text = "○"
            else:
                text = "✗"
            
            if i == 0:
                self.b1['text'] = text
            elif i == 1:
                self.b2['text'] = text
            elif i == 2:
                self.b3['text'] = text
            elif i == 3:
                self.b4['text'] = text
            elif i == 4:
                self.b5['text'] = text
            elif i == 5:
                self.b6['text'] = text
            elif i == 6:
                self.b7['text'] = text
            elif i == 7:
                self.b8['text'] = text
            elif i == 8:
                self.b9['text'] = text
            print('リプレイループ',i,' 表示文字は',text)
            time.sleep(0.5)
        self.message['text'] = 'リプレイ終了'
    """
        
            


#メインプログラム
root = tk.Tk()
f = MyFrame(root)
f.pack()
root.mainloop()
