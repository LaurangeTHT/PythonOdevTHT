isim = input("İsminiz nedir? ")
print("Merhaba", isim, end="!\n")

print("""

=========******============
| - 1. -| Çarpma
| - 2. -| Toplama
| - 3. -| Bölme
| - 4. -| Çıkartma
=========******===========

         """)
işlem =  input("İşlem Numarasını Giriniz:") 

x = int(input("Birinci Sayı:")) 

y = int(input("İkinci Sayı:")) 

if (işlem == "1"): 

             	print("Sonuç :",x * y)

elif (işlem == "2"):

             print("Sonuç :",x + y)

elif (işlem == "3"):

	print("Sonuç :",x / y)

elif (işlem == "4"):

            print("Sonuç :",x - y)
else:

    print("Lütfen geçerli işlem numarası giriniz. :")