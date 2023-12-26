import re


# Ввод через пробел
def to_polish_notation(explanation):
    result = ""
    explanation = explanation.split()
    op_stack = ["#"]  # Если первым символом встретится оператор
    stack = []

    for el in explanation:
        if re.fullmatch(r"^[+-]?[0-9]+$", el):
            stack.append(int(el))
        else:
            if el == "(":
                op_stack.append(el)
            elif el == ")":
                while op_stack[-1] != "(":
                    stack.append(op_stack.pop())
                op_stack.pop()
            elif el in ("+", "-"):
                if op_stack[-1] == "(":
                    op_stack.append(el)
                else:
                    while op_stack[-1] not in ("#", "("):
                        stack.append(op_stack.pop())
                    op_stack.append(el)
            elif el in ("*", "/"):
                if op_stack[-1] == "(":
                    op_stack.append(el)
                else:
                    while op_stack[-1] not in ("#", "(", "+", "-"):
                        stack.append(op_stack.pop())
                    op_stack.append(el)

    while op_stack[-1] != "#":
        stack.append(op_stack.pop())

    result = " ".join(map(str, stack))
    return result


def calculate_polish_notation(polish: str):
    operators = ['+', '-', '/', '*']
    temp = []
    polish = polish.split()
    for el in polish:
        if el not in operators:
            temp.append(int(el))
        else:
            if el == '+':
                temp[-2] += temp[-1]
            elif el == '-':
                temp[-2] -= temp[-1]
            elif el == '*':
                temp[-2] *= temp[-1]
            elif el == '/':
                temp[-2] //= temp[-1]  # чтобы не собирать флоты
            del temp[-1]

    return temp[0]


a = to_polish_notation('( 8 + 2 * 5 ) / ( 1 + 3 * 2 - 4 )')
print(a)
print(calculate_polish_notation(a))
