#------------------------------------
i=0;
while(i<20):
    print(i)
    i=i+1
    if (i==10):
        break # 10 hariç tüm sayıları yazdırır
#------------------------------------
for liste in(range(0,20)):
    print(liste)
    if (i==18):
        break # i 18 olduğunda döngüden çık
#------------------------------------
while True:
    isim=input("İsminizi giriniz:(Çıkmak için q tuşuna basınız)")
    if(isim=="q"):
        print("Çıkış yapılıyor..")
        break #sonsuz döngüye girdi, q ya basınca çıkıyor
    print("isim",isim)
#------------------------------------
liste=list(range(0,20))
for i in liste:
    if(i==2 or i==6):
        continue
    print("i:",i) # 2 ve 6 hariç tüm sayıları yazdırır
#------------------------------------
