def parenthesis(pair):
    stack = []

    pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for ch in pair:
        if ch in "([{":
            stack.append(ch)
        else:
            if not stack:
                return False
            
            top = stack[-1]
            
            if top!= pairs[ch]:
                return False
            
            stack.pop()

    return len(stack) == 0


s = "{[()]}"
print(parenthesis(s))