#Görev 5: Argüman olarak bir liste alan, listenin içerisindeki tek ve çift sayıları ayrı listelere atayan ve bu listeleri
#return eden fonksiyon yazınız

list = [2,13,18,93,22]


def func(list):
    even_list=[]
    odd_list =[]
    for i in list:
        if i % 2 ==0:
            even_list.append(i)
        else:
            odd_list.append(i)
    print("The even number is" , even_list)
    print("The odd number is" , odd_list)

func(list)

