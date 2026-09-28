# username va age
# Agar username == "admin" bo'lsa:
#   agar age >= 18 bo'lsa "Full access"
#   aks holda "Limited"
# Aks holda "No access"
parts = input().split()
username = parts[0]
age = int(parts[1])
if username == "admin":
    if age >= 18:
        print("Full access")
    else:
        print("Limited")
else:
    print("No access")