def faktor():
    A, I = tuple([int(x) for x in (input().split())])
    print(A * (I - 1) + 1)


faktor()
