print("===valid_parentheses===")
def is_valid(numbers):
    stack = []
    matching = { ')':'(','}':'{',']':'['}
    for char in numbers:
        if char in matching:
            if not stack:
                return False
            if stack[-1] != matching[char]:
                return False
            stack.pop()
        else:
           stack.append(char)

    return len(stack) == 0

print(is_valid("()"))        # Expected: True
print(is_valid("()[]{}"))    # Expected: True
print(is_valid("(]"))        # Expected: False
print(is_valid("([)]"))      # Expected: False
print(is_valid("{[]}"))      # Expected: True


