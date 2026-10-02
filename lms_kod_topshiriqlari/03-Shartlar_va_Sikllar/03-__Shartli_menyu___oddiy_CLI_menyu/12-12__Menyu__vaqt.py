# hour
# <12 -> Morning
# <18 -> Day
# aks holda Night
hour = int(input())
if hour < 12:
    print("Morning")
elif hour < 18:
    print("Day")
else:
    print("Night")