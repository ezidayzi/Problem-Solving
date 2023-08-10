# 1253 좋다
# N개의 수 중 어떤 수가 다른 수 두개의 합으로나타남

n = int(input())
nums = list(map(int, input().split(' ')))
nums.sort()

if len(nums) == 2:
    print(0)
    exit()

ans = 0
for target in range(len(nums)):
    start = 0
    end = len(nums) - 1

    while start < end:
        if start == target:
            start = start + 1
            continue
        if end == target:
            end = end - 1
            continue

        s = nums[start] + nums[end]

        if s == nums[target]:
            ans += 1
            break
        elif s < nums[target]:
            start = start + 1
        else:
            end = end - 1
print(ans)
