# -*- coding: utf-8 -*-
   # https://colab.research.google.com/drive/1-AqYk7nOUut3lJWigIllr-flYCWs3juG

7%2 #açıklama satırı bu da mod alma işlemi

7//2 #bölümü gösterir (3)

7/2


3**3

10 < 11
10 == 10
19 != 10

not(10==10)

True and False

print(True and False or not True and not True) #sondan başlayacaksın eşleştrimeye

a=5
a+=5
print(a)

a %= 4
a

a **=2 # karesini alır
print(a)

"""If Else

"""

a = 10

if a == 10:  #iften sonra : altına da tab kadar boşluk bırak
  print("a eşittir 10") #burdaki tab ı unutma

a = 10

if a > 5:  #iften sonra : altına da tab kadar boşluk bırak
  print("a 5 den büyüktür") #burdaki tab ı unutma
  print("python en sevdiğim dil sağ ol mete hocam")
print("Girilen sayı",a)

a = -222

if a > 5:  #iften sonra : altına da tab kadar boşluk bırak
  print("a 5 den büyüktür") #burdaki tab ı unutma
  print("python en sevdiğim dil sağ ol mete hocam")
else:
  print("a 5 ten küçük")
print("Girilen sayı",a)

a = input("Sayı gir:")

if a > 5:  #iften sonra : altına da tab kadar boşluk bırak
  print("a 5 den büyüktür") #burdaki tab ı unutma
  print("python en sevdiğim dil sağ ol mete hocam")
else:
  print("a 5 ten küçük")
print("Girilen sayı",a)

a = int(input("Sayı gir:"))

if a > 5:  #iften sonra : altına da tab kadar boşluk bırak
  print("a 5 den büyüktür") #burdaki tab ı unutma
  print("python en sevdiğim dil sağ ol mete hocam")
else:
  print("a 5 ten küçük")
print("Girilen sayı",a,a)

a = 10
print(a)
type(a)

x=input("Lütfen bir sayı giriniz: ")
print(x)

x=input("Lütfen bir sayı giriniz: ")
print("Adınız:",x)

a

print("Sonuç", a)

sayı1=input("Birinci sayıyı giriniz:")
sayı2=input("ikinci ssayıyı giriniz:")
ortalama = (sayı1+sayı2)/2
print("Ortalama:", ortalama)

sayı1 = int(input("Birinci sayıyı giriniz:"))
sayı2 = int(input("ikinci ssayıyı giriniz:"))

ortalama = (sayı1 + sayı2) / 2

print("Ortalama: ", ortalama)

type(ortalama)

sinavNotu = int (input("Sınav notunuzu giriniz:"))
if (sinavNotu > 100) or (sinavNotu < 0):
  print("Yanlış not girdiniz!!!")
elif (sinavNotu >= 50):
    print("Geçtiniz")
elif (sinavNotu < 50):
    print("Kaldınız")
elif (sinavNotu == 50):
    print("Sınavdan 50 aldınız")
else:
    print("FF aldınız.")

q=int(input("Sayı gir: "))

if q==1:
  print("q=1")
elif q!=1:
  print("q=1 değil")

a = int (input("Birinci sayıyı giriniz:"))

if a==10:
  print(1)
if a>0:
  print(2)
else:
  print(3)

a  = int (input("Birinci sayıyı giriniz:"))

if a>4:
  print(1)
  if a==5:
    print(2)
  else:
    print(3)
  if a>12:
    print(4)
  else:
    print(5)
else:
  print(6)

a = 12
b = 100 if a == 10 else 50
print(b)

durum=1
msg = "başarılı" if durum==1 else "başarısız"
print(msg)

i = 1
while i<10:
  print(i)
  i+=1

print("Hello\t Merhabaaaa \nAlta indirdin beni")

print("Merhaba",end=" ")
print("Dünya")

print("Merhaba", end="," " umarım yolculuk iyi geçmiştir.")

print("Merhaba",end="***")
print("Dünya")

i = 1
while i<10:
  print(i, end="\t")
  i+=1

i = 1
while i<10:
  print(i, end=" ")
  i+=1

i = 1
while i<10:
  print(i**2, end=" ")
  i+=1

satır=1
n=6
while satır <= n:
  print("k" * satır)
  satır+=1

satır=5

while satır>0:
  print("*" * satır)
  satır-= 1

def pr(satirsayi):
  for i in range(satirsayi-1,-1,-1):
    yildiz=2*i+1
    bosluk=satirsayi-i
    satir=" "*bosluk+"*"*yildiz
    print(satir)
pr(5)

def priamitOlustur(satirSayisi):
  for i in range(satirSayisi):
    yildizSayisi=(2*i)+1
    boslukSayisi=satirSayisi-i-1
    satir=" "*boslukSayisi+"*"*yildizSayisi
    print(satir)

priamitOlustur(5)

deneme=3
while True:
  ad=input("Adınızı giriniz: ")
  sif=float(input("Şifrenizi giriniz: "))
  sif1=123
  ad1=ad
  if ad==ad1 and sif==sif1:
    print("Başarılı giriş")
    break
  else:
    print("Yanlış giriş")
    deneme-=1
  if deneme==0:
    print("Çok fazla deneme yaptınız")
    break

#Kulanıcnın aldığı sayının faktöriyelini aldıran kod

sayı=int(input("Faktöriyelini hesaplamak istediğiniz sayıyı giriniz:"))

i = 1
while 1 <= sayı:
  i = i*sayı
  sayı -= 1
print(i)

"""FOR"""

for i in range(5):
  print(i)

help(range)

for i in range(20,45):   #45 e kadar 45 olmaz
  print(i,end=" ")

for i in range(20,45,4):   #45 ye kadar 45 olmaz
  print(i,end=" :) ")

for i in range(20,0,-4):   #0 ye kadar 0 olmaz
  print(i,end="---")

n=4
for i in range(1,n+1):
  print("*" * i)

n=5
for i in range(n,0,-1):
  print("*" * i)

for i in range(5):
  print("Mete ({})".format(i))  #

k=61
print("Merhaba {}".format(k))

bulundu=0
for i in [10,20,30,40,50]:
  if i==40:
    bulundu=1
    print("Aranan eleman bulundu",i)
    break
  else:
    print("Bulunamadı")

if bulundu == 1:
  print("Bulundu")
else:
  print("Bulunamadı")

import random                    #rastgele sayılar verir import ederiz
for i in range(5):
  print(random.randint(1,100))   #randint dediğiimizden tam sayı verecek

a,b=0,1
for i in range(10):
  print(a,end=' ')
  a,b=b,a+b

for i in range(2,100):
  asal=1
  for j in range(2,i):
    if i%j==0:
      asal=0
      break
  if asal==1:
    print(i,end=" | ")

