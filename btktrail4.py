# def square(num): return num ** 2

numbers = [1, 3, 4, 5, 9, 10]

# result = map(square, numbers)

# print(list(result))

# for item in map(lambda x : x ** 2, numbers):
#     print(item)



def  check_even(num): return num % 2 == 0

result = list(filter(lambda num : num % 2 == 0, numbers))

print(result)