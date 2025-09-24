n = int(input())

for i in range(n):
    kod = int(input())

    if kod == 88:
        print("Hello")
    elif kod == 86:
        print("How are you?")
    elif kod < 88:
        print("GREAT!")
    else:
        print("Bye.")