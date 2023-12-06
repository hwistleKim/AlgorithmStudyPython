import sys
input = sys.stdin.readline

N = int(input().rstrip())
flag = True

command  = input().rstrip()
queue = [int(num) for num in command.split()]
stack = []
count = 1
for i in queue :
    if len(stack) != 0 :
        while stack[-1] == count:
            stack.pop()
            count = count + 1
            if len(stack) == 0: break
    if i == count:
        count = count + 1
    else :
        stack.append(i)
    
while len(stack) != 0:
    temp = stack.pop()
    if temp == count:
        count = count + 1
    else :
        flag = False
        break

if flag :
    print ("Nice")
else :
    print ("Sad")
