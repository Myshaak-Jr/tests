from random import randint, random, randrange


with open("a.txt", "w") as f:
    for _ in range(10000):
        f.write("".join([chr(randint(0x41, 0x41 + 25)) for _ in range(randint(3, 8))]) + " " + "".join([chr(randint(0x41, 0x41 + 25)) for _ in range(randint(3, 8))]) + " " + "".join([chr(randint(0x41, 0x41 + 25)) for _ in range(randint(3, 8))]) + f"{random() * randrange(10000)}")


