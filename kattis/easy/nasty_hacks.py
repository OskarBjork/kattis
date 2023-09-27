def nasty_hacks():
    n = int(input())
    for _ in range(n):
        revenue_no_advertise, revenue_advertise, cost_to_advertise = tuple(
            [int(x) for x in input().split()]
        )
        if revenue_no_advertise > revenue_advertise - cost_to_advertise:
            print("do not advertise")

        elif revenue_advertise - cost_to_advertise > revenue_no_advertise:
            print("advertise")

        elif revenue_advertise - cost_to_advertise == revenue_no_advertise:
            print("does not matter")


nasty_hacks()
