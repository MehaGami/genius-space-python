password = "password123"
input_password_1 = "password123"
input_password_2 = "password124"

password_list = [input_password_1, input_password_2]

for password_check in password_list:
    if password_check == password:
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

i = 0
while i < 9:
    if i >= 1 and i <=7:
        print(i)
        print(week_days[str(i)])
    else:
        print(i)
        print("incorrect parametr")
    i += 1

num = 5
j = 1
while j <= 10:
    print(num * j)
    j += 1

numbers = [1, 22, 3, 45, 21]
result = 0
for i in numbers:
    result += i
print(result)

num = 6
i = 1 
result = 1 
while i <= num:
    result *= i
    i += 1
print(result)

i = 1
while i <= 50:
    if i % 2 == 0:
        print(i)
    i += 1

i = 1
while i <= 50:
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
