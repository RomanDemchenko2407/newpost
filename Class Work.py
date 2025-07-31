#dictionari-lug'atlar bilan ishlaydi->{"hi":"salom"}
#nimadur=dict() #1-usul lugat yaratish
#nimadur={} #2-isul lugat yaratish
# Dictionary --> key, value
# import random
# from curses.ascii import isdigit
# from multiprocessing.process import parent_process
# from secrets import choice
#
# from wheel.cli.convert import parse_wininst_info
#
# import random

# nimadir = {
#     "ism":"Roman",
#     "familiya":"Demchenko",
#     "yosh":15
# }
# print(nimadir)
# # print(type(nimadir))
# name = nimadir['ism']  #name = "Roman"
# print(name)
# print(type(name))


#1-zadacha
# nimadur={
#     "name":"Roman",
#     "age":15,
#     "sity":"Termez"
# }
# print(nimadur)
# yosh=nimadur["age"]
# print(yosh)

#2-zadacha
# produkt={
#     'name':'Laptop',
#     'brand':'Dell'
# }
# print(produkt)
# produkt.setdefault("price",12000)
# print(produkt)- добавляет ещё одно значение к(produkt) или каким либо другим объуктам

#3-zadacha
# nimadur={
#     "name":"Roman",
#     "age":15,
#     "sity":"Termez"
# }
# print(nimadur)
# del nimadur["sity"]
# print(nimadur)      #Помогает убрать какой либо пункт из написанного

#4-zadacha
# person={
#     'name':'Roman',
#     'age':15,
#     'city':'Termez'
# }
# print(person)
# mail=person.get("email"), "Mavjut emas"
# print(mail)   #Помогает проверить есть ли такой пункт или нет

#5-zadacha
# if person==("email"):
#     print("mavjut")
# else:
#     print("mavjut emas")---> # Тот же самый принцип что и в 4 задаче

#6-zadacha
# rezume={
#     'name':'Ali',
#     'age':25,
#     'city':'Tashkent'
# }
# print(rezume)
# rezume.setdefault("email","unkonown@gmail.com")
# print(rezume)

# for key,value in rezume.items():
#     print(f"key:{key}")
#     print(f"value:{value}")


# student={
#     "name":"Jahongir",
#     "grades":[90,85,78,92]
# }
# print(len(student["grades"]))
# print(sum(student["grades"]))
# print(f"345/4={345/4}")






# kartalar = {}
#
# def bankomat_menu(parol):
#     print(f"""===Bankomat===
# 1.Balans ko'rish
# 2.Pul yechish
# 3.Hisobni to'ldirish
# 4.Ortga(Asosiy Menyu""")
#
#     tanlov = input("Son kiriting (1-4): ")    #kartalar[parol]
#     if tanlov == "1":
#         print(f"Sizninghisobingizdagi balans: {kartalar[parol]}")
#     elif tanlov == "2":
#         money = int(input("Summani kiriting: "))
#         if money <= kartalar[parol]:
#             kartalar[parol] -= money
#             print(f"Pul yechildi. Yangi balans: {kartalar[parol]}")
#         else:
#             print("Hisobingizda yetarli mablag' yo'q.")
#
#     elif tanlov == "3":
#         hisob = int(input("Qancha to'ldirmoqchisiz?: "))
#         if hisob > 0:
#             kartalar[parol] += hisob
#             print(f"Hisobingiz to'ldirildi. Yangi balans: {kartalar[parol]}")
#         else:
#             print("Noto'g'ri summa.")
#
#     elif tanlov == "4":
#         print("Asosiy menuga qaytingiz")
#     else:
#         print("Bunday tanliv mavjut emas")
#     bankamatga_kirish()
#
# def bankamatga_kirish():
#     parol=input("\n💳Karta parolini kiriting: ")
#     if 999 < int(parol) <= 9999:
#         if parol in kartalar:
#             print("Karta topilgan")
#             bankomat_menu(parol)
#         else:
#             print("Karta mavjud emas")
#     else:
#         print("Bu 4 xonali parol emas!")
#
#
#         main_menu()
#
# def main_menu():
#     print("""===Asosiy Menyu===
# 1.🏧Bankomat
# 2.🏢Bank
# 3.✨Dasturdan chiqish""")
#     choice=input("Tanlang (1-3): ")
#     if choice == "1":
#         bankamatga_kirish()
#     elif choice == "2":
#         bank_menu()
#     elif choice == "3":
#         print("Dasturdan chiqildi,xayr.")
#     else:
#         print("Bunday menyu yo'q")
#
#
#
# def bank_menu():
#     print("""===Bank Menyusi===
# 1.✍Parolni qo'lda yozish
# 2.🖥 Avtomanik parol qoyish: """)
#     vibor=input("Tanlang(1-2): ")
#
#     if vibor=="1":
#         qol_parol=input("Yangi parol kiriting: ")
#         if 1000<int(qol_parol)<1000000:
#             print(f"Yangi karta yaratildi!Parol:{qol_parol} ")
#             kartalar[qol_parol]=0
#             main_menu()
#         else:
#             print("4 xonali sonlardan foydalang!")
#
#
# main_menu()





