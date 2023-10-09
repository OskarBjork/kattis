# A2B1A2B2A1A2A2A2
# A2B2A1B2A2B1A2B2A1B2A1A1B1A1A2


def basketball():
    game_record = input()
    scores = {"A": 0, "B": 0}
    current_player = ""
    win_by_2 = False
    for char in game_record:
        if char in ("A", "B"):
            current_player = char
        else:
            scores[current_player] += int(char)

        if scores["A"] == 10 and scores["B"] == 10:
            win_by_2 = True

        if win_by_2:
            continue

        if scores["A"] >= 11:
            return "A"
        elif scores["B"] >= 11:
            return "B"

    return "A" if scores["A"] > scores["B"] else "B"


print(basketball())
