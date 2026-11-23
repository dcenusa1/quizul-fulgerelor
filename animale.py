intrebari = [
    ["Care este cel mai mare animal de pe planeta?", "A. Elefantul", "B. Balena albastra", "C. Girafa", "B"],
    ["Care este regele junglei?", "A. Leul", "B. Tigrul", "C. Lupul", "A"],
    ["Cate picioare are un paianjen?", "A. 6", "B. 8", "C. 10", "B"],
    ["Care este cel mai rapid animal terestru?", "A. Leopardul", "B. Ghepardul", "C. Calul", "B"],
    ["Ce pasare poate zbura pe loc?", "A. Vulturul", "B. Barza", "C. Colibri", "C"],
    ["Cum se numeste puiul broastei?", "A. Mormoloc", "B. Boboc", "C. Larva", "A"],
    ["Ce animal are gatul cel mai lung?", "A. Girafa", "B. Strutul", "C. Camila", "A"],
    ["Care dintre acestea este mamifer?", "A. Crocodilul", "B. Delfinul", "C. Rechinul", "B"],
    ["Ce mananca panda in principal?", "A. Carne", "B. Bambus", "C. Peste", "B"],
    ["Ce animal isi schimba culoarea?", "A. Cameleonul", "B. Vulpea", "C. Iepurele", "A"],
    ["Cate inimi are o caracatita?", "A. Una", "B. Doua", "C. Trei", "C"],
    ["Care este cea mai mare pasare din lume?", "A. Vulturul", "B. Strutul", "C. Condorul", "B"],
    ["Ce animal are o memorie foarte buna?", "A. Elefantul", "B. Pisica", "C. Veverita", "A"],
    ["Ce animal produce miere?", "A. Fluturele", "B. Albina", "C. Furnica", "B"],
    ["Care dintre acestea este reptila?", "A. Broasca", "B. Soparla", "C. Delfinul", "B"],
    ["Ce animal traieste si in apa, si pe uscat?", "A. Broasca", "B. Girafa", "C. Leul", "A"],
    ["Cum se numeste grupul de lupi?", "A. Haita", "B. Turma", "C. Stol", "A"],
    ["Ce animal are dungi alb-negre?", "A. Zebra", "B. Ursul", "C. Panda", "A"],
    ["Care este cel mai mare animal terestru?", "A. Rinocerul", "B. Elefantul african", "C. Hipopotamul", "B"],
    ["Ce animal foloseste ecolocatia pentru a se orienta?", "A. Liliacul", "B. Vulturul", "C. Calul", "A"]
]

scor = 0

print("BINE AI VENIT LA QUIZUL DESPRE ANIMALE!")
nume = input("Cum te numesti? ")
print("Succes,", nume, "!")

for i in range(20):
    print()
    print("Intrebarea", i + 1, "din 20")
    print(intrebari[i][0])
    print(intrebari[i][1])
    print(intrebari[i][2])
    print(intrebari[i][3])

    raspuns = input("Raspunsul tau (A/B/C): ").upper()

    while raspuns != "A" and raspuns != "B" and raspuns != "C":
        print("Alege doar A, B sau C!")
        raspuns = input("Raspunsul tau: ").upper()

    if raspuns == intrebari[i][4]:
        print("BRAVO! Raspuns corect!")
        scor = scor + 1
    else:
        print("NU ESTE CORECT!")
        print("Raspunsul corect era:", intrebari[i][4])

    input("Apasa ENTER pentru urmatoarea intrebare...")

print()
print("================================")
print("          REZULTAT FINAL")
print("================================")
print("Jucator:", nume)
print("Raspunsuri corecte:", scor)
print("Raspunsuri gresite:", 20 - scor)
print("Scor final:", scor, "/ 20")
print("================================")

if scor >= 18:
    print("EXCELENT! Esti un expert in animale!")
elif scor >= 15:
    print("FOARTE BINE! Te pricepi la animale!")
elif scor >= 10:
    print("BINE! Mai ai cateva lucruri de invatat!")
else:
    print("MAI EXERSEAZA! Data viitoare vei fi mai bun!")

print("Multumim pentru participare,", nume, "!")