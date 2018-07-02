# Stack frame demo ---------------------
# Let's explore how stack frames work

def get_average(numbers):
    sum = 0
    count = len(numbers)
    for number in numbers:
        sum += number
    return sum / count

def get_min(numbers):
    if len(numbers) == 0:
        return 0
    
    min = numbers[0]
    for number in numbers:
        if number < min:
            min = number
    
    return min

def print_statistics(numbers):
    avg = get_average(numbers)
    min = get_min(numbers)
    print("average: " + str(avg))
    print("min: " + str(min))

numbers = [4, 1, 29, 2]
print_statistics(numbers)
