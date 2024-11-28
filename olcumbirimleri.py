olcumbirimi=(input("Çevirmek istediğiniz ölçüm birimini giriniz."))
if(olcumbirimi=="F" or olcumbirimi=="Fahrenheit"):
    kacselsiyus=float(input("Celsius değerini giriniz:"))
    fahrenheit=kacselsiyus*1.8+32
    print(fahrenheit)
elif(olcumbirimi=="C" or olcumbirimi=="Celsius"):
    kacfahrenheit=float(input("Fahrenheit değerini giriniz:"))
    celsius=(kacfahrenheit-32)/1.8
    print(celsius)
