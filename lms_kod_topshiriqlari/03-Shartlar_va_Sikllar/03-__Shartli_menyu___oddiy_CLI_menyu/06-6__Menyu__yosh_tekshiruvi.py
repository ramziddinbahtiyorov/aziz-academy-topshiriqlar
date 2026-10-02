# age
# 1 -> Adult (>=18)
# 2 -> Minor (<18)
# aks holda Invalid
choice = int(input())
if choice == 1:
    print("Adult")
elif choice == 2:
    print("Minor")
else:
    print("Invalid")