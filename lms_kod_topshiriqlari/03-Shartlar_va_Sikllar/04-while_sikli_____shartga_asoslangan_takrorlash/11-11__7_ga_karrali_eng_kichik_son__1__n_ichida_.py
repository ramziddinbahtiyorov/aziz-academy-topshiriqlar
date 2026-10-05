n = int(input())
i = 1
ans = "No"

while i <= n:
    if i % 7 == 0:
        ans = i
        break
    i += 1
    
print(ans)