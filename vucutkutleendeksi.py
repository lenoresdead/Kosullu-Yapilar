kutle=float(input("Lutfen kilonuzu giriniz."))
boy=float(input("Lutfen boyunuzu metre cinsinden giriniz."))
vki=kutle/(boy*boy)
if(vki<18):
    print("Normal kilonun altındasınız.")
elif(vki>=18 and vki<=24):
    print("Normal ve sağlıklı kilodasiniz.")
elif(vki>=25 and vki<=29):
    print("Normal kilonun üstündesiniz.")
elif(vki>=30 and vki<=40):
    print("Normal kilonun fazla üzerisindesiniz.")
elif(vki>40):
    print("Normal kilonun çok fazla üzerisindesiniz.")
