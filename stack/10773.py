import sys
input = sys.stdin.readline

K = int(input())
stack = []

for i in range (0, K) :
    number = int(input().rstrip())
    if number == 0:
        stack.pop()
    else : stack.append(number)


result = 0

for i in stack :
    result += i

print(result)