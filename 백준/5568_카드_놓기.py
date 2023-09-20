n = int(input())
k = int(input())
card = []
for _ in range(n):
    card.append((input()))

card_list = []
def dfs(result, n, picked):
    if n == k:
        if result not in card_list:
            card_list.append(result)
        return

    for i in range(len(card)):
        if i not in picked:
            picked.append(i)
            dfs(result+card[i], n+1, picked)
            picked.pop()


dfs("", 0, [])
print(len(card_list))