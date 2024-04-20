qt = int(input())

for i in range(qt):
    ch = input()
    ch = ch.split(" ")

    if ch[0] == "papel":
        if ch[1] == "papel":
            print("Caso #%d: De novo!" % (i + 1))
        elif ch[1] == "pedra":
            print("Caso #%d: Bazinga!" % (i + 1))
        elif ch[1] == "lagarto":
            print("Caso #%d: Raj trapaceou!" % (i + 1))
        elif ch[1] == "tesoura":
            print("Caso #%d: Raj trapaceou!" % (i + 1))
        elif ch[1] == "Spock":
            print("Caso #%d: Bazinga!" % (i + 1))
    elif ch[0] == "pedra":
        if ch[1] == "papel":
            print("Caso #%d: Raj trapaceou!" % (i + 1))
        elif ch[1] == "pedra":
            print("Caso #%d: De novo!" % (i + 1))
        elif ch[1] == "lagarto":
            print("Caso #%d: Bazinga!" % (i + 1))
        elif ch[1] == "tesoura":
            print("Caso #%d: Bazinga!" % (i + 1))
        elif ch[1] == "Spock":
            print("Caso #%d: Raj trapaceou!" % (i + 1))
    elif ch[0] == "lagarto":
        if ch[1] == "papel":
            print("Caso #%d: Bazinga!" % (i + 1))
        elif ch[1] == "pedra":
            print("Caso #%d: Raj trapaceou!" % (i + 1))
        elif ch[1] == "lagarto":
            print("Caso #%d: De novo!" % (i + 1))
        elif ch[1] == "tesoura":
            print("Caso #%d: Raj trapaceou!" % (i + 1))
        elif ch[1] == "Spock":
            print("Caso #%d: Bazinga!" % (i + 1))
    elif ch[0] == "tesoura":
        if ch[1] == "papel":
            print("Caso #%d: Bazinga!" % (i + 1))
        elif ch[1] == "pedra":
            print("Caso #%d: Raj trapaceou!" % (i + 1))
        elif ch[1] == "lagarto":
            print("Caso #%d: Bazinga!" % (i + 1))
        elif ch[1] == "tesoura":
            print("Caso #%d: De novo!" % (i + 1))
        elif ch[1] == "Spock":
            print("Caso #%d: Raj trapaceou!" % (i + 1))
    elif ch[0] == "Spock":
        if ch[1] == "papel":
            print("Caso #%d: Raj trapaceou!" % (i + 1))
        elif ch[1] == "pedra":
            print("Caso #%d: Bazinga!" % (i + 1))
        elif ch[1] == "lagarto":
            print("Caso #%d: Raj trapaceou!" % (i + 1))
        elif ch[1] == "tesoura":
            print("Caso #%d: Bazinga!" % (i + 1))
        elif ch[1] == "Spock":
            print("Caso #%d: De novo!" % (i + 1))
