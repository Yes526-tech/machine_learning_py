number = int(input("enter number: "))

def find_divisive(number):
    numbers = []
    for i in range(2, number + 1):
        if number % i == 0:
            numbers.append(i)
    return numbers



print(find_divisive(number))