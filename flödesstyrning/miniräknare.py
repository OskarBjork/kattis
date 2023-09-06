def evaluate_expression(expression):
    print(expression)
    for char in expression:
        if char == "+":
            return int(expression[0]) + int(expression[-1])
        elif char == "-":
            return int(expression[0]) - int(expression[-1])
        elif char == "*":
            return int(expression[0]) * int(expression[-1])
        elif char == "/":
            return int(expression[0]) / int(expression[-1])
    pass


def replace_string(string, replace_string, start, end):
    string_list = list(string)
    string_list[start:end] = replace_string
    return "".join(string_list)


def calculator(expression):
    print(expression)
    parenthesis_start = 0
    parenthesis_end = 0
    for index, char in enumerate(expression):
        if char == "(":
            parenthesis_start = index + 1
        elif char == ")":
            parenthesis_end = index
            string_list = list(expression)
            string_list[parenthesis_start - 1 : parenthesis_end + 1] = str(
                evaluate_expression(expression[parenthesis_start:parenthesis_end])
            )
        elif char == "+":
            num_1 = expression[index - 2]
            num_2 = expression[index + 2]

            expression_start = index - 2
            expression_end = index + 2
            if num_1 in "()" or num_2 in "()":
                calculator()
            calculator(
                replace_string(
                    expression,
                    str(int(num_1) + int(num_2)),
                    expression_start,
                    expression_end + 1,
                )
            )


# print(replace_string("Hello world", "ko", 1, 1))

calculator("5 + 2 + (8 - 6)")
# print(evaluate_expression("5 + 2"))
