def solution(sizes):
    answer = 0
    width = 0
    height = 0
    for size in sizes:
        size.sort()
        width = max(width, size[0])
        height = max(height, size[1])
    answer = width * height
    return answer