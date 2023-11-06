import tkinter


def return_handler(e):
    player[f"{e.widget._name.capitalize()}"] = e.widget.get()
    print(player)


def main():
    global player
    player = {
        "Name": "John Doe",
        "Strength": 10,
        "Dexterity": 10,
        "Constitution": 10,
        "Intelligence": 10,
        "Wisdom": 10,
        "Charisma": 10,
    }

    # BEGIN: 6f5d4a9b3c2e
    root = tkinter.Tk()
    root.geometry("500x500")

    labels = []
    input_fields = []

    for stat in player.keys():
        label = tkinter.Label(root, text=f"Enter your {stat}:")
        input_field = tkinter.Entry(root, name=stat.lower())
        label.pack()
        input_field.pack()
        input_field.bind("<Return>", lambda e: return_handler(e))
        labels.append(label)
        input_fields.append(input_field)

    root.mainloop()
    # END: 6f5d4a9b3c2e


if __name__ == "__main__":
    main()
