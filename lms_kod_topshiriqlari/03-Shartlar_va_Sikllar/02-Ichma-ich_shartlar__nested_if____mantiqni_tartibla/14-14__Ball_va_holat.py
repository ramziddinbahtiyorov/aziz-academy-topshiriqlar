# score
# Agar score >= 50 bo'lsa:
#   agar score >= 90 bo'lsa "Excellent"
#   aks holda "Pass"
# Aks holda "Fail"
score = int(input())
if score >= 50:
    if score >= 90:
        print("Excellent")
    else:
        print("Pass")
else:
    print("Fail")