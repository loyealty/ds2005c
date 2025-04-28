def is_vaild_brackets(expression : str) -> bool:
    stack = []
    brackeets = {')':'(', '}':'{', ']':'['}

    for letter in expression:
        if letter in brackeets.values():
            stack.append(letter)
        if letter in brackeets.keys():
            if not stack or stack.pop() != brackeets[letter]:
                return False
    return not stack

print(is_vaild_brackets("([2+3])"))
print(is_vaild_brackets("(2+{3*9}"))
print(is_vaild_brackets("(2+(3*9)"))
print(is_vaild_brackets(")2+(3*9)("))