import time
class kutuphane:
    def __init__(self,kitapadi,kitapyazari,basimyili,sayfasayisi):
        self.kitapadi= kitapeqweqweqwe
        self.kitapyazari = kitapyazari
        self.basimyili = basimyili
        self.sayfasayisi = sayfasayisi

def arayuz():
    a=0
    print("Kütüphaneye hos geldiniz, yapmak istediğinizi seçiniz:\n1)Kitap ekle\n2)Kitap Çıkart\n3)Kitaplari Listele\n4)Çıkış yap")
    try:
        a = int(input())
    except:
        print("Sanırım yanlış yazım yaptınız yeniden deneyin")
        time.sleep(1)
        arayuz()
    
    if (a==1):
        return kitapekle()
    elif(a==2):
        return kitapcikar()
    
    elif (a==3):
        return kitaplarigoster()
    
    elif(a==4):
        return exit()
    else:
    
        print("Sanırım yanlış yazım yaptınız yeniden deneyin")
        time.sleep(1)
        arayuz()


def kitapekle():
    
    print("Kitabın ismi nedir?")
    isim = str(input().capitalize())
    print("Kitabın yazarı kimdir?")
    yazar = str(input().capitalize())
    print("Kitabın basım yılı nedir?")
    yas = str(input())
    print("Kitabın sayfa sayısı nedir?")
    sayfa = str(input())
    girilecek = kutuphane(isim,yazar,yas,sayfa)

    with open("veriler.txt","a+") as dosya:
        dosya.write(str(girilecek.kitapadi).replace(" ","_").replace("ü","u").replace("ğ","g").replace("ü","u").replace("ş","s").replace("ç","c").replace("ö","o").replace("ı","i")+" ")
        dosya.write(str(girilecek.kitapyazari).replace(" ","_").replace("ü","u").replace("ğ","g").replace("ü","u").replace("ş","s").replace("ç","c").replace("ö","o").replace("ı","i")+" ")
        dosya.write(str(girilecek.basimyili).replace(" ","_").replace("ü","u").replace("ğ","g").replace("ü","u").replace("ş","s").replace("ç","c").replace("ö","o").replace("ı","i")+" ")
        dosya.write(str(girilecek.sayfasayisi).replace(" ","_").replace("ü","u").replace("ğ","g").replace("ü","u").replace("ş","s").replace("ç","c").replace("ö","o").replace("ı","i")+" ")
        dosya.write("\n")
    print("Başarılı, ana sayfaya yönlendiriliyorsunuz.")
    time.sleep(1)
    arayuz()
        


def kitapcikar():
    print("Çıkarmak istediğiniz kitabın adınız yazınız, Kitabın isminin doğru yazıldığına dikkat ediniz\nkelimeler arası boşluk bırakabilirsiniz.")
    cikarilacakkitap=str(input().capitalize().replace(" ","_").replace("ü","u").replace("ğ","g").replace("ü","u").replace("ş","s").replace("ç","c").replace("ö","o").replace("ı","i"))
    with open("veriler.txt","r+") as dosya:
        x=dosya
        a=dosya.read().splitlines()
        sutunsayisi=0
        for x in a:
            sutunsayisi=sutunsayisi+1
        i=0
        while(i<sutunsayisi-1):
            b=a[i].split()
            if b[0]== f"{cikarilacakkitap}":
                del a[i]
            i=i+1
        time.sleep(2)
    with open("veriler.txt","w") as dosya:
        j=0
        while j<sutunsayisi-1:
            dosya.write(f"{a[j]}")
            dosya.write("\n")
            j=j+1
    print("Ana menüye dönülüyor")
    time.sleep(1)
    arayuz()

            
                



def kitaplarigoster():
    print("Bütün kitaplar gösteriliyor:")
    time.sleep(0.5)
    with open("veriler.txt","r") as dosya:
        a=dosya.read().splitlines()
        for b in a:
            b = b.split()
            print("*"+b[0].replace("_"," "))
        print("Detaylı bilgi için kitap ismini yazınız(İstemiyorsanız ana menüye donmek için q'ya basın):")
        tercih = input().capitalize().replace(" ","_").replace("ü","u").replace("ğ","g").replace("ü","u").replace("ş","s").replace("ç","c").replace("ö","o").replace("ı","i")
        if tercih == "Q":
            dosya.close()
            arayuz()
        for g in a:
            g = g.split()
            if tercih == g[0]:
                print(f"Kitabın ismi:{g[0].replace("_"," ")} \nKitabın yazarı: {g[1].replace("_"," ")}\nKitabın basım yılı:{g[2].replace("_"," ")}\nKitabın sayfa sayısı:{g[3].replace("_"," ")}\n")
                time.sleep(5)
    kitaplarigoster()

        


arayuz()










