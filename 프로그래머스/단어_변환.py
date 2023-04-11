# 두 개의 단어 begin, target / 단어 집합 words
# 1. 한 번에 한 개의 알파벳만 바꿀 수 있습니다.
# 2. words에 있는 단어로만 변환할 수 있습니다.
# 최소 몇 단계의 과정을 거쳐 begin을 target으로 변환할 수 있는 가?
# hhh -> hih -> hii -> iii 중복 문자 있을 수 있다 유의

from collections import deque


def solution(begin, target, words):
    answer = 0
    now = begin
    visited = [False] * len(words)

    def bfs(wrd):
        queue = deque()
        queue.append([wrd, 0])
        cnt = 0

        while queue:
            w, cnt = queue.popleft()
            if w == target:
                return cnt

            for j in range(len(words)):
                count = 0

                if not visited[j]:
                    for i in range(len(words[j])):
                        if w[i] == words[j][i]:
                            count += 1

                    if count == len(w) - 1:
                        visited[j] = True
                        queue.append([words[j], cnt + 1])

        return 0

    answer = bfs(begin)
    return answer