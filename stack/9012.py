import sys

T = int(input())

# 스택에 들어와서 전부 반환 했을때만
# (들어오면 1 append )들어오면 pop
for i in range(T) :
    command = list(sys.stdin.readline().rstrip()) #rstrip 없이 한번 해보자 
    stack = []
    result = True
    
    for j in command :
        if j == '(' :
            stack.append(j)
        else :
            if stack:
                stack.pop()
            else:
                result = False
                break
    if stack :
        result = False
    if result :
        print("YES")
    else :
        print ("NO")
        

        