for i in range(2, 100):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i, end=" | ")
##asal=1 değişkenine gerek kalmadan yazılabilir    döngülerde else kullanılabilir

liste=[0,12,2,-11]

min(liste)
max(liste)

for i in liste:
  print(i,end=" ")

-11 in liste

50 not in liste

for i in liste:
  print(i**2,end=" ")

metin = "Merhaba"
for i in metin:
  print(i,end=" ")

liste = [10, -11, 3.14, "Mete", True, 100]

for i in liste:
  if i==True:
    break
  print(i)

for i in liste:
  if i=="Mete":      #Mete de yazar devam eder
    pass
  print(i ,end = "\t")

sayı = int(input("Bir sayı gir: "))

if sayı==0:
  pass
elif sayı !=0:
  print("Merhaba")

i = 10

while i<20:
  if i==13:
    break
  print("i",i)
  i+=1

#SÜREKLİ DÖNGÜYE GİRER 13 Ü DÖDÜRÜR DÖNDÜRÜR DURUR
i = 10

while i<20:
  if i==13:
    continue
  print("i",i)
  i+=1

i = 10

while i<20:
  if i==13:
    i+=1
    continue
  print("i",i)
  i+=1

i = 10

while i<20:
  if i==13:
      i+=1
      pass
  print("i",i)
  i+=1

liste1 = [1,2,3]
liste2 = [10,20,30]
a=10

for i in liste1:
  for j in liste2:
    if i>j:
      a=a+liste[j]
a

l1=[1,2,3]
l2=[9,8,7]
l3=[]

for i in l1:
  for j in l2:
    if i<j:
      if j not in l3:
        l3.append(j)
l3

liste = [10,20,30,-100]
yeniListe = []

for i in liste:
  yeniListe.append(i)

print(yeniListe)
#yeniListe  yazıp da yazdırabiliriz çıktı olarak

yeniListe = [i for i in liste]
print(yeniListe)
#yeniListe = [i for i in liste if i % 2 == 0]  # Sadece çift sayıları ekler

meyveler = ["muz","elma","portakal"]
print(meyveler)

meyveler.append("kavun")
print(meyveler)

meyveler

meyveler.remove("muz")
print(meyveler)

tup1=("ali")
tup2=("ylm")
tup1+=tup2
print(tup1)

indeks = meyveler.index("kavun")
print(indeks)

meyveler.sort()
print(meyveler)

uzunluk = len(meyveler)
print(uzunluk)

ilk_iki = meyveler[:2]
print(ilk_iki)
#: işaretinin sol tarafı başlangıç indeksini (boş bırakılırsa 0 demek)
#: işaretinin sağ tarafı bitiş indeksini (bu indeks dahil değil) gösterir

son_iki=meyveler[-2:]
print(meyveler)

meyveler.reverse()
print(meyveler)

tersMeyveler=meyveler[::-1]
print(tersMeyveler)
#[başlangıç:bitiş:adım] yapısını unutma:
#[::-1] → "Sondan başa , tersten 1'er 1'er git"
#[::2] → "Baştan sona, 2'şer atlayarak git"
#[2:5:1] → "2. indeksten 5. indekse kadar (5 dahil değil), 1'er 1'er git"
#-1 = "Tersine çevir" mantığı:
#Matematikte -1 ile çarpmak tersine çevirir, burada da aynı mantık var.

sayılar = [1,2,3,4,5,6,7,8,9,10]
çift_sayılar=[]
indeks=0

while indeks<len(sayılar):
  if sayılar[indeks]%2==0:
    çift_sayılar.append(sayılar[indeks])
  indeks+=1

print(çift_sayılar)

liste = [2,-2,4,-10,2,33,-44] #negatif sayıları pozitif yap ve listeyi yazdır
indeks=0

while indeks<len(liste):
  if liste[indeks]<0:
    liste[indeks]*=-1
  indeks+=1
print(liste)

# tekrar eden elemanları çıkar yazdır
elemanlar = ["elma", "muz", "elma", "muz", "çilek", "muz", "portakal"]
benzersiz_elemanlar = []

for eleman in elemanlar:
  if eleman not in benzersiz_elemanlar:
    benzersiz_elemanlar.append(eleman)

print(benzersiz_elemanlar)

elemanlar = ["elma", "muz", "elma", "muz", "çilek", "muz", "portakal"]
yeniElemanlar=[]
for i in elemanlar:
  if i  in yeniElemanlar:
    continue
  else:
    yeniElemanlar.append(i)
print(yeniElemanlar)

liste = [1,2,3,4,5,6,7,8,9,10]

len(liste)

liste

liste.insert(2,100)

liste

liste.insert(100,-555)
liste

liste.pop()

liste

i = liste.index(2)
i

liste

liste.remove(2)

liste

liste.count(0)

liste.sort()

liste

liste.sort(reverse=True)

liste

liste.clear()

yeniListe= liste.copy()
yeniListe

liste = []
liste

l=[]

for i in range(1,4,1):
  e=float(input(f"{i}. eleman:"))
  l.append(e)

liste = []
for i in range(5):
    eleman = float(input(f"{i+1}. elemanı girin: "))
    liste.append(eleman)

ortalama = sum(liste) / len(liste)

print(f"Listenin elemanlarının ortalaması: {ortalama}")

liste = []
for i in range(2):
  eleman = int(input('Lütfen {}. elemanı giriniz:' .format(i+1)))
  liste.append(eleman)

print("listemiz: ", liste)
print('toplam:',sum(liste))
print('ortalama:',(sum(liste)/len(liste)))

liste=[]
i=0
toplam=0

while i<5:
  eleman = int(input('Lütfen {}. elemanı giriniz:' .format(i+1)))
  liste.append(eleman)
  toplam+=eleman
  i+=1

print(liste)
print('toplam:',toplam)
print('ortalama:',(toplam/len(liste)))

liste

type(liste)

liste=['erz','trb',10,3.14,['ank'],14.53]

liste

liste[4]

liste=['erz','trb',10,3.14,['ank','ist'],14.53]

liste[4]

liste[4][0]

liste1=['erz','ank']

liste2=[10,20,liste1]

liste2

liste2[2][0]

liste1=[10,20,30]
liste2=[1,2,3]
liste3=liste2+liste1

liste3

liste1=['erz','ank','tr']
liste1=liste1 + ['ist']
liste1

liste

del liste[0]
liste

metin="Merhaba dünya"
type(metin)

liste4=list(metin)
liste4

type(liste4)

liste5=[i for i in range(10)]
liste5

x = []
for i in range(10):
  x.append(i)

print(x)

