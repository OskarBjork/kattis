import tkinter as tk
from PIL import Image, ImageTk, ImageSequence
import requests
from io import BytesIO

root = tk.Tk()

# Load the image from a URL
url = "https://media.tenor.com/n14-wyp-7JMAAAAC/epic-amazing.gif"
response = requests.get(url)
image = Image.open(BytesIO(response.content))

# Create a list of PhotoImage objects for each frame of the GIF
frames = []
for frame in ImageSequence.Iterator(image):
    photo = ImageTk.PhotoImage(frame)
    frames.append(photo)

# Create a label to display the animated GIF
label = tk.Label(root)
label.pack()


# Define a function to animate the GIF
def animate_gif(frame):
    photo = frames[frame]
    label.config(image=photo)
    root.after(50, animate_gif, (frame + 1) % len(frames))


# Start the animation
animate_gif(0)

root.mainloop()
