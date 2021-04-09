print("Beden Kitle İndeksi Hesaplama Programına Hoşgeldiniz...")

boy = float(input("Buyunuzu metre cinsinden giriniz:"))
kilo = float(input("Ağırlığınızı kilo cinsinden giriniz:"))

print("Beden Kitle İndeksiniz Hesaplanıyor...")
indeks = float(kilo / (boy * boy))

print(" Vücut kitle İndeksiniz : {}".format(indeks))

print("Mevcut Durmunuz:")

if indeks < 18.5:
    print("Zayıfsınız.")
elif indeks <= 25:
    print("Normal")
elif indeks <= 30:
    print("Kilolusunuz")
elif indeks > 30:
    print("Çok Kilolususunuz.")
else:
    print("Negatif fdeğer giremezsiniz!")