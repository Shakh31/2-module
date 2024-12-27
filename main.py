# ..........................1-task.............................
# class Student:
#     def __init__(self, student_id, student_name, class_name):
#         self.student_id = student_id
#         self.student_name = student_name
#         self.class_name = class_name
#
#     def info(self):
#         return f"ID: {self.student_id}, Name: {self.student_name}, Class: {self.class_name}"
#
#
# student1 = Student(1, "Ali Valiyev", "Matematika")
# student2 = Student(2, "Olim Karimov", "Fizika")
# student3 = Student(3, "Sara Ahmedova", "Kimyo")
#
# print(student1.info())
# print(student2.info())
# print(student3.info())
from idlelib.replace import replace


# .........................2-task................................
# import json
#
# python_obj = {
#     "name": "David",
#     "class": "I",
#     "age": 6
# }
#
# json_obj = json.dumps(python_obj)
# print(json_obj)


# .........................3-task..............................
# from datetime import date
#
# def kunlar_soni(a, b):
#     sana1 = date(a[0], a[1], a[2])
#     sana2 = date(b[0], b[1], b[2])
#     farq = sana2 - sana1
#     return farq.days
#
#
# sana_1 = (2014, 7, 2)
# sana_2 = (2014, 7, 11)
# print(kunlar_soni(sana_1, sana_2))


# .........................4-task.............................
# with open('context.txt', 'r') as file:
#     text = file.read()
#
# words = text.split()
# word_count = {}
#
# for word in words:
#     if word in word_count:
#         word_count[word] += 1
#     else:
#         word_count[word] = 1
#
# print(word_count)


# ..........................5-task.............................
# from datetime import date, timedelta
#
# bugun = date.today()
#
# kecha = bugun - timedelta(days=1)
#
# ertaga = bugun + timedelta(days=1)
#
# print("Kechagi sana:", kecha)
# print("Bugungi sana:", bugun)
# print("Ertangi sana:", ertaga)


# ..........................6-task..............................
# L = [2, 2, 3, 4, 5]
#
# R = []
# for x in L:
#     R.append(x**3)
#
# print(R)


# ..........................7-task...........................
# import datetime
#
# def weekends(year):
#     first_weekend = datetime.date(year, 1, 1)
#     end_weekend = datetime.date(year, 12, 31)
#
#     print(f'{year} yilidagi barcha yakshanbalar: ')
#
#     while first_weekend <= end_weekend:
#         if first_weekend.weekday() == 6:
#             print(first_weekend)
#
#         first_weekend += datetime.timedelta(days=1)
#
# yil = int(input("Yilni kiriting: "))
# print(weekends(yil))


# ...........................8-task..............................
# def tub(number):
#     if number <= 2:
#         return False
#     for i in range(2, number):
#         if number % i == 0:
#             return False
#
#     return True
#
# def find_tub_numbers(n):
#     res = []
#     for i in range(2, n + 1):
#         if tub(i):
#             res.append(i)
#
#     return res
#
#
# numbers = int(input('Enter tub number = '))
# tub_sonlar = find_tub_numbers(numbers)
# print(tub_sonlar)


# ...........................9-task.............................
# text = "Python is a widely used high-level, general-purpose, interpreted, dynamic programming language.Its design philosophy emphasizes code readability"
# new_text = text.replace("a", "9")
#
# print(new_text)


# .......................



