x = 50

def test():
    global x
    print(f"x: {x}")

    x  = 100
    print(f"changed x to {x}")



test()

print(x)