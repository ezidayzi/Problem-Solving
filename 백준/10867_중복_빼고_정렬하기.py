n = int(input())
l = list(map(int, input().split()))
ans = sorted(list(set(l)))
print(' '.join(map(str, ans)))
