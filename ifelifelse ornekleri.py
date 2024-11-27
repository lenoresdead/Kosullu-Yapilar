kartbilgileri={
"kart no":"123456",
"cvv":"110",
"skt":"10/28"
 }
kartno=input("Lutfen kart no giriniz")
cvv=input("Lutfen cvv giriniz")
skt=input("Lutfen son kullanma tarihini giriniz")
if(kartbilgileri["kart no"]==kartno and kartbilgileri["cvv"]==cvv and kartbilgileri["skt"]==skt):
    print("islem onaylanmistir")
else:
    print("islem onaylanamamistir,lutfen tekrar deneyiniz.")



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
