matn = input().lower()
unli_soni = sum(matn.count(h) for h in 'aeiou')
print(unli_soni)