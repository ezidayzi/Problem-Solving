# 회의실 배정
# 한개의 회의실 N개의 회의
# 각 회의가 겹치지 않게 하면서 회의실을 사용할 수 있는 회의의 최대 개수?
import sys
read = sys.stdin.readline

N = int(read())
time = [list(map(int, read().split())) for _ in range(N)]
time.sort(key = lambda x: [x[1], x[0]])
end_time = 0

answer = 0
for t in time:
   if end_time <= t[0] :
        answer += 1
        end_time = t[1]

print(answer)