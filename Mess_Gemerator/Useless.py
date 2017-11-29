def random_generate(length):
    import random
    characters = "QWERTYUIOPASDFGHJKLZXCVBNM"
    result = []
    for t in range(length):
        result.append(random.choice(characters))
    return result

def boring(length):
    psw_first = random_generate(length)
    times = 0
    while True:
        psw_second = random_generate(length)
        times += 1
        if psw_first == psw_second:
            break
    return times

def main():
    length = int(input("How long do you wanna test: "))
    print(boring(length))

while True:
    main()
