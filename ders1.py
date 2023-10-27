# task 1

# name_info = {
#     "Aslan": "Aslan emi ogludur",
#     "Imran": "Imran dayi ogludur",
#     "Afaq": "Afaq bibi qizidir",
#     "Uzeyir": "Uzeyir xala ogludur",
#     "Shahin": "Shahin yaxin dostdur",
# }

# while True:
#     name = input("Ad daxil edin: ")
    
#     if name:
#         if name in name_info:
#             print(name_info[name])
#         else:
#             print(f"{name} kimdir? Men onu tanimadim")
#     else:
#         print("Siz ad daxil etmediniz")





# Task 2 

# doğru_istifadəçi_adı = "test"
# doğru_şifrə = "12345"

# istifadəçi_adı = input("İstifadəçi Adı:\n")
# şifrə = input("Şifrə:\n")

# if istifadəçi_adı == doğru_istifadəçi_adı and şifrə == doğru_şifrə:
#     print("Xoş gəldiniz")
# elif istifadəçi_adı == doğru_istifadəçi_adı and şifrə != doğru_şifrə:
#     print("Şifrə yanlışdır")
# elif istifadəçi_adı != doğru_istifadəçi_adı and şifrə == doğru_şifrə:
#     print("İstifadəçi adı yanlışdır")
# elif istifadəçi_adı == "" and şifrə != "":
#     print("İstifadəçi adı daxil etmədiniz")
# elif istifadəçi_adı != "" and şifrə == "":
#     print("Şifrə daxil etmədiniz")
# else:
#     print("İstifadəçi adı və şifrə yanlışdır")




#task 3
# number1 = float(input("Birinci ededi daxil edin: "))
# number2 = float(input("Ikinci ededi daxil edin: "))
# number3 = float(input("Ucuncu ededi daxil edin: "))


# max_number = max(number1, number2, number3)


# print("Ən böyük rəqəm:", max_number)





#task 7

# name_list = []

# while True:
#     name = input("Ad daxil edin (maksimum 15 hərf): ")

#     if not name:
#         print("Ad daxil etmediniz")
#     elif len(name) > 15:
#         print("Ad çox uzundur (maksimum 15 hərf)")
#     else:
#         name_list.append(name)
#         print("Ad Bazaya ugurla elave olundu")
    



#task 4

# height = float(input("Boyunuzu Daxil edin (metrlər ilə): "))
# weight = float(input("Kütləni Daxil edin (kilogramlar ilə): "))

# bmi = weight / (height * height)


# if bmi < 18.5:
#     category = "Zəif"
# elif 18.5 <= bmi < 25:
#     category = "Normal"
# elif 25 <= bmi < 30:
#     category = "Kilolu"
# else:
#     category = "Obez"

# print(category)


