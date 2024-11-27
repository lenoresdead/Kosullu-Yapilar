# Kosullu Yapilar
Koşullu yapılar, programın akışını belirli bir koşulun doğruluğuna göre yönlendiren yapılardır. Bu yapılar, bir koşulun doğru (True) ya da yanlış (False) olmasına göre farklı işlemlerin yapılmasını sağlar. 3 farklı koşullu yapı mevcuttur;

# 1)If Yapısı
Türkçe meali "eğer" olan if,  belirli bir koşul doğruysa bir işlem yapılmasını sağlar.

örnek:

if a > b:
    print("a, b'den büyüktür.")

# 2)Elif Yapısı
Elif(else if), birden fazla koşulun kontrol edilmesini sağlar. İlk koşul sağlanmazsa, bir sonraki koşul kontrol edilir.

NOT: Elif her zaman if'ten sonra kullanılır.

örnek:

if a > b:
    print("a, b'den büyüktür.")
elif a == b:
    print("a, b'ye eşittir.")
else:
    print("a, b'den küçüktür.")

# 3)Else Yapısı
Aksi takdirde anlamına gelen else, if koşulunun sağlanmaması durumunda yapılacak işlemi tanımlar. Hiçbiri değilse budur koşuludur. Her zaman en sonda kuollanılır.

örnek:

if a > b:
    print("a, b'den büyüktür.")
else:
    print("a, b'den büyük değildir.")

