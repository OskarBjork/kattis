from math import sqrt


def pythagorean_triplet():
    for a in range(1, 1000):
        for b in range(a, 1000):
            c = 1000 - a - b
            if a**2 + b**2 == c**2:
                return a * b * c


def my_func():
    for _ in range(10):
        print("gör något")


# print(pythagorean_triplet())


def annan_funktion():
    a = 0
    b = 0
    c = 0

    while a + b + c != 1000:
        a = 0
        b += 1

        for _ in range(0, b):
            a += 1
            c = sqrt(a**2 + b**2)

            if a + b + c == 1000:
                return a * b * c


print(annan_funktion())
