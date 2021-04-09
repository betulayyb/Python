print("Oyuncu Kaydetme Programı")

Ad = input("Oyuncunun Adı:")
Soyad = input("Oyuncunun Soyadı:")
Takimi = input("Oyuncunun Takımı:")

print("Bilgiler Kaydediliyor...")

bilgiler = [Ad, Soyad, Takimi]

print("Oyuncunun adi: {}\nOyuncunun Soyadı: {}\nOyuncunun Takımı:{}\n".format(bilgiler[0], bilgiler[1], bilgiler[2]))

print("Bilgiler kaydedildi..")
