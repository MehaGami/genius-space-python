numbers_list = [15, 23, 21]
print(numbers_list)
numbers_list.append(10)
numbers_list.append(20)
print(numbers_list)
numbers_list.remove(10)
print(numbers_list)
result = 0
for num in numbers_list:
    result += num
print(result)

result_numbers_list = []
for num in numbers_list:
    num = num * 2
    result_numbers_list.append(num)
print(result_numbers_list)

item_tuple = ("яблуко", "банан", "апельсин")
for item in item_tuple:
    print(item)

numbers_tuple_1 = (1, 2, 3)
numbers_tuple_2 = (4, 5, 6)
print(numbers_tuple_1, numbers_tuple_2)
all_numbers_tuple = numbers_tuple_1 + numbers_tuple_2
print(all_numbers_tuple)

sportsmen = {
    "name": "Tom",
    "sport": "volleyball",
    "age": "22",
}
print(sportsmen)

books = {
    "1989": "2000",
    "essensialism": "2010"
}
print(books)
new_book = {"mark avreli": "2015"}
books.update(new_book)
print(books)

countries = {
    "Ukraine": "Kiev",
    "France": "Paris",
    "Poland": "Warsaw"
}
country = input("Write country: ")
country = country.capitalize()
print(countries.get(country, "We don't have this country("))