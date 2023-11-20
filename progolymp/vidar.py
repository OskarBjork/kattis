class Tile:
    def __init__(self, row, column, char) -> None:
        self.row = row
        self.column = column
        self.char = char
        self.counted = False


def count_tile(tile, map, landmass):
    if tile is None or tile.char == "." or tile.counted:
        return landmass

    landmass += 1

    landmass = count_tile()


def get_tile(row, column, map):
    try:
        return map[row - 1][column - 1]
    except IndexError:
        return None


def get_adjacent_tiles(tile, map):
    try:
        north_tile = get_tile(tile.row - 1, tile.column, map)
        south_tile = get_tile(tile.row + 1, tile.column, map)
        west_tile = get_tile(tile.row, tile.column - 1, map)
        east_tile = get_tile(tile.row, tile.column + 1, map)
        return (north_tile, south_tile, west_tile, east_tile)
    except IndexError:
        return None


def calculate_landmass(map):
    for row in map:
        print(row)
    s_index = find_s(map)

    map_above = map[: s_index[0]]
    map_below = map[s_index[0] + 1 :]
    map_above.reverse()
    # map_below.reverse()
    # print(map_above)
    # print(map_below)

    landmass = 0
    connected_to_s = find_all_connected_to_s(map[s_index[0]])
    landmass += len(connected_to_s)
    safe_index_above = connected_to_s
    safe_index_below = connected_to_s
    # print(f"Map above: {map_above}")
    counted_landmass_points = []
    for i, row in enumerate(map_above):
        new_safe_indexes = []
        for j, char in enumerate(row):
            # print(safe_index_below)
            if char == "#" and (j in safe_index_below) and j not in new_safe_indexes:
                # print(i, j)
                landmass += 1
                # print((len(map_above) - i, j + 1))
                counted_landmass_points.append((len(map_above) - i, j + 1))
                new_safe_indexes.append(j)
                new_connections = find_all_connected_to_index(row, j)
                # print("new connections: ", new_connections)
                # print(j)
                for new_connected in new_connections:
                    if new_connected not in new_safe_indexes:
                        landmass += 1
                        # print((len(map_above) - i, new_connected + 1))
                        counted_landmass_points.append(
                            (len(map_above) - i, new_connected + 1)
                        )
                        new_safe_indexes.append(new_connected)
        safe_index_below = new_safe_indexes

        # try:
        #     index = 0
        #     rows_before = map[: s_index[0] + i]
        #     new_landmass = 1
        #     while new_landmass != 0:
        #         current_row = rows_before[index]
        #         new_landmass = find_leftovers(
        #             current_row, new_safe_indexes, counted_landmass_points, i
        #         )
        #         landmass += new_landmass
        # except IndexError:
        #     continue

    # print("Map Below: ", map_below)

    for i, row in enumerate(map_below):
        new_safe_indexes = []
        for j, char in enumerate(row):
            # print(safe_index_above)
            if char == "#" and (j in safe_index_above) and j not in new_safe_indexes:
                # print(i, j)
                landmass += 1
                # print((len(map_above) + 2 + i, j + 1))
                counted_landmass_points.append((len(map_above) + 2 + i, j + 1))
                new_safe_indexes.append(j)
                new_connections = find_all_connected_to_index(row, j)
                # print("new connections: ", new_connections)
                # print(j)
                for new_connected in new_connections:
                    if new_connected not in new_safe_indexes:
                        landmass += 1
                        # print((len(map_above) + 2 + i, new_connected + 1))
                        counted_landmass_points.append(
                            (len(map_above) + 2 + i, new_connected + 1)
                        )
                        new_safe_indexes.append(new_connected)
        safe_index_above = new_safe_indexes

        # try:
        #     index = 0
        #     rows_after = map[: len(map_above) + 1 + i]
        #     new_landmass = 1
        #     while new_landmass != 0:
        #         current_row = rows_after[index]
        #         new_landmass = find_leftovers(
        #             current_row, new_safe_indexes, counted_landmass_points, i
        #         )
        #         landmass += new_landmass
        # except IndexError:
        #     continue

    return landmass


def find_leftovers(row, indexes, counted_points, row_num):
    new_landmass = 0
    for i in indexes:
        if row[i] == "#" and not (row_num, i) in counted_points:
            new_landmass += 1
    return new_landmass


map = ["######", "#....#"]


def find_all_connected_to_index(row, index):
    connected = []
    # print("lol")
    # print(row)
    # print(row[:index])
    # print(row[index:])
    row = row[:index] + "T" + row[index + 1 :]
    # print(row)
    for i, char in enumerate(row):
        if i == index:
            # connected.append(i)
            continue
        stop = 0
        # print(char + ": ")
        if char == "#":
            # print("right")
            front = row[i + 1 :]
            for new_index, new_char in enumerate(front):
                # print(new_char)
                if new_char == ".":
                    break
                if new_char == "T":
                    connected.append(i)
                    stop = 1
                    break
            if stop == 1:
                continue

            # print("left")
            # print(row[:i])
            behind = row[:i][::-1]
            for new_index, new_char in enumerate(behind):
                # print(new_char)
                if new_char == ".":
                    break
                if new_char == "T":
                    connected.append(i)

    return connected


def find_all_connected_to_s(row):
    # print(row)
    connected = []
    for i, char in enumerate(row):
        if char == "S":
            connected.append(i)
            continue
        stop = 0
        # print(char + ": ")
        if char == "#":
            # print("right")
            for new_char in row[i + 1 :]:
                # print(new_char)
                if new_char == ".":
                    break
                if new_char == "S":
                    connected.append(i)
                    stop = 1
                    break
            if stop == 1:
                continue

            # print("left")
            # print(row[:i])
            for new_char in row[:i][::-1]:
                # print(new_char)
                if new_char == ".":
                    break
                if new_char == "S":
                    connected.append(i)

    return connected


def find_s(map):
    for i, row in enumerate(map):
        for j, column in enumerate(row):
            if column == "S":
                return (i, j)


def main():
    rows = int(input())
    columns = int(input())
    num_of_changes = int(input())
    list_of_changes = []
    map = []
    for row in range(rows):
        map.append(input())
    if num_of_changes != 0:
        for i in range(num_of_changes):
            soy = input()
            i, j = int(soy[0]), int(soy[2])
            list_of_changes.append((i, j))

    landmass = calculate_landmass(map)
    print(landmass)

    # print(len(list_of_changes))
    # print(list_of_changes)

    for change in list_of_changes:
        i, j = change
        # print(i)
        # print(j)
        # print(change)
        # print(map[i - 1])
        map[i - 1] = map[i - 1][: j - 1] + "#" + map[i - 1][j:]
        # print(map[i - 1])
        print(calculate_landmass(map))

    pass


main()
# print(find_all_connected_to_s("#.S..."))
