transport = int(input())
category = int(input())

if transport == 1:
    price = 1700
elif transport == 2:
    price = 1700
elif transport == 3:
    price = 4000
else:
    price = None
    
if price is None:
    print("Notogri transport")
else:
    if category == 1:
        print(price)
    elif category == 2:
        print(price // 2)
    elif category == 3:
        print(0)
    else:
        print("Notogri toifa")