arabalar=["BMW","Mercedes","Audi"]
modeller= ["X6","E200","Corsa"]

arabalar.append(modeller)
arabalar

arabalar=["BMW","Mercedes","Audi"]
modeller= ["X6","E200","Corsa"]

arabalar.extend(modeller)
arabalar

tuple1 = ("Mete",25,"Erz")

type(tuple1)

tuple2 = "mete",40,3.14

tuple2

del tuple2  #siler

tuple1

for i in tuple1:
  print(i)

if 'Mete' in tuple1:
  print("mete var")
else:
  print("mete yok")

tuple5=("m","e","t","e")

tuple5

len(tuple5)

tuple5.count("a")

tuple5.index("m")

tuple6=("a","b")*5
tuple6

tuple7=(1,2,3)+(4,5,6)
tuple7

tuple8=list(tuple7)
type(tuple8)

tuple8

a=(1,2,3,4,5,6,7,8,9,10)

a[1:]

a[:5]

a[::2]

a[::-1]

tuple1

ad,yas,sehir=tuple1

ad

yas

sehir

tuple9=(0,1,2,3,4,5)
tuple9

ilkEleman,*ortaEleman,sonEleman=tuple9
# * operatörü, kalan tüm elemanları bir liste olarak toplar.
# Eğer * kullanılmazsa, eleman sayısı eşleşmez ve ValueError alırsınız.

ilkEleman

ortaEleman

sonEleman

ortaEleman1=tuple(ortaEleman)
ortaEleman1

ortaElemanlar2=tuple(ortaEleman)
print(type(ortaElemanlar2))#tuple olarak kullanmak için tuple dönüşümü yapmak lazım

first, *rest = (10, 20, 30, 40)
print(first)  # 10
print(rest)   # [20, 30, 40]

a=((0,1,2),(3,4,5),(7,8,9))
print("a[1][2]",a[1][2])

tuple1[1]

tuple1[1]=40
#değiştirilemezler sonradan

import sys
liste=['1','2','3','4','5','merhaba',3.14,True]
tuple0=('1','2','3','4','5','merhaba',3.14,True)
print(sys.getsizeof(liste,),'byte')
print(sys.getsizeof(tuple0,),'byte')
#bir nesnenin bellekte kapladığı alanı byte cinsinden verir

import timeit
print(timeit.timeit(stmt="['1','2','3','4','5','merhaba',3.14,True]"))
print(timeit.timeit(stmt="('1','2','3','4','5','merhaba',3.14,True)"))
#kod parçalarının çalışma süresini ölçmek

sözlük={"isim": "Mete", "yaş": 25, "şehir": "Erzurum"}
sözlük

sözlük["isim"]

sözlük["Meslek"]="Akademisyen"
sözlük

sözlük["eposta"]="mail@eklendi"
sözlük

del sözlük["eposta"]
sözlük

sözlük.pop("yaş")

sözlük

sözlük.popitem()

sözlük

sözlük1.clear()  #sözlük olacak orası, silmeyeyim diye yazdım sözlük1

sözlük={"isim": "Mete", "yaş": 25, "şehir": "Erzurum"}

if "isim" in sözlük:
  print("isim var")
else:
  print("isim yok")

for i in sözlük:
  print(i,":",sözlük[i])

sözlük.keys()

for i in sözlük.keys():     #for i in sözlük:    bu kullanımda olur
  print(i)

sözlük.values()

for i in sözlük.values():
  print(i)

sözlük.items()

for anahtar,değer in sözlük.items():
  print(anahtar,değer)

sözlük["isim"]="Ferhat"
sözlük

a=dict(sözlük)   #yapıyı sözlüğe dönüştürür
type(a)          #dict çıktısı verir

sözlük2=dict(isim="Mete",yaş=25,şehir="Erzurum")

sözlük.update(sözlük2)
sözlük

#Ortak Anahtar Yoksa
sözlük11  = {"meslek": "mühendis"}
sözlük22 = {"isim": "Mete"}

sözlük11.update(sözlük22)
print(sözlük11)  # {'meslek': 'mühendis', 'isim': 'Mete'}

#Aynı Anahtar Varsa
sözlük111  = {"isim": "Ahmet", "yaş": 30}
sözlük222 = {"isim": "Mete", "şehir": "Erzurum"}

sözlük111.update(sözlük222)
print(sözlük111)  # {'isim': 'Mete', 'yaş': 30, 'şehir': 'Erzurum'}

import pandas as pd

sözlük = {
    "İsim": ["Ahmet", "Mehmet", "Ayşe"],
     "Yaş": [25, 30, 28],
     "Şehir": ["İstanbul", "Ankara", "İzmir"]
    }

df = pd.DataFrame(sözlük)
df

df["Maaş"]=None

df

df.at[1,"Maaş"]=5000
df.at[3,"Maaş"]=1000000

df

import pandas as pd

veri = {
    "İsim": ["Ali", "Veli", "Ayşe", "Mehmet", "Zeynep"],
    "Yaş": [22, 34, 29, 40, 22],
    "Şehir": ["İstanbul", "Ankara", "İzmir", "İstanbul", "İzmir"]
}

df = pd.DataFrame(veri)

# Yaşı 25'ten büyük olanları filtrele
yas_filtreli = df[df["Yaş"] > 25]
print("Yaşı 25'ten büyük olanlar:\n", yas_filtreli)

# Şehirlere göre yaş ortalaması
sehir_grup = df.groupby("Şehir")["Yaş"].mean()
print("\nŞehirlere göre yaş ortalaması:\n", sehir_grup)

kisiler={
    "Mete":["Basketbol","Yüzme"],
    "Batu": ["Yürüyüş","Sinema","Kitap okuma"],
    "Ebru": ["Yüzme"],
    "Ferhat": ["Yürüyüş","Sinema","Dağcılık","Kitap Okuma"]

}

hobi_sayıları={kisi: len(hobi) for kisi,hobi in kisiler.items()}
print(hobi_sayıları)

son={}
for anahtar,deger in kisiler.items():
    son[anahtar]=len(deger)
print(son)

hobi_sayilari={kisi:len(hobiler) for kisi,hobiler in kisiler.items()}
print('hobi sayilari',hobi_sayilari)

"""Devamı kendi örneklerim"""

sözlük={"İsim" : "Ali", "Soyad" : "Yılmaz"}
sözlük["İsim"]

sözlük["Meslek"]="Barista"

del sözlük["Meslek"]

if "İsim" in sözlük:
  print("İçinde")
else:
  print("İçinde değil")

for i in sözlük:
  print(i,sözlük[i])

for i in sözlük.keys():
  print(i)

for i in sözlük.values():
  print(i)

sözlük.items()

