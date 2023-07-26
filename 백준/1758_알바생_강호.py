# 각 손님은 강호에게 원래 주려고 생각했던 돈 - (받은 등수-1)만큼의 팁
# 민호 3
# 재필이 2
# 주현이 1

n = int(input()) # 줄서있는 사람의 수
arr = []
for _ in range(n):
    arr.append(int(input()))

arr.sort(reverse=True)

answer = 0
for i, a in enumerate(arr):
    m = a - i
    answer += m if m > 0 else 0

print(answer)