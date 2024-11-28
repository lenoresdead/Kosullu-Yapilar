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

  
