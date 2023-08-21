def autori(s):
    return "".join([name[0] for name in s.split("-")])


print(autori("Mirko-Slavko"))
