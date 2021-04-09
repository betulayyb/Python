liste=[1,2,3,4,5,6,7,8,9,10]
for eleman in liste:
    print("Eleman",eleman)
toplam=0
for eleman in liste:
    toplam += eleman
    print("Toplam:",toplam)
print("Toplam:",toplam)
if eleman in liste:
    if eleman%2== 0:
        print("cift sayılar",eleman)
s='Python'
for karakter in s:
    print(karakter)
for karakter in s:
    print(karakter*3)
demet=(1,2,3,4,5,6,7)
for eleman in demet:
    print(eleman)
liste=[(1,2),(3,4),(5,6),(7,8),(9,10)]
for eleman in liste:
    print(eleman)
for(i,j) in liste:
    print(i,j)
liste1=[(1,2,3),(4,5,6),(7,8,9),(10,11,12)]
for(i,j,k) in liste1:
    print(i*j*k)
sozluk={"bir":1,"iki":2,"üç":3}
for eleman in sozluk.keys(): #sözlük üzereinde gezip anahtarları yazdırdı
    print(eleman)
for eleman in sozluk.values():
    print(eleman)
for (i,j) in sozluk.items():
    print("Anahtar:",i,"Deger:",j)
