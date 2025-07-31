#2-oy. 1-Home Work
# from operator import index

#1-savol
# home={}
# print(home)
# print(type(home))

#2-savol
# ism={
#     "name":"Jahongir"
# }
# print(ism)

#3-savol
# ism={
#     "name":"Jahongir",
#     "sity":"Termez",
#     "age":27
# }
# print(ism)
# del ism ["name"]
# print(ism)

#4-savol
# uzunlik={
#     "name":"Demchenko",
#     "age":15
# }
# print(len(uzunlik))

#5-savol
# my_dict={"name":"Jahongir","age":27}
# print(len(my_dict))

# 6-savol
# somlar={
#     1,2,3,
#     4,5,6
# }
# print(somlar)
# somlar.remove(3)
# print(somlar)

#7-savol
# my_list=[10,20,30,40]
# my_list.pop()
# print(my_list)

#8-savol
# info={
#     "name":"Jahongir",
#     "age":27
# }
# print(info)
# yosh=info.get("age"),"bor"
# print(yosh)

#9-savol
# person = {
#     "name": "Sardor",
#     "age": 12,
#     "city": "Toshkent"
# }
# print(len(person))

#10-savol
# info={
#     'name':'Roman',
#     'age':16,
#     'city':'Termez'
# }
# print(info)
# gorod=info.get('city')
# print(gorod)

#11-savol
# nimadur={
#     'name':'Sobirjon',
#     'age':25
# }
# print(nimadur)
# chtoto=nimadur.get('country'), "Noma'malum"
# print(chtoto)

#12-savol
# nimadur={
#     'Name':'Ali',
#     'age':25
# }
# print(nimadur)
# nimadur["age"]= 30
# print(nimadur)

#13-savol
# information={
#     "name":"Boyqo'zi",
#     "age":25,
#     "city":"Toshkent"
# }
# print(information)
# info=information.pop("city")
# print(info)

#14-savol
# nimadur={
#     "name":"Ali",
#     "age":25
# }
# print(nimadur.keys())

#15-savol
# nimadir={
#     'name':'Ali',
#     'age':25
# }
# print(nimadir.values())

#16-savol
# nimadir={
#     'name':'Ali',
#     'age':25
# }
# print(nimadir.values())

#17-savol
# nimadir={
#     'name':'Ali',
#     'age':25
# }
# print(nimadir)
# print(nimadir.items())

#18-savol
# person = {
#     "name": "Ali",
#     "age": 25
# }
# person.clear()
# print(person)

#19-savol
# nimadir={
#     'name':'Ali',
#     'age':25
# }
# print(nimadir)
# print(nimadir.popitem())

#20-savol
# nimadir={
#     'name':'Ali',
#     'age':25
# }
# print(nimadir)
# print(nimadir.copy())

#21-savol
# nimadir={
#     'name':'Ali',
#     'age':25,
#     'city':'Toshkent'
# }
# print(nimadir)
# print(nimadir.update({"city": "Toshkent"}))

#22-savol
# person = {
#     "name": "Ali",
#     "age": 25
# }
# person.update({"city": "Toshkent"})
# print(person)


#2-oy, 3-darsni

#1-savol
# text="python dasturlash tili"
# print(text.upper())

#2-savol
# matn="HELLO WORLD"
# print(matn.lower())

#3-savol
# matn="salom dunyo"
# print(matn.capitalize())

#4-savol
# matn="bu yerda hamma narsalar ajoyib"
# print(matn.title())

#5-savol
# matn=" Bugun juda yaxshi kun! "
# print(matn.strip())

#6-savol
# matn="banana va anor"
# matn2=matn.replace("a","o")
# print(matn2)

#7-savol
# matn="elementar elektronika"
# e_harf=matn.count("e")
# print(e_harf)

#8-savol
# text="Python hello world"
# print(text.count("hello"))

#9-savol
# matn="PyThOn DaStUrLaSh TiLi"
# print(matn.swapcase())

#10-savol
# matn="Salom, qanday yuribsiz?"
# print(matn.startswith("Salom"))

#11-savol
# matn="Hayot go'zal, dunyo"
# print(matn.endswith("dunyo"))

#12-savol
# matn="Python123"
# print(matn.isalpha())

#13-savol
# matn="Kodlash"
# print(matn.isalpha())

#14-savol
# matn="1234"
# print(matn.isalnum())

#15-savol
# matn="    "
# print(matn.isspace())

#16-savol
# matn="python is the best"
# print(matn.islower())

