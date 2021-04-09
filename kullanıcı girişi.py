print("*** İnstagram Kullanıcı Kayıt ve Girişi ***")

"""
İnstagram Kullanıcı Girişi Programı....

"""
print("Lütfen Kayıt İçin Geçerli Bilgileri Giriniz.")
kullanici_adi=input("Telefon numarası, kullanıcı adı veya e-posta:")
sifre=input("Şifre:")

print("Bilgileriniz Kaydediliyor...")
print("Bilgileriniz Kaydedildi.")

print("Lütfen giriş yapabilmek için şifrenizi ve kullanıcı adınızı giriniz.")

kullanici_adi_giris=input("Telefon numarası, kullanıcı adı veya e-posta:")
sifre_giris=input("Şifre:")

if kullanici_adi==kullanici_adi_giris and sifre==sifre_giris:
    print("Giriş Başaralı!")
elif kullanici_adi==kullanici_adi_giris and sifre!=sifre_giris:
    print("Şifre Yanlış!")
elif kullanici_adi != kullanici_adi_giris and sifre == sifre_giris:
    print("Kullanıcı Adi Yanlış!")
else:
    print("Kullanıcı Adı ve Şifre Yanlış!")