def main():
    rows = int(input("n ? "))
    columns = int(input("m ? "))

    map = []
    for i in range(rows):
        map.append(input(f"Rad {i+1} ? "))

    secret_message = ""

    for i, row in enumerate(map):
        for j, char in enumerate(row):
            if char != ".":
                secret_message += char

    print("Svar:", secret_message)


main()
