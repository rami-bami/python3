# Boodschappenlijst
def welkom():
    print("Welkom bij je boodschappen lijst")
    print("Je gaat vandaag boodschappen doen en je moet een lijstje maken.")
    print("Ik heb er alvast wat dingen op gezet.")
    print()
    print("--Kies q om te stoppen.")
    print("--Er zit 100 euro in de bank.--")


def keuze_lijst():
    print()
    print("--1: Laat lijstje zien.--")
    print("--2: Voeg product toe aan lijstje.--")
    print("--3: Verwijder product van lijstje.--")
    print("--4: Wijzig product.--")
    print("--5: Koop product van lijstje.--")
    print("--Kies Q om te stoppen.--")
    print("--Kies bank om je geld te zien.--")
    print()


def main(boodschap=None):
    if boodschap is None:
        boodschap = {"brood": 3, "kaas": 2, "sap": 2, "yogurt": 3}
    doorgaan = True

    def toon_lijst():
        print("____________________")
        print("-Boodschappenlijst-")
        for key, value in boodschap.items():
            print(key, value)
        print("____________________")

    while doorgaan:
        bank = 100
        keuze_lijst()
        print("Wat is uw keuze?")
        keuze = input()
        if keuze == "q":  # stopt
            doorgaan = False

        elif keuze == "bank":  # toont je je rekening
            print(bank)

        elif keuze == "1":  # toont menu
            toon_lijst()

        elif keuze == "2":  # voegt product toe
            try:
                print("Welk product wilt u toevoegen?")
                voeg = input()
                print("Wat is de prijs?")
                voeg_prijs = int(input())
                boodschap[voeg] = voeg_prijs
                toon_lijst()

            except ValueError:
                print("Dat is geen getal en dat kan niet.")

        elif keuze == "3":  # verwijdert product
            toon_lijst()
            print("Welk product wilt u verwijderen?")
            remove = input()
            if remove in boodschap:
                del boodschap[remove]
                toon_lijst()

            else:
                print(remove, "staat niet op je lijstje, dus kan je het niet verwijderen.")

        elif keuze == "4":  # wijzigt product
            try:
                toon_lijst()
                print("Welk product moet er gewijzigd worden?")
                edit = input()

                if edit in boodschap:
                    del boodschap[edit]
                    print("Met wat moet het verplaats worden?")
                    voeg_edit = input()
                    print("Wat is de nieuwe prijs?")
                    edit_prijs = int(input())
                    boodschap[voeg_edit] = edit_prijs
                    toon_lijst()

                else:
                    print(edit, "staat niet op je lijstje, dus je kan het niet wijzigen.")

            except ValueError:
                print("Dat is geen getal en dat kan niet.")

        elif keuze == "5":  # koopt product
            toon_lijst()
            print("Welk product wilt u kopen?")
            print("Kies Q om te stoppen met kopen.")
            koop1 = input()
            if koop1 == "q":
                print()

            elif koop1 in boodschap:
                prijs = bank - boodschap[koop1]
                bank -= boodschap[koop1]

                if prijs <= -1:
                    print("Zoveel geld heb je niet!")

                elif bank <= 0:
                    print("Je geld is op!")
                    print("Je hebt gefaald in het leven en in het boodschappen doen.")
                    doorgaan = False

                else:
                    del boodschap[koop1]
                    print("Product is gekocht!")
                    print("Op je bank staat nog", bank, "euro op je bank.")
                    toon_lijst()
                    print("Wilt u nog een product kopen? (Y/N)")
                    nog_een_keer = input()
                    if nog_een_keer == "Y" or "y" or "ja":
                        print("Typ 5, en kies je product.")
                    elif nog_een_keer == "N" or "n" or "nee":
                        print()
            else:
                print("Een van de producten staat niet in je lijstje, dus je kan het niet kopen.")

        else:
            print("Hey! Even normaal blijven doen hè.")
            toon_lijst()


welkom()
main()
