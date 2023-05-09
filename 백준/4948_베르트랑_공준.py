test_case = []
while(1):
    i = int(input())
    if i == 0: break
    test_case.append(i)

n = max(test_case) * 2

prime_list = [True] * (n +1)
prime_list[0] = False
prime_list[1] = False

for i in range(2, int(n**0.5) + 1):
    if prime_list[i]:
        for j in range(i*2, n + 1, i):
            prime_list[j] = False

for case in test_case:
    count = 0
    for i in range(case + 1, 2*case+1):
        if prime_list[i]:
            count += 1
    print(count)
