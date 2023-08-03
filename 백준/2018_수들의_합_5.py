import sys
read = sys.stdin.readline

N = int(read())

start = 1
end = 1
answer = 1
s = 1

while end < N:
    if s < N :
        end += 1
        s += end
    elif s == N :
        answer += 1
        end += 1
        s += end
    else:
        s -= start
        start += 1


print(answer)