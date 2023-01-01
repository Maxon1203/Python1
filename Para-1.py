from Class import method
# Ввод данных
# name = input("Введите ваше имя:")
# age = input("Введите ваш возраст:")
# # Вывод в консоль
# # Обьединение строк
# print("Привет: ",name, "Возраст: ",age)
# # Вывод через форматирование строки
# print(f"Hello {name} возраст {age}")


# number = input("Кол-во чисел: ") 
# znak = input("Кол-во чисел: ")
# if (znak == "+"):
#     i=1
#     summ = 0
#     while i <= int(number):
#         i +=1
#         numbers = input("число")
#         summ += int(numbers)
#     print(summ)
# elif(znak =="-"):
#     i=1
#     summ = 0
#     while i <= int(number):
       
#         numbers = input("число")
#         if (i == 1):
#             summ = int(numbers)           
#         else:
#             summ -=int(numbers)
#         i +=1

#     print(summ)
# elif(znak =="*"):
#     i=1
#     summ = 1
#     while i <= int(number):
#         i +=1
#         numbers = input("число")
#         summ *= int(numbers)
#     print(summ)
 
# # Плюс
# print(12 + 2)  #14
# # Минус
# print(5 - 2)  #3
# # Умножение
# print(4 * 2)  #8
# # Деление 
# print(5 / 2)  #2.5
# # Деление с остатком
# print(5 // 2)  #2
# # Округление 
# print(round(7 / 3, 3))  #2.333

def sum(numbers):
    result=0
    for n in numbers:
        result += n
    print(f"sum = {result}") 


number = input("Кол-во чисел: ") 
i=1
qwe = []
while i <= int(number):
    i +=1
    numbers = input("число")
    qwe.append(int(numbers))
method.sum(qwe)

# def sum(numbers):
#     result=0
#     for n in numbers:
#         result += n
#     print(f"sum = {result}") 


