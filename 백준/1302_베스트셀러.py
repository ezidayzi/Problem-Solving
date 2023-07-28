import collections

n = int(input())
books = []
for _ in range(n):
    books.append(input())
check_book = sorted(collections.Counter(books).items(), key = lambda x : (-x[1], x[0]))


for k, v in check_book:
    print(k)
    break