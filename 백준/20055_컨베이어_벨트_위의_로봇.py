# 길이가 N인 컨베이어 벨트
# 길이가 2N인 벨트가 컨베이어 벨트를 위아래로 감싸고 있음
# i번 칸의 내구도는 Ai
# 1번칸 = 올리는 위치
# N번칸 = 내리는 위치
# 1번칸에만 로봇을 올릴 수 있고 N에 도달하면 로봇을 내림
# 로봇은 스스로 이동 가능, 로봇을 올리는 위치에 올리거나 어떤 칸으로 이동하면 내구도는 1감

# 로봇이 이동하기 위해서는 이동하려는 칸에 로봇이 없으며 내구도가 1이상 남아있어야함
# 내구도가 0인 칸의 개수가 K개 이상이라면 과정 종료
# 종료되었을 때 몇번째 단게가 진행중이었는지

from collections import deque

n, k = map(int, input().split())
belt = deque(list(map(int, input().split())))
robots = deque([False] * 2 * n)
step = 1

while True:
    # 로봇과 함께 한칸 회전
    p = belt.pop()
    r = robots.pop()
    belt.appendleft(p)
    robots.appendleft(r)

    # 내리는 칸에서 로봇 내림
    if robots[n - 1]:
        robots[n - 1] = False

    # 로봇을 회전하는 방향으로 한칸씩 이동
    # 이동하려는 칸에 로봇이 없으며 내구도가 1이상
    for i in range(n-2, -1, - 1):
        if robots[i] == True and belt[i + 1] >= 1 and not robots[i + 1]:
            robots[i] = False
            robots[i + 1] = True
            belt[i + 1] -= 1

    # 내리는 칸에서 로봇 내림
    robots[-1] = False

    # 올리는 위치에 있는 칸의 내구도가 0이 아니면 로봇 올림
    if belt[0] != 0:
        robots[0] = True
        belt[0] -= 1

    if belt.count(0) >= k:
        break
    step += 1
print(step)