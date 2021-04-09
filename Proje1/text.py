' Hello world ' #'' arasında string yazma
" Hello world " # " " arasında string yazma
""" ello world """ # """ """ arasında string yazma
print("Hello world") # ekrana yazdırma
print("""Hello world 2""")
a="yeni dunya"
print(a[1:5]) # 1 den 4 e kadar olan kısmı yazdırma
print(a[:4]) # 0 dan 4 e kadar olan kısmı yazdırma
print(a[3:]) # 3 den sonuna kadar olan kısmı yazdırma
print(a[::2]) # bir atlayp bir yazdırma
print(a[::-1]) # tersten yazdırma
print(a[0:8:2]) # 0 dan 7 ye kadar bir atlayıp bir yazdırma
print(a[:]) # tüm diziyi yazdırma
print(len(a)) # kelimenin uzunluğu
a="ben "
b="""kardeşlerimi """
c="çok "
d='seviyorum'
print(a+b+c+d) # kelimeler toplanabilir
a="HAYAL "
a=a+"okulu bıraktı." # stringler ekleme yapılarak toplanabilir
print(a)
a="Allah Büyüktür "
print(a*33) # stringler çarpılabilir

