import sys

n = int(input())
stack = []

for i in range(0, n):
    order = sys.stdin.readline().split()
    
    if order[0] == "1" :
        stack.append(order[1])
        
    elif order[0] == "2" :
        if len(stack) == 0:
            print(-1)
        else :
            top = stack.pop()
            print(top)
    elif order[0] == "3" :
        print(len(stack))
    elif order[0] == "4" :
        b = len(stack)
        if b == 0 :
            print(1)
        else :
            print(0)    
    elif order[0] == "5" :
        if len(stack) == 0:
            print(-1)
        else :
            top = stack[-1]
            print(top)