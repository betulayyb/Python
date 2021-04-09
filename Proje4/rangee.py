print(*range(0,20)) # 0 dan 20 ye kadar yazdırır
liste=list(range(0,20))
print(*range(10,0,-1))
print(*range(20,0,5))
print(*range(0,20,2))
for liste in (range(0,20)):
    print(liste)
for liste in (range(0,20)):
    print('*'*liste)

