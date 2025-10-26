import re

password = "password123"
input_password = input("Write password: ")

if input_password == password:
    print("You connect to system")
else:
    print("Incorrect password")

week_days = {
    "1": "Monday",
    "2": "Tuesday",
    "3": "Wednesday",
    "4": "Thursday",
    "5": "Friday",
    "6": "Saturday",
    "7": "Sunday",
}

try:
    day = int(input("Write number of day: "))
except ValueError:
    print("incorrect parametr")

if day >= 1 and day <=7 :
    print(week_days[str(day)])
else:
    print("incorrect parametr")

try:
    num = int(input("Write number: "))
except ValueError:
    print("incorrect parametr")
j = 1
while j <= 10:
    print(num * j)
    j += 1

try:
    input_numbers = input("Write numbers separated by commas: ")
    tokens = re.split(r"[,\s]+", input_numbers.strip())
    list_of_numbers = [int(x) for x in tokens if x]
except ValueError:
    print("Incorrect parameter")

result = 0
for i in list_of_numbers:
    result += i
print(result)

try:
    num = int(input("Write number: "))
except ValueError:
    print("incorrect parametr")
i = 1 
result = 1 
while i <= num:
    result *= i
    i += 1
print(result)

try:
    num = int(input("Write number: "))
except ValueError:
    print("incorrect parametr")
i = 1
while i <= num:
    if i % 2 == 0:
        print(i)
    i += 1

try:
    num = int(input("Write number: "))
except ValueError:
    print("incorrect parametr")
i = 1
while i <= num:
    j = 2
    natural = True
    while j < i:
        if i % j == 0:
            natural = False
            break
        j += 1
    if natural:
        print(i)
    i += 1
