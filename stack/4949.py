import sys

while True :
    command = sys.stdin.readline().rstrip()
    stack = []
    
    if command == '.': 
        break
    
    for i in command:
        if i == '(':
            stack.append(i)
        elif i == '[':
            stack.append(i)
        elif i == ')' :
            if len(stack) != 0 and stack[-1] == '(' : 
                stack.pop()
            else :
                stack.append(i)
                break
        elif i == ']': 
            if len(stack) != 0 and stack[-1] == '[' :
                stack.pop()
            else :
                stack.append(i)
                break
            
    if len(stack) == 0:
        print("yes")
    else : 
        print("no")       