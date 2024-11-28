a=int(input("bir sayi giriniz"))
b=int(input("bir sayi giriniz"))
c=int(input("bir sayi giriniz"))
if(a>b and a>c):
    print("a sayisi en buyuktur")
elif(b>a and b>c):
    print("b sayisi en buyuktur")
elif(c>a and c>b):
    print("c sayisi en buyuktur")
else:
    print("girilen sayilarin arasinda en buyuk olan yoktur")
