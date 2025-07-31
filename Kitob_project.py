# kitoblar=[]
# userlar={}
# location=False
# login_fornow=''
#
#
# import psycopg2
# def get_connection():
#     return psycopg2.connect(
#         dbname='kutubxona_db',
#         user='postgres',
#         password='240709',
#         host='localhost',
#         port='5432'
#     )
#
#
# def kitob_qoshish():
#     conn=get_connection()
#     cur=conn.cursor()
#     cur.execute("select * from kitoblar")
#     kitoblar2=cur.fetchall()
#     id=input("Kitob ID-sini kiriting: ")
#     for kitob in kitoblar2:
#         if kitob[0]==id:
#             print("Bunday ID-li kitob bazada bor! Boshqa ID kiriting: ")
#             kitob_qoshish()
#
#     nomi=input("Kitob nomini kiriting: ")
#     author=input("Kitob authorini kiriting: ")
#     narxi=int(input("Kitob narxini kiriting: "))
#
#     cur.execute("""
#     INSERT INTO kitoblar(id, nomi, author, narxi) VALUES (%s, %s, %s, %s)
#     """,(id, nomi, author, narxi))
#     conn.commit()
#
#     print("\033[92mKitob muvaffaqiyatli qo'shildi!\033[0m")
#     sorov=input("Yana kitob qo'shishni hohlayapsizmi[ha\yoq]?: ")
#     if sorov=='ha':
#         kitob_qoshish()
#     else:
#         admin_menu()
#
#
# def kitob_tahrirlash():
#     id=input("Tahrorlamoqchi bo'lgan kitobni ID-sini kiriting: ")
#     conn=get_connection()
#     cur= conn.cursor()
#     cur.execute("select * from kitoblar")
#     kitoblar2 = cur.fetchall()
#     for kitob in kitoblar2:
#         if kitob[0]==id:
#             print(f"{kitob[0]} | {kitob[1]} | {kitob[2]} | {kitob[3]}")
#             kitob_id=input("O'zgartirmoqchi bo'lgan ID-ni kiriting: ") or kitob[0]
#             kitob_nomi =input("O'zgartirmoqchi bo'lgan nomini kiriting: ") or kitob[1]
#             kitob_author =input("O'zgartirmoqchi bo'lgan authorni kiriting: ") or kitob[2]
#             kitob_narxi =int(input("O'zgartirmoqchi bo'lgan narxini kiriting: ")) or kitob[3]
#             cur.execute("UPDATE kitoblar SET id=%s,  nomi=%s, author=%s, narxi=%s WHERE id=%s",(kitob_id, kitob_nomi,kitob_author,kitob_narxi, id))
#             conn.commit()
#             print("Kitob muvaffaqiyatli yangilandi")
#             admin_menu()
#     admin_menu()
#
# def kitob_ochirish():
#     id = input("O'chirmoqchi bo'lgan kitobingizning ID-sini kiriting: ")
#     conn = get_connection()
#     cur = conn.cursor()
#     cur.execute("select * from kitoblar")
#     kitoblar2=cur.fetchall()
#     for kitob in kitoblar2:
#         if kitob [0]==id:
#             print(f"{kitob[0]} | {kitob[1]} | {kitob[2]} | {kitob[3]}")
#             sorov=input("Rostdan ham shu kitobni o'chirmoqchisiz[ha\yoq]?: ")
#             if sorov=='ha':
#                 cur.execute("DELETE FROM kitoblar WHERE id=%s", (id,))
#                 conn.commit()
#                 print("\033[92mKitob muvaffaqiyatli o'chirildi!\033[0m")
#                 admin_menu()
#             else:
#                 admin_menu()
#     admin_menu()
#
# def kitob_detail():
#     id = input("Ko'rmoqchi bo'lgan kitobingizning ID-sini kiriting: ")
#     conn = get_connection()
#     cur = conn.cursor()
#     cur.execute("select * from kitoblar")
#     kitoblar2=cur.fetchall()
#     cur.execute("select * from kitoblar where id=%s",(id,))
#     kitobcha=cur.fetchone()
#     print(kitobcha)
#
#     for kitob in kitoblar2:
#         if kitob[0]==id:
#             print(f"{kitob[0]} | {kitob[1]} | {kitob[2]} | {kitob[3]}")
#
#     admin_menu()
#
# def kitoblar_royhati():
#     print("===KITOBLAR RO'YHATI===")
#     conn=get_connection()
#     cur=conn.cursor()
#
#     cur.execute("select * from kitoblar where mavjudmi=%s",(True,))
#     kitoblar_from_db=cur.fetchall()
#     print(kitoblar_from_db)
#
#
#     for index,kitob in enumerate(kitoblar_from_db):
#         print(f"{index+1}){kitob[0]}|{kitob[1]}|{kitob[2]}|{kitob[3]}")
#
#     if location:
#         admin_menu()
#     else:
#         user_menu(login_fornow)
#
# def kitob_search():
#     nom=input("Izlamoqchi bo'lgan kitob nomini kiriting: ")
#     count= 0
#     conn = get_connection()
#     cur = conn.cursor()
#     cur.execute("select * from kitoblar")
#     kitoblar2=cur.fetchall()
#     count = 0
#     topilgan_kitoblar = []
#
#     for kitob in kitoblar2:
#         if nom.lower() in kitob[1].lower():
#             topilgan_kitoblar.append(kitob)
#
#     if topilgan_kitoblar:
#         print(f"{len(topilgan_kitoblar)} ta topildi\n")
#         for i, kitob in enumerate(topilgan_kitoblar, 1):
#             print(f"{i}) {kitob[0]} | {kitob[1]} | {kitob[2]} | {kitob[3]}")
#     else:
#         print("Bunday kitob topilmadi!")
#
#     if location:
#         admin_menu()
#     else:
#         user_menu(login_fornow)
#
#
#
#
#
# def admin_menu():
#     global location
#     location=True
#     print("""
# 1.Kitob qo'shish
# 2.Kitob tahrirlash
# 3.Kitob o'chirish
# 4.Kitob detail
# 5.Kitoblar ro'yhati
# 6.Kitob search
# 7. Orqaga
#         """)
#     tanlov=int(input("Tanlovni kiriting: "))
#     if tanlov==1:
#         kitob_qoshish()
#     elif tanlov==2:
#         kitob_tahrirlash()
#     elif tanlov==3:
#         kitob_ochirish()
#     elif tanlov==4:
#         kitob_detail()
#     elif tanlov==5:
#         kitoblar_royhati()
#     elif tanlov==6:
#         kitob_search()
#     elif tanlov==7:
#         main_menu()
#     else:
#         print("Bunday qiymat mavjut emas!")
#         admin_menu()
#
#
# def admin_registration():
#     conn=get_connection()
#     cur=conn.cursor()
#     new_login=input("Yangi loginni kiriting: ")
#     new_parol=input("Yangi parolni kiriting: ")
#     cur.execute("""
#     INSERT INTO adminlar(login, parol) VALUES (%s,%s)
#     """,(new_login,new_parol))
#     conn.commit()
#     print("Siz muvaffaqiyatli ro'yhatdan o'tdingiz")
#     main_menu()
#     print("Admin ro'yhatdan o'tdi!")
#
#
# def user_registration():
#     conn = get_connection()
#     cur = conn.cursor()
#     new_login=input("Yangi loginni kiriting: ")
#     new_parol=input("Yangi parolni kiriting: ")
#     cur.execute("""
#        INSERT INTO userlar(login, parol) VALUES (%s,%s)
#        """, (new_login, new_parol))
#     conn.commit()
#     print("Siz muvaffaqiyatli ro'yhatdan o'tdingiz")
#     main_menu()
#     print("User ro'yhatdan o'tdi!")
#
#
# def kitob_detail_va_sotib_olish(login):
#     conn = get_connection()
#     cur = conn.cursor()
#     cur.execute("select * from userlar where login=%s",(login,))
#     usercha=cur.fetchone()
#     id=input("Sotib olmoqchi bo'gan kitobingizning ID-sini kiriting: ")
#     cur.execute("select*from kitoblar where id=%s",(id,))
#     kitob=cur.fetchone()
#     print(kitob)
#     print(f"{kitob[0]}|{kitob[1]}|{kitob[2]}|{kitob[3]}")
#     sorov=input("Rostdan ham shu kitobni sotib olmoqchimisiz[ha\yoq]?: ")
#     if sorov=='ha':
#         if usercha[2]>= kitob[3]:
#             left_balance=usercha[2] -kitob[3]
#             cur.execute("UPDATE userlar SET balance=%s WHERE login=%s",(left_balance,login))
#
#             cur.execute("INSERT INTO xaridlar(user_login, kitob_id) VALUES (%s,%s)", (login,id))
#
#             cur.execute("UPDATE kitoblar SET mavjudmi=%s WHERE id=%s",(False,id))
#             conn.commit()
#             # kitoblar.remove(kitob)
#             print("Siz kitobni sotib oldingiz")
#             user_menu(login)
#         else:
#                 print("Sizda yetarli mablag mavjut emas")
#     else:
#             print("Siz kitobni xarid qilmadingiz!")
#             user_menu(login)
#
#
# def user_xaridlar(login):
#     conn = get_connection()
#     cur = conn.cursor()
#     cur.execute("select*from userlar where login=%s",(login,))
#     usercha=cur.fetchone()
#     if usercha:
#         print("Sizning xaridlaringiz!")
#         cur.execute("""
#         select k.nomi, k.author, k.narxi from xaridlar x join kitoblar k on x.kitob_id=k.id  WHERE x.user_login=%s and k.mavjudmi=%s
#         """,(login,False))
#         kitobchalar=cur.fetchall()
#         if kitobchalar:
#             for index,kitob in enumerate(kitobchalar):
#                 print(f"{index+1}){kitob[0]} | {kitob[1]} | {kitob[2]} | ")
#             user_menu(login)
#         else:
#             print("\033[91mSizda hech qanday xaridlar yo'q\033[0m")
#             user_menu(login)
#
#
# def user_menu(login):
#     global location
#     location=False
#     global login_fornow
#     login_fornow=login
#     conn=get_connection()
#     cur=conn.cursor()
#     cur.execute("select*from userlar where login=%s",(login,))
#     usercha=cur.fetchone()
#     print("""
# 1.Kitoblar ro'yhati
# 2.Kitob search
# 3.Kitob detail va sotib olish
# 4.Balance
# 5.Xaridlar
# 6.Orqaga
#     """)
#     tanlov=int(input("Tanlang(1-6): "))
#     if tanlov==1:
#         kitoblar_royhati()
#     elif tanlov==2:
#         kitob_search()
#     elif tanlov==3:
#         kitob_detail_va_sotib_olish(login)
#     elif tanlov==4:
#         print(f"Sizning hisobingizdagi balans: {usercha[2]}")
#         user_menu(login)
#     elif tanlov==5:
#         user_xaridlar(login)
#     elif tanlov==6:
#         main_menu()
#     else:
#         print("Bunday qiymat mavjut emas!")
#         user_menu(login)
#
#
# def admin_panel():
#     login=input("Loginni kiriting: ")
#     parol=input("Parol kiriting: ")
#
#     conn = get_connection()
#     cur = conn.cursor()
#     cur.execute("select * from adminlar WHERE login=%s",(login,))
#     admincha= cur.fetchone()
#
#     if admincha:
#         if admincha[1]==parol:
#             print("\033[92mBunday admin topildi!\033[0m")
#             admin_menu()
#         else:
#             print("Login to'g'ri ammo parol notogri kiritildi!")
#     else:
#         print("\033[91mBunday admin topilmadi, ro'yhatdan o'ting\033[0m")
#         admin_registration()
#
#
# def user_panel():
#     login=input("Loginni kiriting: ")
#     parol=input("Parolni kiriting: ")
#
#     conn = get_connection()
#     cur = conn.cursor()
#     cur.execute("select * from userlar WHERE login=%s and parol=%s", (login,parol))
#     usercha = cur.fetchone()
#     print(usercha)
#     if usercha:
#         print("\033[92mBunday user topildi!\033[0m")
#         user_menu(login)
#     else:
#         print("\033[91mBunday user topilmadi\033[0m")
#         user_registration()
#
#
#
# def main_menu():
#     print("""
# 1.Admin panel
# 2.User panel
# 3.Dasturrdan chiqish
#     """)
#     tanlov=int(input("Tanlang(1-3): "))
#     if tanlov==1:
#         admin_panel()
#     elif tanlov==2:
#         user_panel()
#     elif tanlov==3:
#         print("Dastur toxtatildi")
#         exit()
#     else:
#         print("Bunday qoymat mavjut emas!")
#         main_menu()
#
# main_menu()
