#못풀었어요

def right(s):
    stack=[]
    for char in s:
        if char in '([{':
            stack.append(char)
        else:
            if not stack:
                return False
            if char