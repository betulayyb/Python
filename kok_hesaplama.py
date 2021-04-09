a = int(input("İkinci dereceden baş katsayı:"))
b = int(input("birinci dereceden baş katsayı:"))
c = int(input("sabit sayı:"))

print("Veriler Heartland....")

delta = b**2 - (4*a*c)
kok_bir = (-b - delta ** 0.5) // (2*a)
kok_iki = (-b + delta ** 0.5) // (2*a)

kokler = [kok_bir, kok_iki]

print("Birinci Kök:{}\nİkinci Kök:{}".format(kokler[0], kokler[1]))

print("İyi gunner...")
