import random
import sys

r=random.randint(0,100)

NOMBRE_ESSAI= 5
ESSAI = NOMBRE_ESSAI
print("""
*** Le jeu du nombre mystère***
*** Il te reste 5 essais***
""")
while True:
    
    PLAYER_CHOICE=input("Devine le nombre:")

    if not PLAYER_CHOICE.isdigit():
        print("Veuillez entrer un nombre valide.")
        print(f"Il te reste {ESSAI} essais")
    else:
        ESSAI-=1
        if r < int(PLAYER_CHOICE):
            print(f"Le nombre mystère est plus petit que {PLAYER_CHOICE}")
            print(f"Il te reste {ESSAI} essais")
        elif r > int(PLAYER_CHOICE):
            print(f"Le nombre mystère est plus grand que {PLAYER_CHOICE}")
            print(f"Il te reste {ESSAI} essais")
        elif r == int(PLAYER_CHOICE):
            print(f"Bravo ! Le nombre mystère était bien {r}")
            print(f"Tu as trouvé le nombre en {NOMBRE_ESSAI-ESSAI} essai")
            print(f"Fin du jeu")
            sys.exit()
        if ESSAI== 0:
            print(f"Dommage ! Le nombre mystère était {r}")
            print("Fin du jeu")
            sys.exit()
# sys.exit()
#*** Le jeu du nombre mystère***
#*** Il te reste 5 essais***
#Devine le nombre:

#1
#si on entre autre chose qu'un nombre, on affiche
#"Veuillez entrer un nombre valide."
#"Il te reste 5 essais"
#"Devine le nombre"

#2
#On rentre un nombre X
#Le programme affiche:
#"Le nombre mystère est plus petit que X"
#"Il te reste 4 essais"
#"Devine le nombre :"

#3
#Si on ne trouve pas le nombre mystère avant la fin des 5 essais
#Le programme affiche:
#"Dommage ! Le nombre mystère était Y"
#"Fin du jeu."

#4
#Si trouve le nombre mystère avant la fin des 5 essais
#Le programme affiche:
#"Bravo ! Le nombre mystère était bien Y"
#"Tu as trouvéle nombre en X essai"
#"Fin du jeu."