#15.04.2025

# import random
# random_son=random.randint(1,100)
# def random():
#     son=0
#     son=+1
#     while son<10:
#         kiritish=int(input("Son kiriting(1,100): "))
#         if random_son==kiritish:
#             print("Togri toptingiz!"
#                   f"Urinishlar soni {son}")
#             ball=50 - (son-1)*5
#             print(f"Sonning balingiz: {ball}")
#             break
#         elif random_son<kiritish:
#             print(f"{kiritish} dan pasroq")
#         else:
#             print(f"{kiritish} dan yuqoriroq")
# print(random())


#random--->tasodifiy son
# import random
#
# son=random.randint(1,50)
# print(son)


# print(ord("A")) # funksiya berilgan narsani kodini chiqarib beradi
# print(ord("y"))

# print(ord("🖥"))
# print(">>>>>>>")
# print(chr(128421))



# shifrlash=input("Shifirlaysizmi?[ha/yoq]: ")
# matn=input("matinni kiriting: ")
# shifr=int(input("Nechi marta siljisin: "))

# empty=""
# if shifrlash== "ha":
#     for i in matn:
#         empty=empty + chr(ord(i)+ shifr)
# elif shifrlash == "yoq":
# else:
#     for i in matn:
#         empty= empty +chr(ord(i)- shifr)
#
#
#     print(f"Natija>>>{empty}")


#CLASS- 2 tipa - hususiyat - metod

# class cars:
#     def __init__(self,rang,model,eshiklar):
#         self.model=model
#         self.rang=rang
#         self.eshiklar=eshiklar
#
# cars1=cars("qora","Cobalt",4)
# print(cars1.model)
# print(cars1.rang)
# print(cars1.eshiklar)


# def count_code(str):
#   count=0
#   for index in range(len(str)):
#     if str[index]=="C" and str[index+3]=="e":
#            cound+=1
#     if index ==len(str)-4:
#       break
#   return count


#OOP
# class Talaba:
#     def __init__(self,ism,familiya,kurs):
#         self.ism=ism
#         self.familiya=familiya
#         self.kurs=kurs
#
#     def get_info(self):
#         return f"ism:{self.ism}, familiya:{self.familiya}, kurs:{self.kurs}"
#
#     def get_ism(self):
#         return self.ism
#
# talaba1=Talaba("Roman","Demchenko",2)
# talaba2=Talaba("Adham","Qosimov",2)


# print(talaba1.get_info())
# print(talaba2.get_info())



# class Odam:
#     def __init__(self,name,surname,passport):
#         self.name=name
#         self.surname=surname
#         self.passport=passport
#
#     def get_ism(self):
#        return self.name
#
#     def get_surname(self):
#        return self.surname
#
#     def get_passport(self):
#            return self.passport
#
# odam1=Odam('Roman','Demchenko','AD 26341828')

# print(odam1.get_surname())
# print(odam1.name)


# class Talaba(Odam):
#     def __init__(self,name,surname,passport,id_raqam):
#         super().__init__(name,surname,passport)
#         self.id_raqam=id_raqam
#
# Talaba1=Talaba('Roman','Demchenko','AD 226040588')


#OOp-Tamoilari - 4 ta
#1)inheritance- vorislik
#2)encapsulation-kapsulaga olish
#3)poliformizm-bilmiman
#4)abstraktion-abstrakt classlar


#encapsulation

# class Talaba:
#     def __init__(self,ism,familiya,passport):
#         self.ism=ism
#         self.familiya=familiya
#         self.__passport=passport
#
#     def get_ism(self):
#         return self.ism
#
#     def set_ism(self,new_ism):
#         self.ism=new_ism
#
#     def set_passport(self,new_passport):
#         self.__passport=new_passport
#
#     def get_passport(self,):
#         return self.__passport
#
# talaba1=Talaba("Roman","Demchenko","AD56248978")
# print(talaba1.get_ism())
# talaba1.set_ism("Jahongir")
# print(talaba1.get_ism())
# print(talaba1.get_passport())
# talaba1.set_passport("AD15748239")
# print(talaba1.get_passport())


# class Avtozavod:
#     def __init__(self,type,model,color):
#         self.type=type
#         self.model=model
#         self.color=color
#
#     def info(self):
#         text=(f"Moshinalarning turi: {self.type}\n"
#               f"Moshinaning modeli:{self.model}\n"
#               f"moshinaning rangi:{self.color}")
#         return text
#
# avto1=Avtozavod("yengil","KIA","silver")
#
# class Avto(Avtozavod):
#     def __init__(self,type,model,color,price):
#         super().__init__(type,model,color)
#         self.price=price
#
#     def info(self):
#         text=(f"Moshinalarning turi: {self.type}\n"
#               f"Moshinaning modeli:{self.model}\n"
#               f"Moshinaning rangi:{self.color}\n"
#               f"Moshinaning narxi:{self.price}")
#         return text
#
# car1=Avto("yengil","Haval","Red",15000)
# print(car1.info())





















