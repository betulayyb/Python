sifre="12345"
bakiye=0
sifre1=input("Sifrenizi Giriniz:")
giris_hakki=3;
while True:
    if (sifre!=sifre1):
        print("Sireniz yanlış.")
        print("Tekrar Deneyiniz.")
        break
    else:
        print("Giriş Başarılı!")
        print("Para çekmek için : '1' , Para Yatırmak için '2' , Bakiye sorgulamak için '3' ")
        secenek=input("Sayıyı Giriniz:")
        if (secenek == '1'):
            para=int(input("Çekmek istediğiniz miktarı giriniz:"))
            if (bakiye<para):
                print("Bakiye Yetersiz!")
            else:
                bakiye=para+bakiye
                print("İşleminiz Sonlandı!")
        elif(secenek=='2'):
            para=int(input("Çekmek istediğiniz miktarı giriniz:"))
            bakiye=bakiye+para
            print("Paranız Yatırıldı...")
        elif(secenek=='3'):
            print("Son bakiyeniz: ",bakiye)
        else:
            print("Böyle bir seçenek yok!")