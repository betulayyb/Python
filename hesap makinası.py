a = int(input("Birinci değeri giriniz:"))
b = int(input("ikinci değeri giriniz:"))
sonuc = None

print("HESAP MAKİNASI")

print("Toplama : 1", "Çıkarma : 2", "Çarpma : 3", "Bölme: 4", sep="\n")

print("Yukarıdaki kodları kullanarak yapmak istediğiniz işlemi seçiniz....")

islem = int(input("İşlem Seçiniz:"))

if islem == 1:
    print("sonuc={}".format(a + b))
elif islem == 2:
    print("sonuc={}".format(a - b))
elif islem == 3:
    print("sonuc={}".format(a * b))
elif islem == 4:
    print("sonuc={}".format(a / b))
else:
    print("Boyle bir işlem yok! Lütfen tekrar deneyiniz...")
