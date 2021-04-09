sayi=int(input("Faktoriyelini almak istediğiniz sayıyı giriniz: "))
factoriyel=1
liste=list(range(1,sayi))
for i in liste:
    factoriyel=factoriyel*sayi
    sayi=sayi-1
print(factoriyel)