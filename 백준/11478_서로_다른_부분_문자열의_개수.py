words = input()
part_word = set()

for i in range(len(words)):
    for j in range(i+1, len(words)+1):
        part_word.add(words[i:j])

print(len(part_word))