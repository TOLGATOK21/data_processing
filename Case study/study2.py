#Görev 2: Verilen string ifadenin tüm harflerini büyük harfe çeviriniz. Virgül ve nokta yerine space koyunuz, 
#kelime kelime ayırınız

text ="The goal is to turn data int information, and information into insight."
print(text.upper().replace(","," ").replace("."," ").split())