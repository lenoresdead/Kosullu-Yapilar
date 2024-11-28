turkce=int(input("Turkce notunuzu giriniz"))
mat=int(input("Matematik notunuzu giriniz"))
tarih=int(input("Tarih notunuzu giriniz"))
ing=int(input("İngilizce notunuzu giriniz"))
fizik=int(input("Fizik notunuzu giriniz"))
ortalama=(turkce*5+mat*6+tarih*2+ing*4+fizik*4)/21
if(ortalama>=85):
    print("Tebrikler!Takdir belgesi aldınız.")
elif(ortalama>=70 and ortalama<85):
    print("Tebrikler!Teşekkür belgesi aldınız.")
else:
    print("Hiçbir belge alamadiniz.")
