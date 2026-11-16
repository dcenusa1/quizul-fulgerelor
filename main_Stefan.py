print("==============================")
print("QUIZ-UL FULGERELOR")
print("==============================")

categorii = {
    1: {
        "nume": "SPORT",
        "intrebari": [
            ("Câți jucători are o echipă de fotbal pe teren?", "11"),
            ("În ce sport se folosește racheta?", "Tenis"),
            ("Câte inele are simbolul olimpic?", "5")
        ]
    },
    2: {
        "nume": "ANIMALE",
        "intrebari": [
            ("Care este cel mai mare animal de pe Pământ?", "balena albastra"),
            ("Câte picioare are un păianjen?", "8"),
            ("Ce animal doarme agățat cu capul în jos?", "liliacul")
        ]
    },
    3: {
        "nume": "JOCURI VIDEO",
        "intrebari": [
            ("Care este personajul principal din Minecraft?", "Steve"),
            ("Cum se numește mascota Nintendo?", "Mario"),
            ("Ce joc are personaje numite Creeperi?", "Minecraft")
        ]
    },
    4: {
        "nume": "ȘTIINȚĂ",
        "intrebari": [
            ("Care este planeta roșie?", "Marte"),
            ("Cât face 5 x 5?", "25"),
            ("Ce gaz respiră oamenii?", "oxigen")
        ]
    }
}

r=0
nume = input("Cum te numesti? > ")
while True:
    print(f" Salut, {nume}! Alege o categorie: ")
    print("1.Sport")
    print("2.Animale")
    print("3.Jocuri video")
    print("4.Stiinta")
    print("0.Exit")
    alegere = input("Alege o categorie ")
    if alegere == "0":
        break
    elif alegere == "1":
        categorie = categorii[1]
        print(f"Ai ales categoria: {categorie['nume']}")
        print(f"Câți jucători are o echipă de fotbal pe teren?")
        raspuns = input("Răspuns: ")
        if raspuns == "11":
            print("Răspuns corect!")
            r=r+1
        else:
            print("Răspuns greșit. Răspunsul corect este 11.")
        print(f"În ce sport se folosește racheta?")
        raspuns = input("Răspuns: ")
        if raspuns == "Tenis":
            print("Răspuns corect!")
            r=r+1
        else:
            print("Răspuns greșit. Răspunsul corect este Tenis.")
        print(f"Câte inele are simbolul olimpic?")
        raspuns = input("Răspuns: ")
        if raspuns == "5":
            print("Răspuns corect!")
            r=r+1
        else:
            print("Răspuns greșit. Răspunsul corect este 5.")
        if r == 3:
            print("Felicitări! Ai răspuns corect la toate întrebările din categoria Sport!")
        else:
            print(f"Ai răspuns corect la {r} întrebări din categoria Sport.")
        r=0
        print("Ai dori să continui cu altă categorie?")
        print("1.Da")
        print("2.Nu")
        if input("Alege o opțiune: ") == "2":
            break
    elif alegere == "2":
        categorie = categorii[2]
        print(f"Ai ales categoria: {categorie['nume']}")
        print(f"Care este cel mai mare animal de pe Pământ?")
        raspuns = input("Răspuns: ")
        if raspuns == "balena albastra":
            print("Răspuns corect!")
            r=r+1
        else:
            print("Răspuns greșit. Răspunsul corect este balena albastra.")
        print(f"Câte picioare are un păianjen?")
        raspuns = input("Răspuns: ")
        if raspuns == "8":
            print("Răspuns corect!")
            r=r+1
        else:
            print("Răspuns greșit. Răspunsul corect este 8.")
        print(f"Ce animal doarme agățat cu capul în jos?")
        raspuns = input("Răspuns: ")
        if raspuns == "liliacul":
            print("Răspuns corect!")
            r=r+1
        else:
            print("Răspuns greșit. Răspunsul corect este liliacul.")
        if r == 3:
            print("Felicitări! Ai răspuns corect la toate întrebările din categoria Animale!")
        else:
            print(f"Ai răspuns corect la {r} întrebări din categoria Animale.")
        r=0
        print("Ai dori să continui cu altă categorie?")
        print("1.Da")
        print("2.Nu")
        if input("Alege o opțiune: ") == "2":
            break
    elif alegere == "3":
        categorie = categorii[3]
        print(f"Ai ales categoria: {categorie['nume']}")
        print(f"Care este personajul principal din Minecraft?")
        raspuns = input("Răspuns: ")
        if raspuns == "Steve":
            print("Răspuns corect!")
            r=r+1
        else:
            print("Răspuns greșit. Răspunsul corect este Steve.")
        print(f"Cum se numește mascota Nintendo?")
        raspuns = input("Răspuns: ")
        if raspuns == "Mario":
            print("Răspuns corect!")
            r=r+1
        else:
            print("Răspuns greșit. Răspunsul corect este Mario.")
        print(f"Ce joc are personaje numite Creeperi?")
        raspuns = input("Răspuns: ")
        if raspuns == "Minecraft":
            print("Răspuns corect!")
            r=r+1
        else:
            print("Răspuns greșit. Răspunsul corect este Minecraft.")
        if r == 3:
            print("Felicitări! Ai răspuns corect la toate întrebările din categoria Jocuri!")
        else:
            print(f"Ai răspuns corect la {r} întrebări din categoria Jocuri Video.")
        r=0
        print("Ai dori să continui cu altă categorie?")
        print("1.Da")
        print("2.Nu")
        if input("Alege o opțiune: ") == "2":
            break
    elif alegere == "4":
        categorie = categorii[4]
        print(f"Ai ales categoria: {categorie['nume']}")
        print(f"Care este planeta roșie?")
        raspuns = input("Răspuns: ")
        if raspuns == "Marte":
            print("Răspuns corect!")
            r=r+1
        else:
            print("Răspuns greșit. Răspunsul corect este Marte.")
        print(f"Cât face 5 x 5?")
        raspuns = input("Răspuns: ")
        if raspuns == "25":
            print("Răspuns corect!")
            r=r+1
        else:
            print("Răspuns greșit. Răspunsul corect este 25.")
        print(f"Ce gaz respiră oamenii?")
        raspuns = input("Răspuns: ")
        if raspuns == "oxigen":
            print("Răspuns corect!")
            r=r+1
        else:
            print("Răspuns greșit. Răspunsul corect este oxigen.")
        if r == 3:
            print("Felicitări! Ai răspuns corect la toate întrebările din categoria Știință!")
        else:
            print(f"Ai răspuns corect la {r} întrebări din categoria Știință.")
        r=0
        print("Ai dori să continui cu altă categorie?")
        print("1.Da")
        print("2.Nu")
        if input("Alege o opțiune: ") == "2":
            break