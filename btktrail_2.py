def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
    
def find_prime(num1, num2):
    prime_nums = []
    for i in range(num1, num2 + 1):
        if is_prime(i):
            prime_nums.append(i)
    return prime_nums, len(prime_nums)
    


num1 = int(input("İlk sayiyi girin: "))
num2 = int(input("İkinci sayiyi girin: "))

primes = find_prime(num1, num2)
print(primes)