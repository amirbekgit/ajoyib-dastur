from random import *

summa  =  input('summani kiriting: ')
print(f"summa: {summa}")

otkazma_manzili = input("o`tkazma manzilini kiriting: ")
otkazma = input("o`tkazma summasini kiriting: ")
print("ekraningizda o`tkazmani o`tkazish uchun tasdiqlash kodi chiqadi")

kod = randint(1000, 9000)

print(f"Tasdiqlash kodi: {kod}")

inputt = input("Tasdiqlash kodini kiriting: ")

if inputt == f"{kod}":
    print("To`lov muvvfaqiyatli amalga oshirildi")
else:
    print("Tasdiqlash kodi kiritilmagan yoki manzill to`g`ri kiritilmagan bo`lishi mumkin")



print("siz show_money komandasi orqali qolgan summani korishingiz mumkin")
command = input(">>>")

qolgan = int(summa) - int(otkazma)


if command == "show_money":
    print(f"qolgan summa: {qolgan}")
else:
    print("Xatolik bor")