dict = {"Christian": ["America",18],
        "Daisy": ["England",12],
        "Antonio": ["Spain",22],
        "Dante": ["ıtaly",25]}

#Adım 1: Key değerlerine erişiniz.
print(dict.keys())
#Adım 2: Value'lara erişiniz.
print(dict.values())
#Adım 3: Daisy key'ine ait 12 değerini 13 olarak güncelleyiniz.
dict.update({"Daisy":["England",13]})
print(dict)
#Adım 4: Key değeri Ahmet value değeri [Turkey,24] olan yeni bir değer ekleyiniz.
dict.update({"Ahmet":["Turkey",24]})
#Adım 5: Antonio'yu dictionary'den siliniz.
dict.pop("Antonio")
print(dict)