#17-savol
# matn="HELLO FREANDS"
# print(matn.isupper())

#18-savol
# matn="This Is A Test"
# print(matn.istitle())

#19-savol
# matn="Men Python o'rganmoqdaman"
# javob="python" in matn.lower()
# print(javob)

#20-savol
# matn = "Bu yerda nechta bo'sh joy bor?"
# print(matn.count(" "))

#21-savol
# matn="kompyuter"
# print(matn.index("o"))

#22-savol
# matn="Men bugun juda baxtliman"
# print(matn.replace(" ","-"))

#23-savol
# matn="Bu matnning oxirida nuqta bor."
# print(matn.rstrip("."))



# home work
#1-savol
# ism=input("Ismingizni kiriting: ")
# print(ism.upper())

#2-savol
# suz=input("Matinni kiriting: ")
# if suz=="Python":
#     print("Zo'r")
# else:
#     print("Qayta urinip ko'ring")

#3-savol
# sonlar=int(input("Sonni kiriting: "))
# if sonlar %2 == 0:
#     print("Bu juft son")
# else:
#     print("Bu toq son")

#4-savol
# for i in range (1,11):
#     print(i)

#5-savol
# total=0
# for i in range(5,16):
#     total+=i
# print("Yigindisi: ", total)

#6-savol
# soz = input("Ixtiyoriy so'z kiriting: ")
# for harf in soz:
#     print(harf)

#7-savol
# matn="ananas,anor,avakado"
# print(matn.replace("a","@"))

#8-savol
# matn=input("Raqamli matn kiriting: ")
# if matn.isdigit():
#     print("Matn faqat raqamdan iborat")
# else:
#     print("Harifdan tashqari boshqa belgi ham bor")

#9-savol
# yosh=int(input("Yoshingizni kiriting: "))
# if yosh<18:
#     print("Holi yosh ekansiz")
# else:
#     print("Hush kelipsiz")

#10-savol
# matn="assalomu aleykum hurmatli ustoz"
# print(matn.title())

#11-savol
# isimlar=[]
# for i in range(5):
#     ism=input(f"{i+1}-ismni kiriting: ")
#     isimlar.append(ism)
#
# print("Kiritilgan isimlar ro'yhati",isimlar)

#12-savol
# isimlar=[]
# for i in range(5):
#     ism=input(f"{i+1}-ismni kiriting: ")
#     isimlar.append(ism)
#     isimlar.sort()
# print("Kiritilgan isimlar ro'yhati",isimlar)

#13-savol
# ismlar=["Adham","Jahongir","Abror","Sherzod","Jaloliddin"]
# print("Ro'yhatda",len(ismlar),"ismlar bor")

#14-savol





# Uy work OOP

#2-misol

# class Student:
#     def __init__(self,ism,yosh,kurs):
#         self.ism = ism
#         self.yosh=yosh
#         self.kurs=kurs
#     def get_ism(self):
#         return self.ism
#     def get_kurs(self):
#         return self.yosh
#     def get_yosh(self):
#         return self.kurs
#
# student1=Student('Roman',16,'Backend')
# print(student1.get_ism())
# print(student1.get_yosh())
# print(student1.get_kurs())

#3-misol
# class Book:
#     def __init__(self,nomi,muallifi,sahifalar_soni):
#         self.nomi=nomi
#         self.muallifi=muallifi
#         self.sahifalar_soni=sahifalar_soni
#     def get_nomi(self):
#         return self.nomi
#     def get_muallifi(self):
#         return self.muallifi
#     def get_sahifalar_soni(self):
#         return self.sahifalar_soni
#
# Kitobxona=Book('Matematika','i dont know',150)
#
# print(Kitobxona.get_nomi())
# print(Kitobxona.get_muallifi())
# print(Kitobxona.get_sahifalar_soni())

#4-misol
# class House:
#     def __init__(self,manzil,xonalar_soni,narxi):
#         self.manzil=manzil
#         self.xonalar_soni=xonalar_soni
#         self.narxi=narxi
#     def get_manzil(self):
#         return self.manzil
#     def get_xonalar_soni(self):
#         return self.xonalar_soni
#     def get_narxi(self):
#         return self.narxi
#
# Uylar=House('Yubileyniy','5','1000000000')
#
# print(Uylar.get_manzil())
# print(Uylar.get_xonalar_soni())
# print(Uylar.get_narxi())

#5-misol










# def reverse_encrypt(text):
#     return text[::-1 ]
# sentence= input("sozni kiriting: ")
# print("shifirlangan",reverse_encrypt(sentence))





























