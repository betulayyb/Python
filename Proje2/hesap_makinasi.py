a=int(input("Birinci Sayıyı giriniz:"))
b=int(input("İkinci sayıyı giriniz:"))
print("çarpma yapmak istiyorsanız 1 e , bölme yapmak istiyorsanız 2 ye, toplama için 3 , çıkarma için 4 e basınız.")
islem_sec=int(input("İşlem sayısını giriniz:"))
if(islem_sec==1):
    print("carpim=",a*b)
elif(islem_sec==2):
    print("bölüm:",a/b)
elif(islem_sec==3):
    print("toplam:",a+b)
elif(islem_sec==4):
    print("çıkarma:",a-b)
else:
    print("Böyle bir işlem yok! Hesap makinemiz o kadar gelişmiş değil!")
