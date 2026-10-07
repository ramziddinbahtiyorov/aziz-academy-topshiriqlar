action = int(input())
balans = int(input())
summa = int(input())

if action == 1:
    print(balans)
elif action == 2:
    if summa <= balans:
        print(balans - summa)
    else:
        print("Mablag' yetarli emas")
elif action == 3:
    print(balans + summa)
else:
    print("Notogri amal")