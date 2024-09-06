from pickle import FALSE
import tkinter as tk
from wordle import Status, PlayResponse, play

globals().update(PlayResponse.__members__)
globals().update(Status.__members__)

TARGET = "FAVOR"
TARGET_LENGTH = 5
MAX_ATTEMPTS = 6
attempt = 0

def create_wordle_board():
    wordle_board = []
    for row in range(MAX_ATTEMPTS):
        wordle_row = []
        for col in range(TARGET_LENGTH):
            block = tk.Label(height = 3, width = 6, borderwidth = 1, relief = 'solid')
            block.grid(row = row + 1, column = col, padx = 1, pady = 1)
            wordle_row.append(block)
        wordle_board.append(wordle_row)
    return wordle_board

def validate_entry(next_char, full_text):
    if len(full_text) > TARGET_LENGTH:
        return False
    return next_char.isalpha()

def update_entry_on_labels(*args):
    cur_entry = entry_str.get()
    for i in range(TARGET_LENGTH):
        if i < len(cur_entry):
            wordleBoard[attempt][i].config(text = cur_entry[i].upper())
        else:
            wordleBoard[attempt][i].config(text = "")

    if len(cur_entry) != TARGET_LENGTH:
        guessButton.config(state = 'disabled')
    else:
        guessButton.config(state = 'normal')

def evaluateGuess():
    guess = guessBox.get()
    guess = guess.upper()
    guessBox.delete('0', tk.END)
    global attempt
    gameStats = play(TARGET, guess, attempt)

    if gameStats[GAME_STATUS] == IN_PROGRESS:
        for i in range(TARGET_LENGTH):
            color = gameStats[TALLY_RESPONSE][i].value
            wordleBoard[attempt][i].config(bg = color, text = guess[i].upper())
    else:
        endMessage(gameStats[GAME_STATUS], gameStats[MESSAGE])
        guessButton.config(state = 'disabled')
    
    attempt = gameStats[ATTEMPTS]

def exitGame(endWindow):
    endWindow.destroy()
    window.destroy()
    endWindow.update()
    window.update()

def endMessage(status, endMessage):
    endWindow = tk.Toplevel(window)
    endWindow.geometry("400x200")
    endWindow.resizable(False,False)

    title = tk.Label(endWindow, text = endMessage)
    title.pack(padx = 100, pady = 50)

    close_button = tk.Button(endWindow, text = "close game", command = lambda: exitGame(endWindow))
    close_button.pack()
    
    if status == WIN:
        endWindow.title("Congratulations!")
    else:
        endWindow.title("Game Over")


window = tk.Tk()

window.geometry("240x500")
window.title("Wordle")

title = tk.Label(window, text = "Wordle", font = ('Arial Black', 18))
title.grid(row = 0, column = 0, columnspan = 5, padx = 20, pady = 20)

wordleBoard = create_wordle_board()

entry_str = tk.StringVar()
guessBox = tk.Entry(validate = "key", validatecommand = (window.register(validate_entry), "%S", "%P"), textvariable = entry_str)
guessBox.grid(row = 7, column = 0, columnspan = 5, padx = 20, pady = 10)
entry_str.trace('w', update_entry_on_labels)

guessButton = tk.Button(state = "disabled", text = "Guess", command = evaluateGuess)
guessButton.grid(row = 8, column = 0, columnspan = 5)

window.mainloop()