for anahtar, değer in sözlük.items():
  print(anahtar,":",değer)

kisiler={
    "Mete":["Basketbol","Yüzme"],
    "Batu":["Yürüyüş","Sinema","Kitap Okuma"],
    "Ebru":["Yüzme"],
    "Ferhat":["Yürüyüş","Sinema","Dağcılık","Kitap Okuma"]
}

kisiler["Mete"]

a={1:50,2:100,3:22,4:0}
a

"""Fonoksiyonlar:"""

söz=dict(na="ali",yas=22)
söz.get("na")

söz.get("ali")

isim = input("İsminizi Giriniz: ")
print(f"Hoşgeldin {isim}")

def hosgeldin():
  print("Hoşgeldin!!!")

hosgeldin()

def hosgeldin1(isim):
  print("Hoşgeldin",isim)

hosgeldin1("Esra")
hosgeldin1("Ali")

def hosgeldin11(ism):
  print("Merhaba",ism)

hosgeldin11("Esra")

isim= input("İsminizi Giriniz: ")
hosgeldin11(isim)

hosgeldin11(input("İsminizi Giriniz: "))

def hosgeldin2(ad,soyad):
  print("Hoşgeldin",ad,soyad)

ad = input ("Adınızı Giriniz: ")
soyad = input ("Soyadınızı Giriniz: ")
hosgeldin2(ad,soyad)

def hosgeldin3(ad="Python",soyad="Dersi"):
  print("Hoş geldin",ad,soyad)# Varsayılan değer girildi.

hosgeldin3()

ad = input ("Adınızı Giriniz: ")
soyad = input ("Soyadınızı Giriniz: ")
hosgeldin3(ad,soyad) # Otomatik doldurma yok.

hosgeldin3(ad="Erhan") # Otomatik doldurma var.
hosgeldin3(soyad="Erhan") # Otomatik doldurma var.

def fonksiyon(ulke="Türkiye"):
  print("I am from "+ ulke)

fonksiyon()
fonksiyon("Germany")

def ogrenci(*bilgiler):
  for i in bilgiler:
    print(i)

ogrenci("Erhan","Kahveci","Bilgisayar Mühendisliği","Erzurum",22)
# *bilgiler - Fonksiyonun değişken sayıda argüman alabileceğini belirtir (tuple paketleme)
# Fonksiyon, aldığı tüm argümanları bilgiler adlı bir tuple içinde toplar
# for döngüsüyle bu tuple'ın elemanlarını tek tek yazdırır

def top(*sayilar):
  toplam = 0
  for i in sayilar:
    toplam+=i
  print("Toplam:",toplam)

top(1,2,3,4,5,6)
#kendi örneğim

def uzunk(*kelimeler):
  kelime=""
  for kel in kelimeler:
    if len(kel)>len(kelime):
      kelime=kel
  print("En uzun kelime:",kelime)

uzunk("Merhaba","Dünya","Python")
#kendi örneğim

def ogrenci2(**bilgiler):
  print("Adı:", bilgiler["ad"])
  print("Soyadı:", bilgiler["soyad"])
  print("Bölüm:", bilgiler["bölüm"])
  print("Şehir:", bilgiler["şehir"])
  print("yaş:", bilgiler["yaş"])

ogrenci2(ad="Erhan", soyad="Kahveci", bölüm="Bilgisayar Mühendisliği", şehir="Erzurum",yaş=22)

# ** sözlük yapısı oluşturuyor
# * yapısı tuple yapısı oluşturuyor

"""'''# **return**'''

"""

def topla(a,b):
  return(a+b)

topla(10,20)

def topla(a,b):
  toplam=a+b
  return toplam

topla(20,30)

sonuc=topla(20,30)
print("Girilen sayıların toplamı:",sonuc)

toplaYeni = lambda sayı1,sayı2:sayı1+sayı2
toplaYeni(100,300)

#Python'da anonim (isimsiz) fonksiyon oluşturma yöntemidir.
#def ile fonksiyon tanımlamaya alternatif, kısa ve tek satırlık fonksiyonlardır.
#Genellikle basit işlemler için kullanılır

carpma = lambda sayı1,sayı2,sayı3:sayı1*sayı2*sayı3
carpma(100,300,0)

import math
math.sqrt(64) # Kök alma

def karakokBul(x):
  return x**(1/2)

karakokBul(25)

math.factorial(5)

def faktoriyelHesapla(sayi):
  if sayi<=0:
    return 1
  else:
    return sayi * faktoriyelHesapla(sayi-1)

faktoriyelHesapla(5)

def faktoriyelHesapla2(n):
  faktoriyel = 1
  for i in range(1,n+1):
      faktoriyel *= i
  return faktoriyel # Bak

faktoriyelHesapla2(5)

"""Kendi örneklerim"""

mylist=["hello", "world",2,61]

mylist[:]

mylist[:2]

mylist[-1]

mylist[:-1]

mylist+mylist

mylist*3

ml=["Elms","Ali",22,61]

ml.index(61)

ml.count(61)

ml.count(1)

ml.append("Aferim")

ml

ml.remove(0)

ml.remove(22)

ml

renkler = ["kırmızı", "mavi", "sarı"]
del renkler[0:1]  # 0. indeksi siler
print(renkler)  # Çıktı: ["mavi", "sarı"]

renkler = ["kırmızı", "mavi", "sarı"]
del renkler[1]  # 0. indeksi siler
print(renkler)  # Çıktı: ["mavi", "sarı"]

renkler.reverse()

renkler

renkler.reverse()

renkler

renkler.extend("31")
renkler

renkler.extend(["Böyle eklenir"])

renkler

renkler.extend([122])
renkler

renkler.pop(0)

renkler

renkler.insert(0,"ali")
renkler

metin = "ahmet "

metin.replace("a","o")

"""
Fonksiyon	Açıklama	Örnek
upper()	Büyük harf	"abc".upper() → "ABC"

lower()	Küçük harf	"ABC".lower() → "abc"

count()	Karakter say	"aab".count('a') → 2

replace()	Değiştirme	"selam".replace('e','a') → "salam"

strip()	Boşluk sil	" hi ".strip() → "hi"
"""

car = "audi"
car.upper() == "audi"

a=int(input("Yaş gir: "))

if a<18:
  print("reşit değil")
  b=18
  print(f"Reşit değilsin maalesef {b}")
elif a==18:
  print("kıl payı reşit")
  b=19
else:
  print("reşit diilsin")

def user_profile(**user):
  print(f"Full name: {user['fname']} {user['lname']}")
  if 'age' in user:
    print(f"Age: {user['age']}")

user_profile(fname="Tobias", lname="Refsnes", age=25)

def ikiKatı(x):
  return x*2

