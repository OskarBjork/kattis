import tkinter
import random


def return_handler(e):
    player[f"{e.widget._name.capitalize()}"] = e.widget.get()
    if (
        player["Name"] is not None
        and player["Race"] is not None
        and player["Job"] is not None
        and sequence != 1
    ):
        print("Generating stats")
        sequence = 1

        num_of_stat_dices = {
            "Human": 4,
            "Elf": 6,
            "Dwarf": 8,
            "Orc": 10,
        }

        stats = [
            "Strength",
            "Dexterity",
            "Constitution",
            "Intelligence",
            "Wisdom",
            "Charisma",
        ]

        for stat in stats:
            player[stat] = random.randint(
                num_of_stat_dices[player["Race"]],
                6 * num_of_stat_dices[player["Race"]],
            )
            print(f"{stat}: {player[stat]}")
            label = tkinter.Label(root, text=f"{stat}: {player[stat]}")
            label.pack()

        new_attributes = ["languages", "skills", "spells"]
        for i, label in enumerate(labels):
            label.destroy()
            input_fields[i].destroy()

        for attribute in new_attributes:
            label = tkinter.Label(root, text=f"Enter your {attribute}:")
            input_field = tkinter.Entry(root, name=attribute.lower())
            label.pack()
            input_field.pack()
            input_field.bind("<Return>", lambda e: return_handler(e))
            labels.append(label)
            input_fields.append(input_field)


def main():
    global sequence
    sequence = 0
    global player
    player = {
        "Name": None,
        "Race": None,
        "Job": None,
    }

    # BEGIN: 6f5d4a9b3c2e
    global root
    root = tkinter.Tk()
    root.geometry("500x500")

    global labels
    global input_fields

    labels = []
    input_fields = []

    for stat in player.keys():
        if stat not in ("Name", "Race", "Job"):
            continue
        label = tkinter.Label(root, text=f"Enter your {stat}:")
        input_field = tkinter.Entry(root, name=stat.lower())
        label.pack()
        input_field.pack()
        input_field.bind("<Return>", lambda e: return_handler(e))
        labels.append(label)
        input_fields.append(input_field)

    root.mainloop()


if __name__ == "__main__":
    main()
