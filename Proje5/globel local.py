c = 10  # Globalde tanımlanmış bir değişken

def fonksiyon():
    c = 2  # Yerelde tanımlanmış bir değişken
    print(c)  # Yerel değişken kullanılıyor.
fonksiyon()
print(c)
fonksiyon()
