a=int(input("Birinci Katsayıyı Giriniz:"))
b=int(input("ikinci Katsayıyı Giriniz:"))
c=int(input("Üçüncü Katsayıyı Giriniz:"))

delta= (b**2)-(4*a*c)
birincikok  = (-b-(delta**0.5)) / (2*a)
ikincikok = (-b+(delta**0.5)) / (2*a)

print("Bİrinci Kök= ",birincikok)
print("Birinci Kok:",ikincikok)

