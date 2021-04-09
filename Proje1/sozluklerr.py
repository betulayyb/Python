sozluk={"bir":1,"iki":2,"üç":3,"dort":4} # anahtar-deger ikilisiyle bir sözlük oluşturduk
print(sozluk)
print(sozluk["iki"]) # sözlük içinden "iki" anahtarını çağırdık
sozluk2={"cay":"seker","kahve":"sut","su":"bardak"}
print(sozluk2)
print(sozluk2["cay"])
sozluk3={"ev":"kira","okul":"ogrenci","3degil":5,"4":5}
print(sozluk3["ev"])
sozluk["bir"]=sozluk["bir"]+4 # bir anahtarının karşılığı olan 1 değerine 4 ekledik
print(sozluk["bir"])
sozluk["bir"]+=5 # yukarıda 4 eklediğimiz  "bir" anahtarının değerine şimdide 5 ekledik
print(sozluk["bir"])
bos_sozluk={}
bos_sozluk2=dict()
sozluk4={"mevsimler":["yaz","kıs",",ilk bahar","sonbahar"],"a":[1,2,3,"dört"],"o":1} # 3 anahtarlı bir sözlük oluşturduk. ilk ikisi listedir.
print(sozluk4["mevsimler"])
sozluk["bes"]=5 #sozluğe eleman ekledik. ama sözlüğe eklenen eleman her hangi bir yere konur sozluklerde sıralama yoktur
print(sozluk)
sozluk5={"season_and_fruit":{"summer":"watermelon","winter":"orange","spring":"plum"},"numbers":{"one":"bir","two":"iki"}} #içi içe sözlük oluşturduk
print(sozluk5["season_and_fruit"]["summer"])
# NOT : Sözlüklerle işlem yaparken listeler gibi düşünmemeliyiz.
# Daha çok bir sözlüğü açmışız ve içerisinden bir kelimenin anlamına bakıyormuşuz gibi düşünmeliyiz.
# indislerle değil anahtarlarla hareket etmeliyiz.
list1=sozluk.values() # Values(değerleri) liste olarak döndürdük
list2=sozluk.keys() # anahtarları liste olaral döndürdük
list3=sozluk.items() # anahtarları ve listeleri matris olarak döndürdük
print("{}\n{}\n{}\n".format(list1,list2,list3)) #uzun yoldan az önce tanımladığımız 3 listeyi alt alta yazdırdık
print(list1,list2,list3,sep="\n") #kısa yoladan az önce tanımladığımız 3 listeyi ekrana yazdırdık

list1=sozluk5.values() # Values(değerleri) liste olarak döndürdük (iç içe liste)
list2=sozluk5.keys() # anahtarları liste olaral döndürdük (iç içe liste)
list3=sozluk5.items() # anahtarları ve listeleri matris olarak döndürdük (iç içe liste)
print("{}\n{}\n{}\n".format(list1,list2,list3)) #uzun yoldan az önce tanımladığımız 3 listeyi alt alta yazdırdık
print(list1,list2,list3,sep="\n") #kısa yoladan az önce tanımladığımız 3 listeyi ekrana yazdırdık





