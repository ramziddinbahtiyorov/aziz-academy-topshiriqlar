s = 0
count = 0

while True:
    n = int(input())
    if n == 0:
        break
    s += n
    count += 1
    
if count == 0:
    print(0)
else:
    print(s / count)