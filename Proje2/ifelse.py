a=2
if(a==2):
    print(a)
print("Merhaba")
"""
Dikkat ederseniz burada daha önce görmediğimiz bir şey yaptık ve if in bulunduğu satırdan sonraki print işlemini bir 
tab kadar girintili yazdık.Burada gördüğümüz gibi, girintiler(tab) Pythonda bir blok oluşturmak için kullanılıyor ve
her bloğunun çalıştırılması gerekmiyor. Mesela yukarıda gördüğümüz kodda 2 print işlemi de çalıştı. Ancak kodumuzu şu
şekilde yazsaydık, ilk print işlemi çalışmayacaktı.
"""
if (a==3):
    print(a)
    print("Merhaba")

yas=int(input("Yaşınızı Giriniz="))
if(yas<18):
    print("Bu mekana giremezsiniz.")

sayi=int(input("Sayıyı giriniz="))
if (sayi<0):
    print("Sayı negatiftir.")

#YANLIŞ KOD
yas1=int(input("yasınızı giriniz="))
if(yas1<18):
    print("Bu mekana giremezsiniz.")
print("Hoşgeldiniz")

#if-else
yas2=int(input("yasınızı giriniz="))
if(yas2<18):
    print("Bu mekana girilemez.")
else:
    print("Mekana Hoşgeldiniz...")












