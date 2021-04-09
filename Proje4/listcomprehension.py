liste = [1, 2, 3, 4]
liste.append(5)  # listeye 5 ekledi
print(liste)
# ------------------------------------
liste1 = list()  # boş liste oluşturur
for i in liste:
    liste1.append(i)  # liste2 ye liste içindeki değerleri yaz
# ------------------------------------
liste5 = [2, 3, 4, 5]
liste6 = [i * 3 for i in liste5] # listeyi 3 ile çarpar
print(liste6)
# ------------------------------------
liste3 = [1, 2, 3, 4, 5]
liste4 = [i * 2 for i in liste3] #listeyi 2 ile çarpar
print(liste3)
# ------------------------------------
liste7 = [(1, 2, 3), (10, 20, 30), (2, 3, 4), (20, 30, 40)]
liste8 = [i * j * y for (i, j, y) in liste7] #dizideki ilk satırı çarpar
print(liste8)
# -------------------------------------
liste9 = list(range(0, 20, 2))
liste10 = [i for i in liste9 if not (i == 4 or i == 8)] #listeden 4 ve 8 i çıkarır
print(liste10)
# -------------------------------------
s = "Okul"
liste11 = [i * 3 for i in s] # listede her bir harfi üç kere yazdırıp listeye atar
print(liste11)
# -------------------------------------
liste12 = [[1, 2, 3], [4, 5, 6, ]]
liste13 = list()
for i in liste12: # listenin içindekileri yazdırır
    print(i)
# --------------------------------------
liste14 = [[1 ,2 ,3], [4, 5, 6], [7, 8, 9]]
liste15 = list()
for i in liste14:
    for x in i:
        liste15.append(x)
print(liste15) # listeyi tek bir liste de yazdırır
# ---------------------------------------
liste16=[[1,2,3],[4,5,6],[7,8,9]]
liste17=[x for i in liste16 for x in i]
print(liste17) # listeyi tek bir listede yazdırır