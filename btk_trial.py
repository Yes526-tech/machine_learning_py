word = input("enter your word: ")
how_many = int(input("how many times do you want this word on screen: "))


def print_on(word, how_many):
    for _ in range(how_many):
        print(word)

print_on(word, how_many)