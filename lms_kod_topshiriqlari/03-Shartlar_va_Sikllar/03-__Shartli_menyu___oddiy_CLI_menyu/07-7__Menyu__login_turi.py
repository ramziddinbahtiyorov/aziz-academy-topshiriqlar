# role
# admin -> "Full access"
# user -> "Limited"
# aks holda "Guest"
role = input()
if role == "admin":
    print("Full access")
elif role == "user":
    print("Limited")
else:
    print("Guest")