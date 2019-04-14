print(*"GÜVENLİ ŞİFRE PROGRAMI --- By Laurange")

harfler= "abcçdefghgğhıijklmnoöprsştuüvwxyzABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVWXYZ"
rakamlar="0415862379"
özelkarekterler="' ! # @ . , $ "

import random

import string


while True:
    soru_rakam = input("Parolanın içerisinde sayı olsun mu? [E/H]: ")
    if soru_rakam != 'E' and soru_rakam != 'H':
        print('Hatalı giriş - E veya H yazmanız gerekiyor.')
        continue
    
    while True:
        soru_harf = input("Parolanızda harf olsun mu? [E/H]: ")
        if soru_harf != 'E' and soru_harf != 'H':
            print('Hatalı giriş - E veya H yazmanız gerekiyor.')
            continue
        
        while True:
            soru_özelkarakter = input("Parolanın içerisinde özel karakter olsun mu? [E/H]: ")
            if soru_özelkarakter != "E" and soru_özelkarakter != "H" :
                print("Hatalı giriş - E veya H yazmanız gerekiyor.")
                continue
        
            while True:
                soru_enaz = int(input("Parolanız minumum kaç karakter olsun? "))
                soru_ençok = int(input("Parolanız maksimum kaç karakter olsun? "))
                if soru_enaz <= 0 and soru_enaz >= soru_ençok:
                    print(" HATA - Geçerli değer girmediniz.")
                    
                    
                    continue
                break
            break
        break
    break

def rastgeleseçim(stringLength = soru_enaz):
        if soru_rakam == "E" and soru_harf == "H" and soru_özelkarakter == "E" :
            parolakarakterleri = harfler + rakamlar  
  
        elif soru_rakam == "E" and soru_harf == "E" and soru_özelkarakter == "H" :
            parolakarakterleri = rakamlar + harfler
        
        
        elif soru_rakam == "H" and soru_harf == "E" and soru_özelkarakter == "E" :
            parolakarakterleri = özelkarekterler + harfler 
       
        
        elif soru_rakam == "E" and soru_harf == "H" and soru_özelkarakter == "H" :
            parolakarakterleri = rakamlar 
       
        
        elif soru_rakam == "H" and soru_harf == "E" and soru_özelkarakter == "H" :
            parolakarakterleri = harfler 
      
        
        elif soru_rakam == "H" and soru_harf == "H" and soru_özelkarakter == "E" :
            parolakarakterleri = özelkarekterler
       
        
        elif soru_rakam == "E" and soru_harf == "E" and soru_özelkarakter == "E" :
            parolakarakterleri = özelkarekterler + rakamlar + harfler 
        return ''.join(random.choice(parolakarakterleri) for i in range(stringLength))

print ("Şifre", rastgeleseçim(soru_enaz) )

parola = ''
        
print(parola)