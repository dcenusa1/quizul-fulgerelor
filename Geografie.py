print("==============================")
print("QUIZ-UL GEOGRAFIEI SPATIALE")
print("==============================")

while True:
    print("Ai ales quiz-ul de geografie spatiala!")
    print("Raspunde la urmatoarele 12 intrebari:")
    r = 0

    print("1. Care este cea mai mare planeta din Sistemul Solar?")
    raspuns = input("Raspuns: ").strip().lower()
    if raspuns in ["jupiter"]:
        print("Raspuns corect!")
        r = r+1
    else:
        print("Raspuns gresit. Raspunsul corect este Jupiter.")

    print("2. Care este cea mai fierbinte planeta din Sistemul Solar?")
    raspuns = input("Raspuns: ").strip().lower()
    if raspuns in ["venus"]:
        print("Raspuns corect!")
        r = r+1
    else:
        print("Raspuns gresit. Raspunsul corect este Venus.")

    print("3. Cum se numeste galaxia in care se afla Sistemul Solar?")
    raspuns = input("Raspuns: ").strip().lower()
    if raspuns in ["calea lactee", "calea-lactee"]:
        print("Raspuns corect!")
        r = r+1
    else:
        print("Raspuns gresit. Raspunsul corect este Calea Lactee.")

    print("4. Care este planeta cunoscuta drept Planeta Rosie?")
    raspuns = input("Raspuns: ").strip().lower()
    if raspuns in ["marte"]:
        print("Raspuns corect!")
        r = r+1
    else:
        print("Raspuns gresit. Raspunsul corect este Marte.")

    print("5. Care este cel mai mare satelit natural din Sistemul Solar?")
    raspuns = input("Raspuns: ").strip().lower()
    if raspuns in ["ganymede", "ganymed"]:
        print("Raspuns corect!")
        r = r+1
    else:
        print("Raspuns gresit. Raspunsul corect este Ganymede.")

    print("6. Intre ce doua planete se afla centura principala de asteroizi?")
    raspuns = input("Raspuns: ").strip().lower()
    if raspuns in ["marte si jupiter", "jupiter si marte"]:
        print("Raspuns corect!")
        r = r+1
    else:
        print("Raspuns gresit. Raspunsul corect este Marte si Jupiter.")

    print("7. Care este cea mai apropiata planeta de Soare?")
    raspuns = input("Raspuns: ").strip().lower()
    if raspuns in ["mercur"]:
        print("Raspuns corect!")
        r = r+1
    else:
        print("Raspuns gresit. Raspunsul corect este Mercur.")

    print("8. Cum se numeste steaua din centrul Sistemului Solar?")
    raspuns = input("Raspuns: ").strip().lower()
    if raspuns in ["soarele", "soare"]:
        print("Raspuns corect!")
        r = r+1
    else:
        print("Raspuns gresit. Raspunsul corect este Soarele.")

    print("9. Care planeta este renumita pentru inelele sale?")
    raspuns = input("Raspuns: ").strip().lower()
    if raspuns in ["saturn"]:
        print("Raspuns corect!")
        r = r+1
    else:
        print("Raspuns gresit. Raspunsul corect este Saturn.")

    print("10. Cum se numeste satelitul natural al Pamantului?")
    raspuns = input("Raspuns: ").strip().lower()
    if raspuns in ["luna"]:
        print("Raspuns corect!")
        r = r+1
    else:
        print("Raspuns gresit. Raspunsul corect este Luna.")

    print("11. Cum se numeste planeta pitica aflata dincolo de Neptun?")
    raspuns = input("Raspuns: ").strip().lower()
    if raspuns in ["pluto"]:
        print("Raspuns corect!")
        r = r+1
    else:
        print("Raspuns gresit. Raspunsul corect este Pluto.")

    print("12. Cum se numeste distanta parcursa de lumina intr-un an?")
    raspuns = input("Raspuns: ").strip().lower()
    if raspuns in ["an lumina", "an-lumina", "an de lumina"]:
        print("Raspuns corect!")
        r = r+1
    else:
        print("Raspuns gresit. Raspunsul corect este an-lumina.")

    if r == 12:
        print("Felicitari! Ai raspuns corect la toate intrebarile!")
    else:
        print(f"Ai raspuns corect la {r} intrebari din 12.")

    print("Ai dori sa incerci din nou?")
    print("1. Da")
    print("2. Nu")

    if input("Alege o optiune (1 sau 2): ").strip() == "2":
        print("Multumim pentru participare! La revedere!")
        break