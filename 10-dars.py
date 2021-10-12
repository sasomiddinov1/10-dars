#                                     10 dars if else

# Yangi cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia'] degan ro'yxat tuzing, 
# ro'yxat elementlarining birinchi harfini katta qilib konsolga chqaring. GM uchun ikkala harfni katta qilin!

cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
for car in cars:
    if car =='gm':
        print(car.upper())
    else:
        print(car.title())
        
# Yuqoridagi mashqni teng emas (!=) operatori yordamida bajaring.

cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
for car in cars:
    if car !='kia':
        print(car.title())
    else:
        print(car.upper())
        
# Foydalanuvchi login ismini so'rang. Agar login admin bo'lsa, "Xush kelibsiz, Admin.
 # Foydalanuvchilar ro'yxatini ko'rasizmi?" xabarini konsolga chiqaring. Aks holda,
 # "Xush kelibsiz, {foydalanuvchi_ismi}!"  matnini konsolga chiqaring.

# login = input('Loginingizni kiriting\n>>>')
# if login.lower() == 'admin':
#     print("Xush kelibsiz Admin Foydalanuvchilar ro'yxatini ko'rasizmi?")
# else:
#     print(f"Xush kelibsiz, {login.title()}!")

# Foydalanuvchidan 2 ta son kiritishni so'rang. Agar ikki son bir-biriga teng bo'lsa,
 # "Sonlar teng" ekan degan yozuvni konsolga chiqaring.

# x =  float(input("Brinchi soningizni kiritin! >>> "))
# y = float(input("Ikkinchi soningizni kiriting! >>> "))
# if x == y:
#     print(f"sonlar teng {x}={y} ga")

# Foydalanuvchidan istalgan son kiritishni so'rang. Agar son manfiy bo'lsa konsolga 
# "Manfiy son", agar musbat bo'lsa "Musbat son" degan xabarni chiqaring. 
son = float(input("istalgan soningizni kiriting >>>"))
print("Manfiy son ") if son <0  else print("son musbat")

#Foydalanuvchidan son kiritishni so'rang, agar son musbat bo'lsa uning ildizini
 # hisoblab konsolga chiqaring. Agar son manfiy bo'lsa, "Musbat son kiriting" 
 # xabarni chiqaring. 

son = float(input('Istalgan son kiriting: '))
print(son**(1/2)) if son>0 else print('Musbat son kiriting')











