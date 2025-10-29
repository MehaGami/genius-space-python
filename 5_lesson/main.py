import calculator
import re
import utilities

operations = {
    "*": calculator.multiply,
    "/": calculator.divide,
    "+": calculator.add,
    "-": calculator.subtract,
}
def main():
    try:
        num_1 = int(input("Write first number: "))
    except ValueError:
        return print("Incorrect parameter")
    try:
        num_2 = int(input("Write second number: "))
    except ValueError:
        return print("Incorrect parameter")
    
    operation = input("Write operetion(+, -, *, /): ")
    result = operations.get(operation, lambda num_1, num_2:"Incorrect operation!!!")(num_1, num_2)
    if result is not None:
        print(result)

main()

input_numbers = input("Write numbers separated by commas: ")
tokens = re.split(r"[,\s]+", input_numbers.strip())
list_of_numbers = [int(x) for x in tokens if x]

print(utilities.calculate_average(list_of_numbers), utilities.find_max(list_of_numbers))