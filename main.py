print("==============================")
print("QUIZ-UL FULGERELOR")
print("==============================")

categorii = {
    1: {
        "nume": "SPORT",
        "intrebari": [
            ("Câți jucători are o echipă de fotbal pe teren?", "11"),
            ("În ce sport se folosește racheta?", "tenis"),
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
            ("Care este personajul principal din Minecraft?", "steve"),
            ("Cum se numește mascota Nintendo?", "mario"),
            ("Ce joc are personaje numite Creeperi?", "minecraft")
        ]
    },
    4: {
        "nume": "ȘTIINȚĂ",
        "intrebari": [
            ("Care este planeta roșie?", "marte"),
            ("Cât face 5 x 5?", "25"),
            ("Ce gaz respiră oamenii?", "oxigen")
        ]
    }
}

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