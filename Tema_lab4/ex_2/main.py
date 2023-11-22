def inlocuieste_cuvant_in_fisier(cale_fisier, cuvant_de_inlocuit, cuvant_inlocuitor):
    try:
        with open(cale_fisier, 'r', encoding='utf-8') as fisier:
            continut = fisier.read()
        numar_inlocuiri = continut.count(cuvant_de_inlocuit)
        continut_nou = continut.replace(cuvant_de_inlocuit, cuvant_inlocuitor)
        with open(cale_fisier, 'w', encoding='utf-8') as fisier:
            fisier.write(continut_nou)
        return numar_inlocuiri
    except FileNotFoundError:
        return "Eroare: Fișierul nu a fost găsit."
    except Exception as e:
        return f"Eroare: {e}"

cale_fisier = 'date.txt'
cuvant_de_inlocuit = 'vechi'
cuvant_inlocuitor = 'nou'
numar_inlocuiri = inlocuieste_cuvant_in_fisier(cale_fisier, cuvant_de_inlocuit, cuvant_inlocuitor)

if isinstance(numar_inlocuiri, int):
    print(f"Rezultat: Înlocuit '{cuvant_de_inlocuit}' cu '{cuvant_inlocuitor}' în {numar_inlocuiri} locuri.")
else:
    print(numar_inlocuiri)
