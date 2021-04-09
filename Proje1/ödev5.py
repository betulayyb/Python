sayi1=int(input("Birinci ssayıyı giriniz:"))
sayi2=int(input("İkinc sayıyı giriniz:"))
print("Değiştirilmeden önceki değerler\nsayi1:{} sayi2:{} \n ".format(sayi1,sayi2))
sayi1,sayi2=sayi2,sayi1
print("Beğiştirildikten sonraki değerler\nsayi1:{} sayi2={}\n".format(sayi1,sayi2))
