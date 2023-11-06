import tkinter


def return_handler(e):
    player[f"{e.widget._name}"] = e.widget.get()
    print(player)


def main():
    global player
    player = {
        "name": "John Doe",
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

    # Create a label for the input field
    label1 = tkinter.Label(root, text="Enter your name:")
    label2 = tkinter.Label(root, text="Enter your Strength:")
    label3 = tkinter.Label(root, text="Enter your Dexterity:")
    label4 = tkinter.Label(root, text="Enter your Constitution:")
    label5 = tkinter.Label(root, text="Enter your Intelligence:")
    label6 = tkinter.Label(root, text="Enter your Wisdom:")
    label7 = tkinter.Label(root, text="Enter your Charisma:")
    labels = [label1, label2, label3, label4, label5, label6, label7]
    for label in labels:
        label.pack()

    # Create the input field
    input_field_name = tkinter.Entry(root, name="name")
    input_field_strength = tkinter.Entry(root, name="Strength")
    input_field_dexterity = tkinter.Entry(root, name="Dexterity")
    input_field_constitution = tkinter.Entry(root, name="Constitution")
    input_field_intelligence = tkinter.Entry(root, name="Intelligence")
    input_field_wisdom = tkinter.Entry(root, name="Wisdom")
    input_field_charisma = tkinter.Entry(root, name="Charisma")

    input_fields = [
        input_field_name,
        input_field_strength,
        input_field_dexterity,
        input_field_constitution,
        input_field_intelligence,
        input_field_wisdom,
        input_field_charisma,
    ]
    for input_field in input_fields:
        input_field.pack()
        input_field.bind("<Return>", lambda e: return_handler(e))
    root.mainloop()
    # END: 6f5d4a9b3c2e


if __name__ == "__main__":
    main()
