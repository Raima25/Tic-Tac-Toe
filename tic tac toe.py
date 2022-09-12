from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Tic Tac Toe")

click = True
c = 0

button_1 = Button(root, width = 3, height = 1, padx = 5, pady = 5, text = " ", font = ("Times New Roman", 25), bg = "Silver", command = lambda: b_click(button_1))
button_1.grid(row = 0, column = 0)

button_2 = Button(root, width = 3, height = 1, padx = 5, pady = 5, text = " ", font = ("Times New Roman", 25), bg = "Silver", command = lambda: b_click(button_2))
button_2.grid(row = 0, column = 1)

button_3 = Button(root, width = 3, height = 1, padx = 5, pady = 5, text = " ", font = ("Times New Roman", 25), bg = "Silver", command = lambda: b_click(button_3))
button_3.grid(row = 0, column = 2)

button_4 = Button(root, width = 3, height = 1, padx = 5, pady = 5, text = " ", font = ("Times New Roman", 25), bg = "Silver", command = lambda: b_click(button_4))
button_4.grid(row = 1, column = 0)

button_5 = Button(root, width = 3, height = 1, padx = 5, pady = 5, text = " ", font = ("Times New Roman", 25), bg = "Silver", command = lambda: b_click(button_5))
button_5.grid(row = 1, column = 1)

button_6 = Button(root, width = 3, height = 1, padx = 5, pady = 5, text = " ", font = ("Times New Roman", 25), bg = "Silver", command = lambda: b_click(button_6))
button_6.grid(row = 1, column = 2)

button_7 = Button(root, width = 3, height = 1, padx = 5, pady = 5, text = " ", font = ("Times New Roman", 25), bg = "Silver", command = lambda: b_click(button_7))
button_7.grid(row = 2, column = 0)

button_8 = Button(root, width = 3, height = 1, padx = 5, pady = 5, text = " ", font = ("Times New Roman", 25), bg = "Silver", command = lambda: b_click(button_8))
button_8.grid(row = 2, column = 1)

button_9 = Button(root, width = 3, height = 1, padx = 5, pady = 5, text = " ", font = ("Times New Roman", 25), bg = "Silver", command = lambda: b_click(button_9))
button_9.grid(row = 2, column = 2)

def b_click(b):
    global click, c
    if b["text"] == " " and click == True:
        b["text"] = "O"
        win = CheckWin()
        c += 1
        click = False
    elif b["text"] == " " and click == False:
        b["text"] = "X"
        win = CheckWin()
        c += 1
        click = True
    else:
        messagebox.showerror("Tic Tac Toe", "Already selected! Pick another box.")
    if win == "O":
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!PLAYER 1 WINS!")
    elif win == "X":
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!PLAYER 2 WINS!")
    elif c == 9 and win == "Not yet":
        messagebox.showinfo("Tic Tac Toe", "MATCH TIED!")

def disable_buttons():
    button_1.config(state=DISABLED)
    button_2.config(state=DISABLED)
    button_3.config(state=DISABLED)
    button_4.config(state=DISABLED)
    button_5.config(state=DISABLED)
    button_6.config(state=DISABLED)
    button_7.config(state=DISABLED)
    button_8.config(state=DISABLED)
    button_9.config(state=DISABLED)

def CheckWin():
    win1 = "O"
    win2 = "X"
    nowin = "Not yet"
    if button_1["text"] == "O" and button_2["text"] == "O" and button_3["text"] == "O":
        button_1.config(bg = "Red")
        button_2.config(bg = "Red")
        button_3.config(bg = "Red")
        disable_buttons()
        return win1

    elif button_1["text"] == "O" and button_4["text"] == "O" and button_7["text"] == "O":
        button_1.config(bg = "Red")
        button_4.config(bg = "Red")
        button_7.config(bg = "Red")
        disable_buttons()
        return win1
    
    elif button_1["text"] == "O" and button_5["text"] == "O" and button_9["text"] == "O":
        button_1.config(bg = "Red")
        button_5.config(bg = "Red")
        button_9.config(bg = "Red")
        disable_buttons()
        return win1

    elif button_2["text"] == "O" and button_5["text"] == "O" and button_8["text"] == "O":
        button_2.config(bg = "Red")
        button_5.config(bg = "Red")
        button_8.config(bg = "Red")
        disable_buttons()
        return win1

    elif button_3["text"] == "O" and button_6["text"] == "O" and button_9["text"] == "O":
        button_3.config(bg = "Red")
        button_6.config(bg = "Red")
        button_9.config(bg = "Red")
        disable_buttons()
        return win1

    elif button_4["text"] == "O" and button_5["text"] == "O" and button_6["text"] == "O":
        button_4.config(bg = "Red")
        button_5.config(bg = "Red")
        button_6.config(bg = "Red")
        disable_buttons()
        return win1

    elif button_7["text"] == "O" and button_8["text"] == "O" and button_9["text"] == "O":
        button_7.config(bg = "Red")
        button_8.config(bg = "Red")
        button_9.config(bg = "Red")
        disable_buttons()
        return win1

    elif button_3["text"] == "O" and button_5["text"] == "O" and button_7["text"] == "O":
        button_3.config(bg = "Red")
        button_5.config(bg = "Red")
        button_7.config(bg = "Red")
        disable_buttons()
        return win1

    elif button_1["text"] == "X" and button_2["text"] == "X" and button_3["text"] == "X":
        button_1.config(bg = "Red")
        button_2.config(bg = "Red")
        button_3.config(bg = "Red")
        disable_buttons()
        return win2

    elif button_1["text"] == "X" and button_4["text"] == "X" and button_7["text"] == "X":
        button_1.config(bg = "Red")
        button_4.config(bg = "Red")
        button_7.config(bg = "Red")
        disable_buttons()
        return win2

    elif button_1["text"] == "X" and button_5["text"] == "X" and button_9["text"] == "X":
        button_1.config(bg = "Red")
        button_5.config(bg = "Red")
        button_9.config(bg = "Red")
        disable_buttons()
        return win2

    elif button_2["text"] == "X" and button_5["text"] == "X" and button_8["text"] == "X":
        button_2.config(bg = "Red")
        button_5.config(bg = "Red")
        button_8.config(bg = "Red")
        disable_buttons()
        return win2

    elif button_3["text"] == "X" and button_6["text"] == "X" and button_9["text"] == "X":
        button_3.config(bg = "Red")
        button_6.config(bg = "Red")
        button_9.config(bg = "Red")
        disable_buttons()
        return win2

    elif button_4["text"] == "X" and button_5["text"] == "X" and button_6["text"] == "X":
        button_4.config(bg = "Red")
        button_5.config(bg = "Red")
        button_6.config(bg = "Red")
        disable_buttons()
        return win2

    elif button_7["text"] == "X" and button_8["text"] == "X" and button_9["text"] == "X":
        button_7.config(bg = "Red")
        button_8.config(bg = "Red")
        button_9.config(bg = "Red")
        disable_buttons()
        return win2

    elif button_3["text"] == "X" and button_5["text"] == "X" and button_7["text"] == "X":
        button_3.config(bg = "Red")
        button_5.config(bg = "Red")
        button_7.config(bg = "Red")
        disable_buttons()
        return win2
    
    else:
        return nowin

root.mainloop()
