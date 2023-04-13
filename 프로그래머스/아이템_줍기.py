# 다각형의 가장 바깥쪽 테두리로 캐릭터가 이동
# 캐릭터가 아이템을 줍기 위해 이동해야하는 최단거리를 구해라

from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0

    field = [[-1] * 102 for i in range(102)]
    visited = [[1] * 102 for i in range(102)]

    for rect in rectangle:
        x1 = rect[0] * 2
        y1 = rect[1] * 2
        x2 = rect[2] * 2
        y2 = rect[3] * 2

        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                if x1 < x < x2 and y1 < y < y2:
                    field[x][y] = 0
                elif field[x][y] != 0:
                    field[x][y] = 1

    # 큐에 캐릭터 출발지점 추가 & 최단거리를 적어줄 visited 배열 선언
    q = deque()
    q.append([characterX * 2, characterY * 2])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while q:
        x, y = q.popleft()
        # 도착한 곳이 아이템이 있는 장소라면 현재의 최단거리(나누기 2)를 answer로 하고 while문을 빠져나옴
        if x == itemX * 2 and y == itemY * 2:
            answer = visited[x][y] // 2
            break
        # 아니라면 상하좌우 네 방향을 체크하면서
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            # 현재 좌표가 테두리이고 아직 방문하지 않은 곳이라면 q에 추가 후 visited 최단거리로 갱신
            if field[nx][ny] == 1 and visited[nx][ny] == 1:
                q.append([nx, ny])
                visited[nx][ny] = visited[x][y] + 1

    return answer