import random
import time
from tkinter import Tk, Button, DISABLED, messagebox

def close_window(self):
    root.destroy()
# Show the symbol
def show_symbol(x, y):
    global first
    global previousX, previousY
    global moves
    global pairs
    buttons[x, y]['text'] = button_symbols[x, y]
    buttons[x, y].update_idletasks()
    if first:
        previousX = x
        previousY = y
        first = False
        moves = moves + 1
    elif previousX != x or previousY != y:
        if buttons[previousX, previousY]['text'] != buttons[x, y]['text']:
            time.sleep(0.5)
            buttons[previousX, previousY]['text'] = ''
            buttons[x, y]['text'] = ''
        else:
            buttons[previousX, previousY]['command'] = DISABLED
            buttons[x, y]['command'] = DISABLED
            pairs = pairs + 1
            if pairs == len(buttons) / 2:
               print('Number of moves: ' + str(moves))
        first = True





root = Tk()
root.title('Matchmaker')
root.resizable(width=False, height=False)

# Make some variables
buttons = {}
first = True
previousX = 0
previousY = 0
moves = 0
pairs = 0

# Add the symbols
button_symbols = {}
symbols = [u'\ud83d\udc99', u'\ud83d\udc99', u'\u2606', u'\u2606', u'\u2660', u'\u2660',
           u'\u2663', u'\u2663', u'\u25cf', u'\u25cf', u'\u25a1', u'\u25a1',
           u'\u25b2', u'\u25b2', u'\u25c8', u'\u25c8'
          ]
# Shuffle the symbols
random.shuffle(symbols)

# Build the grid
for x in range(4):
    for y in range(4):
        button = Button(command=lambda x=x, y=y: show_symbol(x, y), width=5, height=3, border=2)
        button.grid(column=x, row=y,padx=15,pady=20)
        buttons[x, y] = button
        button_symbols[x, y] = symbols.pop()

root.mainloop()
