n = int(input())
freq = {}

for _ in range(n):
    number = input()
    if number in freq:
        freq[number] += 1
    else:
        freq[number] = 1

count_three = sum(1 for v in freq.values() if v == 3)

print(count_three)
