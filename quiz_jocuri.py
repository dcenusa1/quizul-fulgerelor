print("==============================")
print("QUIZ-UL JOCURILOR")
print("==============================")

print("==============================")
print("QUIZ-UL JOCURILOR")
print("==============================")

intrebari = [
    ("Care este personajul principal din Minecraft?", "Steve"),
    ("Care este cel mai popular joc?", "Roblox"),
    ("Ce joc are personaje numite bandits?", "Blox Fruits"),
    ("Care este vehiculul lui Mario?", "Kartul"),
    ("Ce inseamna NPC?", "Non-player character"),
    ("Cu ce te teleportezi in Minecraft?", "Ender pearl"),
    ("Ce capitol de GTA urmeaza sa apara?", "6"),
    ("Care este cel mai bun joc FPS de pe Roblox?", "Rivals"),
    ("Din ce joc vine El Primo?", "Brawl Stars"),
    ("Din ce tara vine Minecraft?", "Suedia"),
    ("Pe ce dispozitiv ai autoshoot?", "Telefon"),
    ("Cum se numeste printesa din Mario?", "Peach"),
    ("Ce joc incepe cu F?", "Fortnite"),
    ("Cum se numeste jocul popular de geografie?", "GeoGuessr")
]

scor = 0

for intrebare, raspuns_corect in intrebari:
    raspuns = input(intrebare + " ")
    
    if raspuns.lower() == raspuns_corect.lower():
        print("Bravo! Ai raspuns corect!")
        scor = scor + 1
    else:
        print("Gresit! Raspunsul corect era:", raspuns_corect)
    print()

print("==============================")
print("Joc terminat! Scorul tau este:", scor, "din", len(intrebari))
print("==============================")