def birCikar(x):
  return x-1
def kareAl(x):
  return x*x

import math as matematik

fonksiyonlarListesi=[
    ikiKatı,
    birCikar,
    kareAl,
    matematik.sqrt
]

sayi=5

for i in fonksiyonlarListesi:
  sayi=i(sayi)
  print(sayi)

def carp(a):
  def carpma (x):
    return x*a
  return carpma      #carp carpma fonk unun return ediyor

sonuc1=carp(1)
sonuc1(2)

liste=[0,1,2,3,4,5,6,7,8,9]
kareListe=[]

for i in liste:
  kareListe.append(i**2)

print(kareListe)

liste=[0,1,2,3,4,5,6,7,8,9]
def kareHesapla(x):
  return x**2
#kareHesapla(liste) #Hata veriyor.(Tek bir değer gidiyor igib düşünüyor bu yüzden hata veriyor.)
kareHesaplaSonuc=list(map(kareHesapla,liste))
kareHesaplaSonuc

kareHesaplaSonuc=tuple(map(kareHesapla,liste))
kareHesaplaSonuc

kareHesapla1=lambda x:x**2
kareHesaplaSonuc=list(map(kareHesapla,liste))
kareHesaplaSonuc

def carpmaYap(a):
  return lambda x: x*a

a = carpmaYap(10)
a(5)

from math import sqrt
sqrt(float(int("16")))

sqrt(int("16"))

from datetime import datetime
baslangıçZamanı=datetime.now()

isim=input("İsminizi Giriniz")
bitişZamanı=datetime.now()

gecenSure=bitişZamanı-baslangıçZamanı
print(gecenSure)

from datetime import datetime
baslangıçZamanı=datetime.now()

toplam=0
for i in range (1,10000):
  toplam+=i
  for j in range (1,10000):
    toplam+=j

bitişZamanı=datetime.now()

gecenSure=bitişZamanı-baslangıçZamanı
print(gecenSure)

"""# **EBOBU BULAN FONKSİYONU YAZINIZ**"""

sayı1=int(input("Lütfen ilk sayıyı giriniz: "))
sayı2=int(input("Lütfen ikinci sayıyı giriniz: "))

enKucukSayı=sayı1
if sayı2<sayı1:
  enKucukSayı=sayı2

for i in range(1,enKucukSayı+1):
  if sayı1%i==0 and sayı2%i==0:
    ebob=i

print("EBOB:",ebob)

"""Verilen listedeki elemanların 10 ile 20 arasında olan elamanların karelerinin toplamını bulunuz.
test listesi=[5,12,17,23,30,8,14]
cevap=629
"""

test_listesi=[5,12,17,23,30,8,14]

def karelerToplamı(liste):
  toplam=0
  for i in liste:
    if i>=10 and i<=20:
      toplam+=i**2
  return toplam

print(karelerToplamı(test_listesi))

def karelerToplamı2(sayılar):
  filtrelendi=filter(lambda x:10<= x <=20,sayılar)

  kareler=map(lambda x:x**2,filtrelendi)

  return sum(kareler)

test_listesi=[5,12,17,23,30,8,14]
sonuc=karelerToplamı2(test_listesi)
print(sonuc)

def yazdır():
  def yazıcı():
    print("Merhaba Dünya")
  return yazıcı

sonuc=yazdır()
sonuc()

#sonuc=yazıcı() #Hata veriyor.(Sadece yazdır adlı fonksiyon üzerinden çağırabiliriz.)
#sonuc

def carp(a):
  def carpma (x):
    return x*a
  return carpma


sonuc3=carp(3)


sonuc3(3)

liste=[0,1,2,3,4,5,6,7,8,9]
def kareHesapla(x):
  return x**2

kareHesaplaSonuc=list(map(kareHesapla,liste))
kareHesaplaSonuc

def ogrenci(*bilgiler):
  for i in bilgiler:
    print(i)

ogrenci=("Erhan","Kahveci","Bilgisayar Mühendisliği","Erzurum",22)
ogrenci

def yazdır():
  def yazıcı():
    print("Merhaba Dünya")
  return "Merhaba Dünya Metni" # Metin döndürülüyor

sonuc=yazdır()
sonuc
#sonuc=yazdır(): yazdır() fonksiyonu çağrılır. Fonksiyonun return ifadesi "Merhaba Dünya Metni" olduğu için, sonuc değişkenine bu metin atanır.
# Artık sonuc bir string değer tutmaktadır, bir fonksiyon değil.
#sonuc() şeklinde çağırırsak şayet
#sonuc(): Bu satırda, sonuc değişkenini bir fonksiyon gibi çağırmaya çalışıyorsunuz.
# Ancak sonuc bir string olduğu için, Python bir hata verecektir.
#Bu hatanın türü TypeError olacaktır ve kabaca "string nesnesi çağrılabilir değil" anlamına gelir.

"""## ***CLASSSS***"""

class Ogrenci:
  def yazdir(self):
    print("Python Class Ogreniyorum")

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
p1 = Person("ali", 12)
print(p1.name+ " " +str(p1.age))

"""str fonk kullanarak:"""

class Person1:
  def __init__(self,name,age):
    self.name=name
    self.age=age
  def __str__(self):
    return f"Adı:{self.name} yaşı: ({self.age}) "

p1=Person1("ali",12)
print(p1)

"""



yani str sayısal ifadeyi de kullandırttı"""

class ogrenci1:
  def yazdır(self):    #nesnelere erişmek için kullanıyoruz
    print("merhaba")
    print(self)    #print(self) satırı, bu o1 nesnesinin hafızadaki yerini (adresini) gösterir.

o1 = ogrenci1()
o1.yazdır()

print(ogrenci1)

print(o1)

class futbol:
  def gol(self,x):
    self.a=x     #self.a = x: x’in değeri nesneye ait a adlı bir özelliğe (değişkene) atanıyor.
  def yazdır(self):
    print(self.a)   #self.a = 5 oluyor sınavda sorar

f=futbol()
f.gol(5)

print(a)    #a adında global (genel) bir değişken arar ama bulamaz.

print(f.a)

f.a

a=10

id(a)   # bellekteki adresi verir

b=10

id(b)

class Test:
  def ekle(self):
    print(self)     # yine nesnenin kendisi yazdırılır.
    print(id(self))    #nesnenin benzersiz kimliği (RAM adresi gibi düşünebilirsin) yazdırılır.
    print("Eklendi")
t=Test()
print(t)     #t nesnesinin bellekteki yeri

print(id(t))    #t nesnesinin benzersiz kimliğini (ID) yani RAM’deki adresini temsil eden bir tamsayı verir.

t.ekle()

t2=Test()
print(t2)

