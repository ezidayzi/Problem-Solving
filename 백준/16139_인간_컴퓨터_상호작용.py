import sys

input = sys.stdin.readline
s = list(map(str, input()))
n = int(input())

alp = [[0] * 26] * (len(s) + 1)
alp[1][ord(s[0]) - ord('a')] = 1
for i in range(1, len(s) - 1):
    alp[i] = alp[i - 1][:]
    alp[i][ord(s[i]) - ord('a')] = alp[i - 1][ord(s[i]) - ord('a')] + 1

for i in range(len(s) + 1):
    print(alp[i])

for _ in range(n):
    i = input().split()
    a = str(i[0])
    x = int(i[1])
    y = int(i[2])
    n = ord(a) - ord('a')
    if x == 0:
        print(alp[y][n])
    else:
        print(alp[y][n] - alp[x - 1][n])
