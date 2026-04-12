
def evalRPN( tokens) :
    stack = []
    while tokens:
        item = tokens.pop(0)
        if item  in {"+","-","/","*"}:
            a = stack.pop(-1)
            b = stack.pop(-1)
            if item == "+":
                stack.append(a+b)
            elif item == "-":
                stack.append(b-a)
            elif item == "/":
                stack.append(int(b/a))
            else:
                stack.append(a*b)
        else:
            stack.append(int(item))
    return stack[-1]
        


        