# 38.	Напишите программу, удаляющую из текста все слова содержащие "абв".


string01 = "ппвпрврвов рвыпабввыав арок абвгдеи светлана"
list01 = string01.split()
print(list01)
for item in list01:
  if "абв" in item:
   list01.remove(item)
print(item)
#string02 = str(list01)
string02 = (",".join(map(str, list01)))
print(string02)