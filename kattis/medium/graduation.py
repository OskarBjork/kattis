class Student:
    def __init__(self, graduate_class, hat_color="blue"):
        self.graduate_class = graduate_class
        self.hat = hat_color


def graduation():
    data = input("N M K: ").split(" ")
    lines = int(data[0])
    columns = int(data[1])
    classes = int(data[2])
    print(lines, columns, classes)

    positions = []
    for i in range(lines):
        column = list(input("Order of students classes: "))
        positions.append(column)

    print(positions)

    students_arr = []

    try:
        for i, line in enumerate(positions):
            print(i, line)
            students_arr.append([])
            for j, column in enumerate(line):
                print(j, column)
                students_arr[i].append(positions[i][j])
    except IndexError:
        print(students_arr)

    print(students_arr)

    pass


# graduation()

my_list = ["1", "2", "three", "__hej__", "__init__"]
print([x for x in my_list if not x.startswith("__")])
