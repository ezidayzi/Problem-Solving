# 블루레이 -> 총 N개의 강의
# 강의의 순서가 바뀌면 안됨 i번 강의와 j번 강의를 불로레이에 녹화하려면 i~j 사이의 모든 강의도 녹화해야함
# M개의 블로레이에 모든 동영상 녹화
# 블루레이의 크기를 최소화 하려고함, M개의 블로레이는 모두 같은크기여야함
# 가능한 블루레이의 크기 중 최소

n, m = list(map(int, input().split()))
lecture = list(map(int, input().split()))

start = max(lecture)
end = sum(lecture)
ans = end

while start <= end:
    lay = (start + end) // 2

    count = 0
    s = 0
    for l in lecture:
        if s + l <= lay:
            s += l
        else:
            count += 1
            s = l

    if count < m:
        end = lay - 1
        ans = min(ans, lay)
    else:
        start = lay + 1


print(ans)
