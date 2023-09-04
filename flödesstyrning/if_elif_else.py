x = 10
s = "Hej"
if x < 10 or s == "Nej":
    print("Foo")
elif s == "Hej":
    print("Bar")
else:
    print("Baz")


def grade_score(score):
    grades = {
        range(1, 60): "F",
        range(60, 70): "D",
        range(70, 80): "C",
        range(80, 90): "B",
        range(90, 101): "A",
    }

    for i in grades.keys():
        if score in i:
            return grades[i]
    return "Invalid score"


def check_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 != 0:
            return False
        return True
    return False
