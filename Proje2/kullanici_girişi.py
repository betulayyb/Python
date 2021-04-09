kullanici_adi="betulayyb"
sifre="betulay"
kullanici_adi1=input("Kullanıcı adını giriniz:")
sifre1=input("şifreyi giriniz:")
if(kullanici_adi==kullanici_adi1 and sifre==sifre1):
    print("Giriş Başarılı")
elif(kullanici_adi!=kullanici_adi1 and sifre!=sifre1):
    print("Giriş Başarılı Değil. Tekrar Deneyin...")
elif(kullanici_adi==kullanici_adi1 and sifre!=sifre1):
    print("Giriş Başarılı Değil. Tekrar Deneyin...")
else:
    print("Giriş Başarılı Değil. Tekrar Deneyin...")
