sayi=int(input("Sayiyi Giriniz:"))
liste=[1]
toplam=0
for i in liste:
    say=sayi%10
    print(say)
    sayi1 = sayi - say
    sayi2=sayi1/10
    sayi=sayi2
    a=say**4
    toplam=toplam+a
    if(sayi<1):
        break
    else:
        liste.append(1)
print(toplam)




