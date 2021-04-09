note = int(input("Notunuzu giriniz:"))

if 100 < note or note <= 80:
    pass
# if - else kullanımı
else:
    print("Norunuz AA")
if 80 >= note > 60:
    print("Notunuz BB")
if 60 < note or note <= 40:
    print("Kaldınız!")
else:
    print("Notunuz CC")

# if - elif - else kullanımı
if note > 80:
    print("Norunuz AA")
elif note > 60:
    print("Notunuz BB")
elif note > 40:
    print("Notunuz CC")
else:
    print("Kaldınız!")
