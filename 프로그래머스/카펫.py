def solution(brown, yellow):
    answer = []
    total = brown + yellow  # 전체 격자의 수

    # 가로 길이와 세로 길이의 조합을 확인
    for width in range(1, total + 1):
        if total % width == 0:  # 전체 격자의 수가 가로 길이로 나누어 떨어진다면
            height = total // width  # 세로 길이 계산

            if (width - 2) * (height - 2) == yellow:  # 노란색 격자의 수가 맞는지 확인
                answer.append(height)
                answer.append(width)
                break  # 가로, 세로 길이를 찾으면 반복문 종료

    return answer