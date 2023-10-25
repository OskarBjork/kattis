import tkinter as tk
import random


def click_handler(e):
    result_label["text"] = ""
    symbol = e.widget["text"]
    computer_symbol = random.choice(["Rock", "Paper", "Scissors"])
    computer_label["text"] = f"Computer chose: {computer_symbol}"
    dict_beats = {"Rock": "Scissors", "Paper": "Rock", "Scissors": "Paper"}
    if symbol == computer_symbol:
        result_label["text"] = "Tie"
    elif dict_beats[symbol] == computer_symbol:
        result_label["text"] = "You win"
    else:
        result_label["text"] = "You lose"


root = tk.Tk()
result_label = tk.Label(root)
result_label.pack()
computer_label = tk.Label(root)
computer_label.pack()


def main():
    root.geometry("500x500")
    b1 = tk.Button(root, text="Rock")
    b2 = tk.Button(root, text="Paper")
    b3 = tk.Button(root, text="Scissors")
    btns = [b1, b2, b3]
    for btn in btns:
        btn.pack()
        btn.bind("<Button-1>", click_handler)

    root.mainloop()


if __name__ == "__main__":
    main()
