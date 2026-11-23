print("==============================")
print("QUIZ-UL JOCURILOR")
print("==============================")
intrebari = {
    "nume": "Stiinta",
    "intrebari": [
        {
            "intrebare": "Care este formula chimică a apei?",
            "raspuns_corect": "H2O"
        },
        {
            "intrebare": "Ce planetă este cunoscută ca Planeta Roșie?",
            "raspuns_corect": "Marte"
        },
        {
            "intrebare": "Care este unitatea de măsură pentru electricitate?",
            "raspuns_corect": "Ampere"
        },
        {
            "intrebare": "Ce gaz respirăm pentru a supraviețui?",
            "raspuns_corect": "Oxigen"
        },
        {
            "intrebare": "Care este cel mai mare organ al corpului uman?",
            "raspuns_corect": "Pielea"
        },
        {
            "intrebare": "Ce planetă este cea mai apropiată de Soare?",
            "raspuns_corect": "Mercur"
        },
        {
            "intrebare": "Care este simbolul chimic pentru aur?",
            "raspuns_corect": "Au"
        },
        {
            "intrebare": "Ce organ produce insulina în corpul uman?",
            "raspuns_corect": "Pancreasul"
        },
        {
            "intrebare": "Care este cel mai mare mamifer terestru?",
            "raspuns_corect": "Elefantul"
        },
        {
            "intrebare": "Ce gaz este esențial pentru fotosinteză?",
            "raspuns_corect": "Dioxid de carbon"
        },
        {
            "intrebare": "Care este cel mai rapid animal terestru?",
            "raspuns_corect": "Ghepardul"
        },
        {
            "intrebare": "Ce planetă are inele vizibile?",
            "raspuns_corect": "Saturn"
        },
        {
            "intrebare": "Care este cel mai mare ocean de pe Pământ?",
            "raspuns_corect": "Oceanul Pacific"
        },
        {
            "intrebare": "Ce organ este responsabil pentru pomparea sângelui în corp?",
            "raspuns_corect": "Inima"
        },
        {
            "intrebare": "Care este cel mai mic os din corpul uman?",
            "raspuns_corect": "Stapezul"
        },
        {
            "intrebare": "Ce gaz este principalul component al atmosferei Pământului?",
            "raspuns_corect": "Azot"
        },
        {
            "intrebare": "Care este cel mai mare mamifer marin?",
            "raspuns_corect": "Balena albastră"
        },
        {
            "intrebare": "Ce organ produce bilă în corpul uman?",
            "raspuns_corect": "Ficatul"
        },
        {
            "intrebare": "Care este cel mai rapid pasăre din lume?",
            "raspuns_corect": "Șoimul călător"
        },
        {
            "intrebare": "Ce planetă este cunoscută pentru culoarea sa albastră?",
            "raspuns_corect": "Neptun"
        }
    ]
}
while True:
    print("Ai ales quiz-ul de știință. Răspunde la următoarele întrebări:")
    r=0
    print("Care este formula chimică a apei?")
    if input("Răspuns: ").lower() == "H2O":
        print("Răspuns corect!")
        r=r+1
    else:
        print("Răspuns greșit. Răspunsul corect este H2O.")
    print("Ce planetă este cunoscută ca Planeta Roșie?")
    if input("Răspuns: ").lower() == "marte":
        print("Răspuns corect!")
        r=r+1
    else:
        print("Răspuns greșit. Răspunsul corect este Marte.")
    print("Care este unitatea de măsură pentru electricitate?")
    if input("Răspuns: ").lower() == "ampere":
        print("Răspuns corect!")
        r=r+1
    else:
        print("Răspuns greșit. Răspunsul corect este Ampere.")
    print("Ce gaz respirăm pentru a supraviețui?")
    if input("Răspuns: ").lower() == "oxigen":
        print("Răspuns corect!")
        r=r+1
    else:
        print("Răspuns greșit. Răspunsul corect este Oxigen.")
    print("Care este cel mai mare organ al corpului uman?")
    if input("Răspuns: ").lower() == "pielea":
        print("Răspuns corect!")
        r=r+1
    else:
        print("Răspuns greșit. Răspunsul corect este Pielea.")
    print("Ce planetă este cea mai apropiată de Soare?")
    if input("Răspuns: ").lower() == "mercur":
        print("Răspuns corect!")
        r=r+1
    else:
        print("Răspuns greșit. Răspunsul corect este Mercur.")
    print("Care este simbolul chimic pentru aur?")
    if input("Răspuns: ").lower() == "au":
        print("Răspuns corect!")
        r=r+1
    else:
        print("Răspuns greșit. Răspunsul corect este Au.")
    print("Ce organ produce insulina în corpul uman?")
    if input("Răspuns: ").lower() == "pancreasul":
        print("Răspuns corect!")
        r=r+1
    else:
        print("Răspuns greșit. Răspunsul corect este Pancreasul.")
    print("Care este cel mai mare mamifer terestru?")
    if input("Răspuns: ").lower() == "elefantul":
        print("Răspuns corect!")
        r=r+1
    else:
        print("Răspuns greșit. Răspunsul corect este Elefantul.")
    print("Ce gaz este esențial pentru fotosinteză?")
    if input("Răspuns: ").lower() == "dioxid de carbon":
        print("Răspuns corect!")
        r=r+1
    else:
        print("Răspuns greșit. Răspunsul corect este Dioxid de carbon.")
    print("Care este cel mai rapid animal terestru?")
    if input("Răspuns: ").lower() == "ghepardul":
        print("Răspuns corect!")
        r=r+1
    else:
        print("Răspuns greșit. Răspunsul corect este Ghepardul.")
    print("Ce planetă are inele vizibile?")
    if input("Răspuns: ").lower() == "saturn":
        print("Răspuns corect!")
        r=r+1
    else:
        print("Răspuns greșit. Răspunsul corect este Saturn.")
    print("Care este cel mai mare ocean de pe Pământ?")
    if input("Răspuns: ").lower() == "oceanul pacific":
        print("Răspuns corect!")
        r=r+1
    else:
        print("Răspuns greșit. Răspunsul corect este Oceanul Pacific.")
    print("Ce organ este responsabil pentru pomparea sângelui în corp?")
    if input("Răspuns: ").lower() == "inima":
        print("Răspuns corect!")
        r=r+1
    else:
        print("Răspuns greșit. Răspunsul corect este Inima.")
    print("Care este cel mai mic os din corpul uman?")
    if input("Răspuns: ").lower() == "stapezul":
        print("Răspuns corect!")
        r=r+1
    else:
        print("Răspuns greșit. Răspunsul corect este Stapezul.")
    print("Ce gaz este principalul component al atmosferei Pământului?")
    if input("Răspuns: ").lower() == "azot":
        print("Răspuns corect!")
        r=r+1
    else:
        print("Răspuns greșit. Răspunsul corect este Azot.")
    print("Care este cel mai mare mamifer marin?")
    if input("Răspuns: ").lower() == "balena albastră":
        print("Răspuns corect!")
        r=r+1
    else:
        print("Răspuns greșit. Răspunsul corect este Balena albastră.")
    print("Ce organ produce bilă în corpul uman?")
    if input("Răspuns: ").lower() == "ficatul":
        print("Răspuns corect!")
        r=r+1
    else:
        print("Răspuns greșit. Răspunsul corect este Ficatul.")
    print("Care este cel mai rapid pasăre din lume?")
    if input("Răspuns: ").lower() == "șoimul călător":
        print("Răspuns corect!")
        r=r+1
    else:
        print("Răspuns greșit. Răspunsul corect este Șoimul călător.")
    print("Ce planetă este cunoscută pentru culoarea sa albastră?")
    if input("Răspuns: ").lower() == "neptun":
        print("Răspuns corect!")
        r=r+1
    else:
        print("Răspuns greșit. Răspunsul corect este Neptun.")
    if r == 20:
        print("Felicitări! Ai răspuns corect la toate întrebările!")
    else:
        print(f"Ai răspuns corect la {r} întrebări din 20.")
    print("Ai dorit să încerci din nou?")
    print("1. Da")
    print("2. Nu")
    if input("Alege o opțiune (1 sau 2): ") == "2":
        print("Mulțumim pentru participare! La revedere!")
        break