class Test2:
  def ekle(self):
    print("Bu bir metottur")

  def çıkartma(self,a,b):
    print(a-b)
t1=Test2()
t2=Test2()

t1.ekle()

t1.çıkartma(10,2)

t2.çıkartma(1,9)

class Test3:
  def yaz1(self):
    print("Bu bir fonk")
  def degisken(self,a,b):
    self.x=a
    self.y=b
  def goster(self):
    print(self.x)
    print(self.y)

t1=Test3()
t2=Test3()

t1.yaz1()

t1.degisken(100,-50)

t1.goster()

t1.x

t1.y

t1.a  #???????????

class ogrenci:
  def __init__(self):
    print("Bu bir yapıcı metot")

o1=ogrenci()
#o1 = ogrenci() satırı yazıldığı anda, Python otomatik olarak şu işlemi yapar:
#1. Yeni bir nesne oluştur.
#2. __init__() metodunu çağır.

class ogrenci2:
  def __init__(self,x):
    self.y=x

o2=ogrenci2(20)

o2.y

class ogrenci3:
  def __init__(self,a,b):
    self.a=a
    self.b=b
o3=ogrenci3(50,100)

o3.a

o3.b

class toplama():
  def __init__(self,a,b):
    self.x=a
    self.y=b
  def topla(selfa):
    print("Toplam",selfa.x+selfa.y)

t1=toplama(10,20)
t1.topla()

class Teacher:
  def __init__(self,name='mete'):
    self.name=name
  def goster(self):
    print(self.name, "benim en sevdiğim hocam")

t1=Teacher()
t1.goster()

t2=Teacher("Ferhat")
t2.goster()

#Inheritance Kalıtım
class Windows7:
  def yazdır(self):
    print("Merhaba ben parent sınıfı içerisindeyim")

class Windows10(Windows7):     #w7 nin bütün özelliklerini kullanabilirsin artık
  def goster(self):
    print("Merhaba ben child içerisindeyim ")

x=Windows7()
x.yazdır()

y=Windows10()
y.yazdır()

y.goster()

x.goster()    #goster child sınıfının

class A:
  def __init__(self):
    print("A sınıfı yapıcı metodu çalıştı")
  def yazdır(self):
    print("A sınıfı yazdır metodu çalıştı")
class B(A):
  def __init__(self):
    print("B sınıfı yapıcı metodu çalıştı")
  def goster(self):
    print("B sınıfı yazdır metodu çalıştı")

x=A()

y=B()

class A:
  def __init__(self):
    print("A sınıfı yapıcı metodu çalıştı")
  def yazdır(self):
    print("A sınıfı yazdır metodu çalıştı")
class B(A):
  def goster(self):
    print("B sınıfı goster metodu çalıştı")

x=A()

class A:
  def __init__(self):
    print("A sınıfı yapıcı metodu çalıştı")
  def yazdır(self):
    print("A sınıfı yazdır metodu çalıştı")
class B(A):
  def __init__(self):
    A.__init__(self)    #A nın yapıcı metodu çalıştırılıyor manuel olarak
    print("B sınıfı yapıcı metodu çalıştı")
  def goster(self):
    print("B sınıfı yazdır metodu çalıştı")

x=A()

class A:
  def __init__(self):
    print("A sınıfı yapıcı metodu çalıştı")
  def yazdır(self):
    print("A sınıfı yazdır metodu çalıştı")

class B(A):
  def __init__(self):
    A.__init__(self)    # A'nın yapıcı metodu çalıştırılıyor manuel olarak
    print("B sınıfı yapıcı metodu çalıştı")
  def goster(self):
    print("B sınıfı yazdır metodu çalıştı")

y = B()
y.yazdır()

y=B()

class A:
  def A_yazdır(self):
    print("A yazdır")

class B(A):
  def B_yazdır(self):
    print("B yazdır")

class C(B):
  def C_yazdır(self):
    print("C yazıdr")

x=A()
y=B()
z=C()

x.A_yazdır()

z.C_yazdır()

x.B_yazdır()   #hata

z.A_yazdır()

print(C.__mro__)   #hangi class ın nerden geldiğini gösteriyor

class A:
  def A_yazdır(self):
    print("A yazdır")

class B(A):
  def B_yazdır(self):
    print("B yazdır")

class C(A):
  def C_yazdır(self):
    print("C yazıdr")

class D(B,C):
  def D_yazdır(self):
    print("D yazdır")

x=D()    #bütün sınıfların özelliklerine erişebiliriz

x.A_yazdır()

x.B_yazdır()

x.C_yazdır()

x.D_yazdır()

def topla(a,b):
  print(a+b)

def topla(a,b,c):
  print(a+b+c)

topla(100,200)     #aynı isimli tanımlanamaz ne fonk ne class

class A:
  def __init__(self):
    self.x="Yapıcı A"
  def goster(self):
    print(self.x)

class B:
  def __init__(self):
    self.x="Yapıcı B"
  def goster(self):
    print(self.x)

xx=A()
yy=B()

xx.goster()

yy.goster()

y.x

class A:
  def __init__(self,x,y):
    self.x=x
    self.y=y
  def __add__(self,diğer):     #add + operatörünü sınıf nesneleriyle kullanabilmek için tanımlanır.self → o1 nesnesidir diğer → o2 nesnesidir
    return A(self.x+diğer.x,self.y+diğer.y)

"""return A(self.x + diğer.x, self.y + diğer.y)




*  → return A(10 + 5, 20 + 10)

*  → return A(15, 30)


"""

o1 = A(10,20)

o2 = A(5,10)

o3=o1+o2    #Bu satır, şununla aynıdır:    o3 = o1.__add__(o2)

print(o3.x)

print(o3.y)

class araba():
  def __init__(self,motorgucu=200,vites=5):
    self.motorgucu=motorgucu
    self.vites=vites
  def araba_ozellikleri(self):
    print("Motor gücü: ", self.motorgucu)
    print("Vites: ", self.vites)


class opel(araba):
  def __init__(self,motorgucu=300,vites=6,cant=19):
    super().__init__(motorgucu,vites)#araba sınıfının __init__() metodunu çağırır.motorgucu ve vites özellikleri opel nesnesine kazandırılıyor.
    self.cant=cant
    print("Motor gücü: ",self.motorgucu)
    print("Vites: ",self.vites)
    print("Cant: ",self.cant)

o4=opel()

o4.araba_ozellikleri()

o1=opel(10,10,30)
#o1 = opel() yazsak varsayılan değerleri yazdırırdı

o1.araba_ozellikleri()

o2=araba()

o2.araba_ozellikleri()

o2.motorgucu

"""## **Kendi örneklerim**


"""

