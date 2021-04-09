print("En büyüğünü bulmak istediğiniz sayıları giriniz")

birinci_sayi=int(input("Birinci sayıyı giriniz:"))
ikinci_sayi=int(input("İkinci sayıyı giriniz:"))
ucuncu_sayi=int(input("Üçüncü sayıyı giriniz:"))

print("Sayılar değerlendiriliyor...")

if birinci_sayi>ikinci_sayi and birinci_sayi>ucuncu_sayi:
    en_buyuk=birinci_sayi
    print("Büyük sayi:",birinci_sayi)
elif ikinci_sayi>birinci_sayi and ikinci_sayi>ucuncu_sayi:
    en_buyuk=ikinci_sayi
    print("Büyük sayi:", ikinci_sayi)
elif ucuncu_sayi>birinci_sayi and ucuncu_sayi>ikinci_sayi:
    en_buyuk=ucuncu_sayi
    print("Büyük sayi:",ucuncu_sayi)