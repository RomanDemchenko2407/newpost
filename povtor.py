# # funksiyalar - 3 ga bo`linadi
# # 1)parametr qabul qilmaydi va qiymat qayarmaydi
# # 2)parametr qabul qiladi va qiymat qaytarmaydi
# # 3)parametr qabul qiladi/qilmaydi va qiymat qaytaradi
# from json.encoder import \
#     encode_basestring_ascii
#
# # 1.parametr qabul qilmaydi va qiymat qaytarmaydi
#
# def salom_ber():
#     print("Assalomu alaykum")
#
#
# # 2.parametr qabul qiladi va qiymat qaytarmaydi
# def salom_de(name):
#     print(f"Assalomu alaykum {name}")
#
#
#
#
# # 3.parametr qabul qiladi/qilmaydi va qiymat qaytaradi
# def salom_ayt(name):
#     return f"Assalomu alaykum {name}"
#
# qiymat = salom_ayt("Jaloliddin")
# print(qiymat)
#
#
# def yigindi(a, b):
#     return a+b
# #
# #
# mylist = []
# sum_ = yigindi(b=36, a=12)
# mylist.append(sum_)
# print(mylist)
#
# # *args
# def yigindi(*telefon):
#     print(telefon)
#     print(type(telefon))
#     yigindi = sum(telefon)
#     print(f"Yig'indi: {yigindi}")
#
# yigindi(2, 4, 5, 11, 13, 15)
#
#
#
# # **kwargs
# def malumotlar(**kwargs):
#     print(kwargs)
#     print(type(kwargs))
#     print(kwargs.items())
#
# malumotlar(ism = 'Jahongir', familiya = 'Omonov', yosh = 27)
#
# def tashqi():
#     print("tashqi")
#
#     def ichki():
#         print("ichki")
#
#     ichki()
# #
# #
# tashqi()
#
#
#
# sonlar = list(range(1, 11))
# print(sonlar)
#
# def sonlar_royhati(start, end, step=0):
#     if end > start:
#         pustoy = []
#
#         while start != end:
#             pustoy.append(start)
#             if step > 1:
#                 start += step
#             else:
#                 start+=1
#         return pustoy
#     else:
#         return "Parametrlar noto'g'ri kiritildi!"
#
#
# xx = sonlar_royhati(1, 11, 2)
# print(xx)
#
# names = ['Suhrob', 'Jasur', 'Eshboy', 'Jahongir']
# def student_baholari(names: list):
#     baholar = {}
#     for ism in names:
#         baho = int(input(f"{ism}ning bahosini kiriting: "))
#         baholar.setdefault(ism, baho)
#     return baholar
#
# xx = student_baholari(names)
# print(xx)
