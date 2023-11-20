def main():
    dna = input("Björns protein ? ")
    k = int(input("k ? "))
    for _ in range(10):
        smallest_substr, index = find_smallest_substr_with_unique_letters(dna, k)
        dna = dna[index + len(smallest_substr) :]
        print(dna)


def find_smallest_substr_with_unique_letters(string, max_length):
    # print(string)
    substrings = []
    for i, char in enumerate(string):
        current_substr = char
        for j, new_char in enumerate(string[i + 1 :]):
            if (
                new_char != current_substr[-1]
                and new_char not in current_substr
                and count(string, new_char) <= 1
            ):
                # print(count(string, new_char))
                # print(new_char)
                current_substr += new_char
                # print(current_substr)
            else:
                # print(char)
                # print(longest_substr)
                break
        if len(current_substr) > 1:
            substrings.append(current_substr)
    min = float("inf")
    min_str = ""
    for substring in substrings:
        if len(string) < min:
            min = len(string)
            min_str = substring
    # print(string, min_str)
    lowest_index = string.find(min_str)
    # highest_index = string.rfind(min_str)
    # print(lowest_index)
    return min_str, lowest_index


def count(string, char):
    sum = 0
    for character in string:
        if character == char:
            sum += 1

    return sum


# print(count("exempelfall", "e"))
# print(find_smallest_substr_with_unique_letters("exempelfall", 4))
main()
