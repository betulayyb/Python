print("Betül","bugün","okula","gelemeyecek") #print yazım şekli
print("Begüm bugün",16,"yaşına girecek") #print yazım şekli
print("ayşe\nbugün\ngelemez") # alt satıra geçme
print("oley!\tyarın\tyokul\tyok!") # bir tab boşluk bırakma
a=16;b=12.54;c="kalem"
print(type(a),type(b),type(c)) # tip sorgulama
print(a,b,c,sep="\n") # sep parametresiyle a b ve c değerlerini alt alta sıraladık.
# Bu fonksiyon print("{}\n{}\n{}".format(a,b,c)) fonksiyonuyla aynı işi yapar
print(3,4,5,6,7,sep=".") # sep parametresiyle virgül aralarına nokta eklendi
print("17","02","2020",sep="/") # sep parametresiyle virgül aralarına / eklendi
print("koş","ali","koş",sep=" ")  # sep parametresiyle virgül aralarına boşluk eklendi
print("koş","ali","koş",sep="\n")  # sep parametresiyle virgül aralarına bir satır aşağıya atlatıldı
print(*"print") # yıldız parametresi her bir karekterin arasına boşluk koyar
print(*"python",sep="\n") # yıldız parametresi her bir karekterin arasına boşluk koyar, sep parametreside bir satır aşağıya atar
print(*"TBMM",sep=".") # yıldız parametresi her bir karekterin arasına boşluk koyar, sep parametreside aralara . ekler
a=0.765454
b=3.876547
c=1.432151
print("{},{},{}".format(a,b,c)) #format şeklinde ekrana yazdırma
print("{1},{2},{0}".format("murat","abi",40)) #format şeklinde ekrana yazdırma
print("{:.2f},{:.3f},{:.4f}".format(a,b,c)) # noktadan sonra kaç basamak geleceğini ayarlar
