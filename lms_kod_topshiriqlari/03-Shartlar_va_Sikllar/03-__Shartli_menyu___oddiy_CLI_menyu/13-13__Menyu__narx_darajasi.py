# price
# <50 -> Cheap
# <200 -> Medium
# aks holda Expensive
price = int(input())
if price < 50:
    print("Cheap")
elif price < 200:
    print("Medium")
else:
    print("Expensive")