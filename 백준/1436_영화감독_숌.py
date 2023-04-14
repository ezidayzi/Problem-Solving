# 666 종말의 수 (6이 적어도 3개 이상 연속으로 들어가는 수)
# 무식하게 구현하는 것도 방법임

n = int(input())
num = 666
cnt = 0
while True:
    if '666' in str(num):
        cnt += 1
    if cnt == n:
        break
    num += 1
print(num)