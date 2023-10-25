import tkinter as tk
import random
from PIL import Image, ImageTk, ImageSequence
import requests
from io import BytesIO


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
url = "https://media.tenor.com/n14-wyp-7JMAAAAC/epic-amazing.gif"
response = requests.get(url)


image = Image.open(BytesIO(response.content))
photo = ImageTk.PhotoImage(image)
label = tk.Label(root, image=photo)
label.pack()


result_label = tk.Label(root)
result_label.pack()
computer_label = tk.Label(root)
computer_label.pack()
frames = []
for frame in ImageSequence.Iterator(image):
    photo = ImageTk.PhotoImage(frame)
    frames.append(photo)


# Define a function to animate the GIF
def animate_gif(frame):
    photo = frames[frame]
    label.config(image=photo)
    root.after(50, animate_gif, (frame + 1) % len(frames))


# Start the animation
animate_gif(0)


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
