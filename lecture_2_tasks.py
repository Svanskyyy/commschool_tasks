from time import time
from tokenize import group

#1 შეინახეთ ცვლადებში ცვლადების ტიპები მათი მნიშვნელობების ნაცვლად

var1 = type(1)
var2 = type(2)
var3 = type(True)

print(var1, var2, var3)

#2 შეცვალეთ ცვლადების ტიპები (type casting-ის მეშვეობით)

var4 = float(False) #float-ში გადაყვანა
var5 = float(3) #float-ში გადაყვანა
var6 = list({"key": "value", "key1": "value", "key2": "value"}) #list-ში გადაყვანა

print(var4, var5, var6)

#3 შექმენით შესაფერისი ტიპის ცვლადები მონაცემებისთვის

group = {
    "name": "Python2023",
    "count": 35,
    "male": 22,
    "female": 13,
    "students": ["Student1", "Student2", "Student3", "Student4", "Student5"],
    "ages": [21, 33, 15, 45, 42]
}

print(group)

#4 დააფორმატეთ სტრიქონი და გამოითვალეთ თქვენი ასაკი

birth_year = 1999
name = "Levan"
surname = "Liparteliani"
current_year = 2026

current_age = current_year - birth_year

print(f"მე {name} {surname} დავიბადე {birth_year} შესაბამისად ვარ {current_age}" )

#5 გამოითვალეთ მომხრეთა და მოწინააღმდეგეთა პროცენტი და აჩვენეთ ორივე.

YES = 119
NO = 82
TOTAL = YES + NO

PERCENTAGE_OF_YES = (YES / TOTAL) * 100
PERCENTAGE_OF_NO = (NO / TOTAL) * 100

print(F"YES: {YES} = {PERCENTAGE_OF_YES:.2f}%"
      F"NO: {NO} = {PERCENTAGE_OF_NO:.2f}%")

#6 გადაიყვანეთ 3670 წამი საათებად და წუთებად

seconds = 3670
hours = seconds // 3600
remaining_seconds = seconds % 3600
minutes = remaining_seconds // 60
total_seconds = remaining_seconds % 60

print(f"{hours} საათი {minutes} წუთი {total_seconds} წამი")

#7 გამოიტანეთ სტრიქონის პირველი და ბოლო ასო

text = "Python"

first_letter = text[0]
last_letter = text[-1]

print(first_letter, last_letter)

#8 გამოითვალეთ სასწავლო საგნის შეფასების პროცენტული წილი

math = 45
total = 60

x = (math / total) * 100

print(f"პროცენტი: {x}%")

#9 გამოითვალეთ ასაკი მომავალ წელს

birth_year = 2000
current_year = 2025

print(f"მომავალ წელს შენ იქნები {current_year - birth_year + 1} წლის")

#10 350 წუთი რამდენი საათია და რამდენი წუთი დარჩება გამოიტანეთ

minutes = 350
hours = minutes // 60
remaining_minutes = minutes % 60

print(f"{hours} საათი და {remaining_minutes} წუთი")




















