### Tic-Tac-Toe Game ###
'''
1. create a list of lists for tic tac toe board
2. Make two choices i.e. "X" / "O"
3. Winner: all rows/columns/diagnol same
4. If once a position is filled it cannot be changed

'''
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Tic Tac Toe")
root.geometry("400x400")
root.resizable(False,False)

current_player = "X"
board = [""] * 9
buttons = []

def check_winner():
    win_combos = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]
    for a,b,c in win_combos:
        if board[a] == board[b] == board[c] != "":
            for i in (a,b,c):
                buttons[i].config(bg="lightgreen")
            return True
    return False

def reset_board():
    global board,current_player
    board = [""] * 9
    current_player = "X"
    for button in buttons:
        button.config(text="", state="normal", bg="#f0f0f0")

def on_click(index):
    global current_player
    if board[index] == "":
        board[index] = current_player
        buttons[index].config(text=current_player, state="disabled")
        if check_winner():
            messagebox.showinfo("Game Over", f"Player {current_player} wins!")
            reset_board()
        elif "" not in board:
            messagebox.showinfo("Game Over", "It's a draw")
            reset_board()
        else:
            current_player = "O" if current_player == "X" else "X"

frame = tk.Frame(root)
frame.pack(pady = 30)

for i in range(9):
    button = tk.Button(frame, text="", font=("Arial",24), width=5, height=2,
                       command=lambda i=i: on_click(i), bg="#f0f0f0", relief="ridge")
    button.grid(row = i//3, column = i%3, padx=5, pady=5)
    buttons.append(button)

#tk.Button(root, text = "Restart", command = reset_board(), font=("Arial,12"), bg="#ddd").pack(pady=10)

root.mainloop()