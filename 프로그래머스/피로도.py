# 최소 필요 피로도
# 소모 피로도
# 최소 필요 피로도
# [최소 필요 피로도, 소모 피로도]
# 배열을 돌면서 남은 피로도 >= 최소 필요도면 진입 가능
# 탐험할 수 있는 최대 던전 수?
from itertools import permutations


def solution(k, dungeons):
    answer = -1

    def explore(k, dungeons):
        count = 0
        for i, dungeon in enumerate(dungeons):
            if dungeon[0] <= k:
                k -= dungeon[1]
                count += 1

        return count

    index_array = list(permutations([i for i in range(len(dungeons))], len(dungeons)))

    for indexs in index_array:
        arr = []
        for i in indexs:
            arr.append(dungeons[i])
        answer = max(answer, explore(k, arr))

    return answer