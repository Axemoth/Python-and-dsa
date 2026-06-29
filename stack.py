def build(word):

    stack = []

    for ch in word:

        if ch == "#":

            if stack:
                stack.pop()

        else:
            stack.append(ch)

    return "".join(stack)


s1 = input()
s2 = input()

if build(s1) == build(s2):
    print("MATCH")
else:
    print("NOT MATCH")