class calisan:
  def __init__(self,isim,soyisim,maas):
    self.isim=isim
    self.soyisim=soyisim
    self.maas=maas

calisan1=calisan("Ali","Ylm",22)
print(calisan1.__dict__)          #sözlük yapısında yazmayı sağlıyor

class Araba:
  def __init__(self,marka,model):
    self.marka=marka
    self.model=model

cs=Araba("Bugatti","Veyron")
print(cs.marka , cs.model)

class Insan:
  def __init__(self,ad):
    self.ad=ad

  def SelamVer(self):
    print(f"Merhaba selamın aleyküm {self.ad}")

cs=Insan("Ali")
cs.SelamVer()

class daire:
  def __init__(self,r):
    self.r=r

  def alanHesapla(self):
    return 3.14 * self.r ** 2

alan=daire(5)
print(alan.alanHesapla())

class Ogrenci:
  okul="17 Şubat"    #sınıf değişkeni
  def __init__(self,ad):
    self.ad=ad


ogr=Ogrenci("Ali")
print(ogr.okul)

class Hayvan:
  def ses(self):
    print("Ses çıkarıyor")

class Kopek(Hayvan):
  def havla(self):
    print("onlar arkadan HAV larlarlarlarrrrrrrğğğ")

c=Kopek()
c.ses()

c.havla()

class Film:
    def __init__(self, ad, yil):
        self.ad = ad
        self.yil = yil

    def __str__(self):
        return f"{self.ad} ({self.yil})"

f = Film("Inception", 2010)
print(f)  # Inception (2010)

"""Benim örneğim"""

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person("John", 36)

print(p1)

"""__str__ olmasıaydı

"""

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)
print(p1)


#adresi veriyor bize str siz
#__str__ metodu, bir sınıfın örneğini (nesnesini) string olarak daha okunabilir ve kullanıcı dostu şekilde temsil etmek için kullanılır.

"""KİTAPLık

"""

class Kitap:
  kitapSayisi=0

  def __init__(self,ad,yazar,sayfasayisi):
    self.ad=ad
    self.yazar=yazar
    self.sayfasayisi=sayfasayisi
    Kitap.kitapSayisi+=1

  def bilgiGoster(self):
    print(f"Kitabı Adı: {self.ad} Yazar: {self.yazar} Sayfa sayısı: {self.sayfasayisi}")


k1=Kitap("İnsan ne ile yaşamaz","Ali Yılmaz",61)
k2=Kitap("kellllilee ve dimne","Gene ali",16)

k1.bilgiGoster()

k2.bilgiGoster()

print(f"Kitap sayısı: {Kitap.kitapSayisi}")

"""Erhan sonrası"""

calisan1=["Bilgisayar Mühendisi","Mete",35,"Sennior",50000]
calisan1=["Bilgisayar Mühendisi","Hakan",25,"Junnior",45000]

class BilgisayarMuhendisi:
  ozellik="Python biliyorum"

  def __init__(self,isim,yas,pozisyon,maas):
    self.isim=isim
    self.yas=yas
    self.pozisyon=pozisyon
    self.maas=maas

calisan1=BilgisayarMuhendisi("Mete",35,"Senior",50000)
calisan2=BilgisayarMuhendisi("Hakan",25,"Junior",35000)# . ile özelliklere erişilebiliyor
calisan3=["Bilgisayar Mühendisi","Batu",40,"Junior",40000]

def code(calisan):
  return f'{calisan[1]} kodu yazmaktadır'

code(calisan3)

class BilgisayarMuhendisi0:
  ozellik="Python biliyorum"

  def __init__(self,isim,yas,pozisyon,maas):
    self.isim=isim
    self.yas=yas
    self.pozisyon=pozisyon
    self.maas=maas

  def code(self):
    return f'{self.isim} kodu yazmaktadır'

  def dil(self,language):    #neden self.language=language yapmadık.Sadece geçici olarak kullanacaksan, parametre olarak al ve direkt kullan. Eğer nesnenin bir özelliği olsun istiyorsan, self.language = language yap ve constructor’a ekle.
    return f'{self.isim} kodu {language} diliyle yazmaktadır.'

  def __str__(self):
    bilgi=f'İsim:{self.isim} -- Yas:{self.yas} -- Pozisyon:{self.pozisyon} -- Maaş:{self.maas}'
    return bilgi
  def __eq__(self,other):#İsimler ve yaşlar eşit mi diye bakıyor
    return self.isim==other.isim and self.yas==other.yas

  @staticmethod
  def YasaGoreMaas(yas):
    if yas<25:
      return 30000
    elif yas<35:
      return 40000
    else:
      return 50000

c1=BilgisayarMuhendisi0("Mete",35,"Senior",50000)
c2=BilgisayarMuhendisi0("Hakan",25,"Junior",40000)# . ile özelliklere erişilebiliyor

if c1==c2:
  print('Aynı')
else:
  print('Farklı')

c1.maas

c1.YasaGoreMaas(30)

BilgisayarMuhendisi0.YasaGoreMaas(30)#Direkt sınıf üzerinden de çağrılabiliyor

class Calisan:
  def __init__(self,isim,yas,maas):
    self.isim=isim
    self.yas=yas
    self.maas=maas
  def kisi(self):
    return f'{self.isim} adlı kişi çalışmaktadır.'

class YazilimMuh(Calisan):
  def __init__(self, isim, yas, maas,level):
    super().__init__(isim, yas, maas)  #Calisan sınıfının init ini kullandırtıyor. Git, Calisan sınıfındaki __init__ metodunu çağır ve ona bu 3 parametreyi gönder.
    self.level=level
  def kisi(self):
    return f'{self.isim} adlı kişi kodlamaktadır'

class Designer(Calisan):
  def cizer(self):
    return f'{self.isim} adlı kişi çizmektedir.'
  def kisi(self):
    return f'{self.isim} adlı kişi dizayn çalışmaktadır'

ym=YazilimMuh('Mete',35,50000,'CEO')
ym.isim

ym.level

ym.kisi()

#ym.dizayn()#Yazılıma ait değil hata verir

d=Designer('Batu',45,54254)
d.kisi()

d.cizer()

calisanlar = [
    YazilimMuh('Mete', 30, 50000, 'CEO'),
    YazilimMuh('Ferhat', 45, 60000, 'Junior'),
    Designer('Batu', 45, 55555)
]

def sonuclar(calisanlar:list):
  for i in calisanlar:
    print(i.kisi())
#sonuclar adında bir fonksiyon tanımlanıyor.
#Parametre olarak bir calisanlar listesi alıyor.
#Listenin içinde döngü ile (for i in calisanlar) her bir çalışan nesnesi alınır.
#Her nesnenin .kisi() metodu çağrılır ve sonucu ekrana yazdırılır.

