# a (butun son)
# Agar a > 0 bo'lsa:
#   agar juft bo'lsa "Positive Even"
#   aks holda "Positive Odd"
# Aks holda "Not positive"
a = int(input())
if a > 0:
    if a % 2 == 0:
         print("Positive Even")
    else:
        print("Positive Odd")
else:
     print("Not positive")