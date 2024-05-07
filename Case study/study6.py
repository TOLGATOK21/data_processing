"""Görev 6: Aşağıda verilen listede mühendislik ve tıp fakülterinde dereceye giren öğrencilerin isimleri
bulunmaktadır. Sırasıyla ilk üç öğrenci mühendislik fakültesinin başarı sırasını temsil ederken son üç öğrenci de 
tıp fakültesi öğrenci sırasına aittir. Enumarate kullanarak öğrenci derecelerini fakülte özelinde yazdırınız"""

ogrenciler = ["Ali", "Veli","Ayşe","Talat","Zeynep","Ece"]

for index,student in enumerate(ogrenciler):
    if index<=2:
        print("Mühendislik fakültesi " + str(index+1) + "." "öğrenci: " + ogrenciler[index])

    else:
        print("Tıp fakültesi " + str(index+1) + "." "öğrenci: " + ogrenciler[index])

