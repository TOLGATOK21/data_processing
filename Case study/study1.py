#Görev 1: Verilen değerlerin veri yapılarını inceleyiniz.
x =8 
y =3.2
z=8j + 18
a ="Hello World"
b = True
c = 23<22
l = [1,2,3,4]
d={"Name":"Jake",
   "Age":27,
   "Adress":"Downtown"}

t = ("Machine Learning","Data Science")
s = {"python", "Machine Learning","Data Science"}
#----------------------------------------------------

def type_of(list):
    for i in list:
        print(f"Type of {i}",type(i))

list = [x,y,z,a,b,c,l,d,t,s]

type_of(list)