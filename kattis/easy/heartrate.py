def heart_rate():
    n = int(input())
    for _ in range(n):
        b, p = tuple([int(x) for x in (input().split())])
        bpm = (60 * b) / p


heart_rate()
