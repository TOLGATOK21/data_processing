#Görev 8: Aşağıda 2 adet set verilmiştir. Sizden istenilen eğer 1. küme 2. kümeyi kapsiyor ise ortak elemanlarını
#eğer kapsamıyor ise 2. kümenin 1. kümeden farkını yazdıracak fonksiyonu tanımlamanız beklenmektedir

kume1 = set(["data","python"])
kume2 = set(["data","function","qcut","lambda","python","miuul"])

def kume(set1,set2):
    if set1.issuperset(set2):
        print(set1.intersection(set2))

    else: 
        print(set2.difference(set1))

kume(kume1,kume2)