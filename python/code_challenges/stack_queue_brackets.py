from data_structures.stack.stack import Stack

def multi_bracket_validation(str):
    brackets = Stack()
    bracket_dictionary = {
        '}': '{',
        ']': '[',
        ')': '('
    }

    for char in str:
        if char in bracket_dictionary.values():
            brackets.push(char)
        if char in bracket_dictionary.keys() and not brackets.is_empty():
            open_bracket = brackets.pop()
            if open_bracket != bracket_dictionary[char]:
                return False
    if not brackets.is_empty():
        return False
    return True

