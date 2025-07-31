#1-topshiriq
#1
# matn = input("matn kiriting: ")
# shifrlash = input("1.Shifrlaysizmi?\n2.Deshifrlaysizmi?: ")
# shift = int(input("nechchi marta siljisin: "))
# for i in matn:
#     print(chr(ord(i) + 3), end="")
#
# empty = ""
# if shifrlash == "1":
#     for i in matn:
#         empty = empty + chr(ord(i) + shift)
# elif shifrlash == "2":
#     empty = ""
#     for i in matn:
#         empty = empty + chr(ord(i) -shift)
#
# print(f" >>>>>{matn}")


#2-topshiriq

# 1-misol
# class Vehicle:
#     def __init__(self,make,model,year):
#         self.make=make
#         self.model=model
#         self.year=year
#
#     def display_info(self):
#         info=(f"Moshinni markasi:{self.make}\n"
#     f"moshinni modeli:{self.model}\n"
#     f"moshinni chiqgan_yili:{self.year}")
#           return info
#
# car1=Vehicle('Chevralet','Cobalt',2024)
#
# print(car1.display_info())
#
# class Car(Vehicle):
#     def __init__(self,make,model,year,num_doors):
#         super().__init__(make,model, year)
#         self.num_doors=num_doors
#
#     def display_info(self):
#         text=(f"Moshinni markasi:{self.make}\n"
#               f"Moshinaning modeli:{self.model}\n"
#               f"Moshinaning rangi:{self.year}\n"
#               f"Moshinaning narxi:{self.num_doors}")
#         return text
#
# car3=Car('Chevralet','Spark',2020,4)
# print(car3.display_info())
#
#
#
# class Motorcycle(Vehicle):
#     class Car(Vehicle):
#         def __init__(self, make, model, year, rang):
#             super().__init__(make, model, year)
#             self.rang = rang
#
#         def display_info(self):
#             text = (f"Motorcycle markasi:{self.make}\n"
#                     f"Motorcycle modeli:{self.model}\n"
#                     f"Motorcycle rangi:{self.year}\n"
#                     f"Motorcycle narxi:{self.rang}")
#             return text
# Motorcycle1=Motorcycle('Kavasaki','nimadir modeli',2020,'Qora')
# print(Motorcycle1.display_info())














