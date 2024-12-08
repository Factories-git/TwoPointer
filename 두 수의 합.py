n = int(input())
sequence = sorted(map(int, input().split()))
target = int(input())

right = 0
sm = 0
c = 0

for left in range(n):
    while sm < target and right < n:
        sm += sequence[right]
        right += 1
    if sm == target:
        c += 1
    sm -= sequence[left]

print(c)
