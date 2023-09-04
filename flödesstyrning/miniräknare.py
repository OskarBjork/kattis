def evaluate_expression(expression):
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


def calculator(expression):
    parenthesis_start = 0
    parenthesis_end = 0
    for index, char in enumerate(expression):
        if char == "(":
            parenthesis_start = index + 1
        if char == ")":
            parenthesis_end = index
            string_list = list(expression)
            string_list[parenthesis_start - 1 : parenthesis_end + 1] = str(
                evaluate_expression(expression[parenthesis_start:parenthesis_end])
            )


calculator("5 + 2 + (8 - 6)")
# print(evaluate_expression("5 + 2"))
