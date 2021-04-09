liste=[1,3.43,"murat",34,2,1] #liste tanımladık
print(liste)
bos_liste=[] #boş liste oluşturduk
bos_liste=list() #boş liste oluşturduk
print(len(liste)) #listenin boyutunu bulduk
print(len(bos_liste)) #listenin boyutunu bulduk
s="merhaba"
print(list(s)) #stringi liseye çevirdik
liste1=[1,2,3,4]
liste2=[5,6,7,8]
liste_toplam=liste1+liste2 #listeleri topladık
print(liste_toplam)
liste3=["er",1,7,5]
print(liste3)
liste3=liste3+[1,"re"] #listeye sonradan eleman ekledik
print(liste3)
print(liste3*3) #listeyi 3 kere yan yana yazdırdık,ama listenin asıl değeri değişmedi
liste3=liste3*3 #listeyi 3 kere yan yana yazdırdık ama eşitlik olduğu için listenin asıl değeri değişti
liste.append(1) #listeye eleman ekledik
print(liste)
liste.append("murat") #listeye eleman ekledik
print(liste)
liste4=[2,3,4,5,6]
liste4.pop() # liste4 ün son elemanını listeden atar ve ekrana bastırır
print(liste4)
liste4.pop(2) # liste4 ün 3. elemanını listeden atar ve ekrana yazdırır
print(liste4)
liste4.sort() #küçükten büyüye sıraladık
print(liste4)
liste4.sort(reverse=True) #büyükten küçüğe sıralar
print(liste4)
meyveler=["elma","armut","muz","kiraz","kavun"]
meyveler.sort() #alfebetik olarak küçükten büyüğe doğru sıralar
print(meyveler)
meyveler.sort(reverse=True) #alfebetik olara büyükten küçüğe sıralarız
print(meyveler)
#iç içe listeler
a=[1,2,3]
b=[3,4,5]
c=[2,4,7]
newlist=[a,b,c] #üç tane listeyi birleştirdik
print(newlist)
print(newlist[2][1]) #liste içerisinden 2. satır 1. sutundan değer yazdırdık
#DEMETLER
demet=(1,2,3,4,5,5,4,3,6,8,5,4) # demetlerin listelerden farkı demetlerin değiştirilemez olmasıdır.
# Onun dışında listelerde geçerli olan tüm fonksiyonlar demetlerdede geçerlidir.
print(demet.count(4)) #demet içerisinde kaç tane 4 sayısı olduğunu gösterir
print(demet.count(1))
print(demet.index(5))



