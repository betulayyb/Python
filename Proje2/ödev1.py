boy=int(input("Boy="))
kilo=int(input("Kilo="))
indeks= kilo/(boy*boy)
if(indeks<18.5):
    print("Zayıf")
elif(indeks>=18.5 and indeks<25):
    print("Normal")
elif(indeks>=25 and indeks<30):
    print("Fazla Kilolu")
elif(30>=indeks):
    print("Obez")