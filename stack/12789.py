import sys
input = sys.stdin.readline

def acmicpc12789(queue):
    stack = []
    count = 1

    for i in queue:
        while stack and stack[-1] == count:
            stack.pop()
            count += 1

        if i == count:
            count += 1
        else:
            stack.append(i)

    while stack:
        temp = stack.pop()
        if temp == count:
            count += 1
        else:
            return False

    return True

def main():
    N = int(input().rstrip())
    command = input().rstrip()
    queue = [int(num) for num in command.split()]

    if acmicpc12789(queue):
        print("Nice")
    else:
        print("Sad")

if __name__ == "__main__":
    main()