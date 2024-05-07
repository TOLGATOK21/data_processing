#Görev 3: Verilen listeye aşağıdaki adımları uygulayınız.






list =["D","A","T","A","S","C","I","E","N","C","E"]
#Adım 1: Verilen listenin eleman sayısına bakınız.
print(len(list))
#Adım 2: Sıfırıncı ve onuncu indeksteki elemanları çağırınız.
print(list[0],list[10])
#Adım 3: Verilen liste üzerinden ["D", "A", "T", "A"] listesi oluşturunuz.
data_list = []
data_list.append(list[0:4])
print(data_list)

#Adım 4: Sekizinci indeksteki elemanı siliniz.
list.pop(8)
print(list)

#Adım 5: Yeni bir eleman ekleyiniz.
list.append("yeni eleman")
print(list)

#Adım 6: Sekizinci indekse "N" elemanını tekrar ekleyiniz

list.insert(8,"N")
print(list)
