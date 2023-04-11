from collections import deque

def solution(numbers, target):
    answer = 0
    queue = deque()
    queue.append([numbers[0], 0])
    queue.append([numbers[0] * -1, 0])

    length = len(numbers)

    while queue:
        num, index = queue.popleft()

        if index < length - 1:
            queue.append([num + numbers[index + 1], index + 1])
            queue.append([num + numbers[index + 1] * -1, index + 1])
        else:
            if target == num:
                answer += 1

    return answer