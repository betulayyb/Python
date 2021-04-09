
ogrenci_sayisi=int(input("Kaç Tane Öğrenciniz Var?"))
ogrenci_isimleri=list()
ogrenci_soyadlari=list()
ogrenci_numaralari=list()
ogrenci_notlari=list()
ogrenci_harfleri=list()

while True:
    ogrenci_adi=input("Öğrenci adı:")
    ogrenci_isimleri.append(ogrenci_adi)
    ogrenci_soyadi=input("Ogrenci Soyadı:")
    ogrenci_soyadlari.append(ogrenci_soyadi)
    ogrenci_numarasi=int(input("Öğrenci Numarası:"))
    ogrenci_numaralari.append(ogrenci_numarasi)
    vize_bir=int(input("Öğrencinin 1. Vize Notu:"))
    vize_iki=int(input("Üğrencinin 2. Vize Notu:"))
    final=int(input("Öğrencinin Final:"))
    not_ortalamasi=(0.3*vize_bir) + (0.3*vize_iki) + (0.4*final)
    ogrenci_notlari.append(not_ortalamasi)
    if (not_ortalamasi>=90):
        ogrenci_harfleri.append("AA")
    elif (not_ortalamasi>=85):
        ogrenci_harfleri.append("BA")
    elif (not_ortalamasi>=80):
        ogrenci_harfleri.append("BB")
    elif (not_ortalamasi>=75):
        ogrenci_harfleri.append("CB")
    elif (not_ortalamasi>=70):
        ogrenci_harfleri.append("CC")
    elif (not_ortalamasi>=65):
        ogrenci_harfleri.append("DC")
    elif (not_ortalamasi>=60):
        ogrenci_harfleri.append("DD")
    elif (not_ortalamasi>=55):
        ogrenci_harfleri.append("FD")
    else:
        ogrenci_harfleri.append("FF")
    ogrenci_sayisi-=1
    if (ogrenci_sayisi==0):
        break
print(ogrenci_isimleri)
print(ogrenci_soyadlari)
print(ogrenci_numaralari)
print(ogrenci_notlari)
print(ogrenci_harfleri)