sonuclar(calisanlar)

class SoftwareEngineer():
  def __init__(self,isim,yas):
    self.isim=isim
    self.yas=yas
    self.maas=None
    self.projeSayisi=0

  def proje(self):
    self.projeSayisi+=1

  def maasGetir(self):
    return self.maas

  def hesapla(self,deger):#Fonksiyon içerisinde fonksiyon çağırdık
    self.maas=self.maasHesapla(deger)

  def maasHesapla(self,deger):
    if self.projeSayisi<5:
      return deger
    elif self.projeSayisi <50:
      return deger*2
    else:
      return deger*5

se=SoftwareEngineer('Mete',35)

se.projeSayisi

se.maasGetir()   #none değer dönüyor

for i in range(70):   #70 proje ekleniyor
  se.proje()
#se.proje() metodu 70 kez çağrılıyor.
#Her çağrıda projeSayisi += 1
#Yani sonunda projeSayisi = 70

se.projeSayisi

se.hesapla(50000)

se.maasGetir()

"""SQL KISMI"""

import sqlite3  #sqlite modülünü içe aktarıyoruz

conn = sqlite3.connect("/content/ogrenci.db")   #klasördeki yolu kopyalayıp buraya yapıştırdık

#Tablo oluşturma
conn.execute('''CREATE TABLE ogrenci_detay2
(ID INT PRIMARY KEY NOT NULL,
NAME TEXT NOT NULL,
AGE INT,
ADDRESS BLOB,
BURS REAL);
''')

conn.close()   #çıkış yaptık

conn.execute("INSERT INTO ogrenci_detay2 VALUES (900, 'Mete', 40, 'İstanbul', 1000.00 )") #hata veriri çıkış yaptığımızdan

conn = sqlite3.connect("/content/ogrenci.db")   #tekrar giriş yaptık

conn.execute("INSERT INTO ogrenci_detay2 VALUES (900, 'Mete', 40, 'İstanbul', 1000.00 )")

conn.commit()   #Veritabanında yaptığın değişiklikleri kalıcı olarak kaydeder. Komit atmadan close dersen kayıt olmaz değişiklikler

conn.execute("INSERT INTO ogrenci_detay2 VALUES (901, 'Ferhat', 50, 'Trabzon', 3000.00 )")
conn.execute("INSERT INTO ogrenci_detay2 VALUES (902, 'Batu', 45, 'Erzurum', 2000.00 )")
conn.commit()

data = conn.execute("SELECT * FROM ogrenci_detay2")
for i in data:
  print("ID:",i[0])
  print("ISIM:",i[1])
  print("YAŞ:",i[2])
  print("ADRES:",i[3])
  print("MAAS:",i[4],"\n")

conn.execute("INSERT INTO ogrenci_detay2 VALUES (903, 'Buket', 25, 'Trabzon', 3000.00 )") #yeni kayıt ekledik

data = conn.execute("SELECT * FROM ogrenci_detay2")
for i in data:
  print("ID:",i[0])
  print("ISIM:",i[1])
  print("YAŞ:",i[2])
  print("ADRES:",i[3])
  print("MAAS:",i[4],"\n")

conn.execute("UPDATE ogrenci_detay2 SET BURS = 4000.00 WHERE ID = 903")   #güncelleme
conn.commit()

data = conn.execute("SELECT * FROM ogrenci_detay2")
for i in data:
  print("ID:",i[0])
  print("ISIM:",i[1])
  print("YAŞ:",i[2])
  print("ADRES:",i[3])
  print("MAAS:",i[4],"\n")

conn.total_changes
#şimdiye kadarki yapılan değişkliklerin sayısını verir

conn.execute("UPDATE ogrenci_detay2 SET BURS = 1000.00 WHERE ID = 903")   #komit yok, şimdi çıkış yaparsak bu değişiklik gider

conn.total_changes

conn.execute("DELETE FROM ogrenci_detay2 WHERE ID = 903")   #silme işlemi
conn.commit()

data = conn.execute("SELECT * FROM ogrenci_detay2")
for i in data:
  print("ID:",i[0])
  print("ISIM:",i[1])
  print("YAŞ:",i[2])
  print("ADRES:",i[3])
  print("MAAS:",i[4],"\n")

conn.close()   #çıkış yaptık

import requests
import lxml.html
import pandas as pd

data = requests.get("https://www.w3schools.com/html/html_tables.asp")

data

data2 = lxml.html.fromstring(data.text)

tablo =data2.xpath('//table')[0]

tablo.getchildren()

len(tablo.getchildren())

tablo.getparent()

data ={

       "Company"  :[],
       "Contact" :[],
       "Country"  :[]
}

for i in tablo.getchildren()[1:7]:
  data["Company"].append(i.getchildiren()[0].text_content())
  data["Contacct"].append(i.getchildiren()[1].text_content())
  data["Country"].append(i.getchildiren()[2].text_content())

pd_tablo.info()

for i in pd_tablo.itertuples():
  print(i)

for i in pd_tablo.itertuples():
  print(i[1:])

import sqlite3

conn = sqlite3.connect("/content/musteri.db")

conn.execute("""
CREATE TABLE pd_tablo2(Company,Contact,Country)
""")

for i in pd_tablo.itertuples():
  insert_table="""
  INSERT INTO pd_tablo2 VALUES(?,?,?)
  """
  conn.execute(insert_table,i[1:])
  conn.commit()

dataYeni=conn.execute("SELECT * FROM pd_tablo2")
for i in dataYeni:
  print("Company =" ,i[0])
  print("Contact =" ,i[1])
  print("Country =" ,i[2], "\n")



"""////////////////////"""

import sqlite3

conn = sqlite3.connect("ornek.db")
c = conn.cursor()

# Tablo oluşturma
c.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER
)
''')
conn.commit()

# Kullanıcı ekleme
def add_user(name, age):
    with conn:
        c.execute("INSERT INTO users(name, age) VALUES (?, ?)", (name, age))

# Kullanıcı güncelleme
def update_user(user_id, name, age):
    with conn:
        c.execute("UPDATE users SET name=?, age=? WHERE id=?", (name, age, user_id))

# Kullanıcı silme
def delete_users(user_id):
    with conn:
        c.execute("DELETE FROM users WHERE id=?", (user_id,))

# Tüm kullanıcıları alma
def get_users():
    c.execute("SELECT * FROM users")
    return c.fetchall()

# Örnek kullanım
add_user("Mete", 40)
add_user("Ferhat", 44)
update_user(1, "Mete Yagan", 39)

# Sonuçları yazdır
for user in get_users():
    print(user)

