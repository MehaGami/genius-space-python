def calculate_average(numbers):
    result = 0
    for num in numbers:
        result += num
    return result / (len(numbers) + 1)

def find_max(numbers):
    result = numbers[0]
    for num in numbers:
        if num > result:
            result = num
    return result