isim1="betulay"
sifre1="Betulay"
giris_hakki=3
while True:
    isim = input("İsinizi Giriniz:")
    sifre = input("Sifrenizi Giriniz:")
    if (isim!=isim1 and sifre!=sifre1):
        print("İsim ve Şifre Yanlış!")
        giris_hakki = giris_hakki - 1
    elif (isim!=isim1 and sifre==sifre1):
        print("Sifre Yanlış!")
        giris_hakki = giris_hakki - 1
    elif(isim==isim1 and sifre!=sifre1):
        print("isim Yanlış!")
        giris_hakki = giris_hakki - 1
    else:
        print("Giriş başarılı! hoşgeldiniz...")
        break
    if (giris_hakki==0):
        print("Giriş Hakkınız Bitti!")
        break
