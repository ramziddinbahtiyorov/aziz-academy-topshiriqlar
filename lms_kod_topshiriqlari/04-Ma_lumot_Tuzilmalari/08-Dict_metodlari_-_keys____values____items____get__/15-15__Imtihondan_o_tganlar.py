n = int(input())
d = {}
for _ in range(n):
    ism, ball = input().split()
    d[ism] = int(ball)
chegara = int(input())
soni = 0
for ism, ball in d.items():
    if ball >= chegara:
        print(ism, ball)
        soni += 1
print("O'tganlar:", soni)