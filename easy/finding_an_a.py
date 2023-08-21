def find_a(s):
    for i, char in enumerate(s):
        if char == "a":
            return s[i::]


print(find_a("art"))
