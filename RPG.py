#ajout d'un module pour importer des données aleatoire
import random
#systeme de combat
def lance_combat(potions_joueur):
    pv_j = 150
    pv_m = 135
    print("Un loup apparait !!! ")
    print("\n--- UN LOUP BARRE LE CHEMIN ! ---")
    while pv_j>0 and pv_m>0:
        print(f"Tes PV: {pv_j} | PV Monstre: {pv_m} | Potions: {potions_joueur}")
        action = input("Action (ATTAQUER / SOIGNER) :").lower()
        if action == "attaquer":
            degats =random.randint(10,30)
            pv_m -= degats
            print(f"Tu as infligé  un  coup!! -{degats} PV pour le loup!!.")
        elif action == "soigner":
            if potions_joueur > 0:
                soin = random.randint(25, 40)
                pv_j += soin
                potions_joueur -= 1
                print(f"Potion bue ! +{soin} PV. Il te reste {potions_joueur} potions.")
            else:
                print("tu n'as plus de  potions !")
        # Tour du monstre
        if pv_m > 0:
            degats_m = random.randint(10, 30)
            pv_j -= degats_m
            print(f"Le loup te mord ! -{degats_m} PV.")  #
    if pv_j>0:
        print("\nVictoire ! Tu peux continuer ta route.")
        return True, potions_joueur
        # On renvoie de la victoire ET le reste de potions
    else:
        print("\nC'est la fin de ton aventure... GAME OVER.")  
        return False, potions_joueur
#  FONCTION PRINCIPALE (EXPLORATION)
def jeu():
    stock_potions = 1 # Le joueur commence avec une seule potion
    print("Bienvenue dans cette mini aventure !")
   
    #  Le Village
    print("\nTu es au village. Un vieux sage te donne une potion gratuite.")
    stock_potions += 1
    print(f"Tu as maintenant {stock_potions} potions.")
   
    #   Le Choix de la grotte
    choix = input("\nVeux-tu entrer dans la GROTTE ou RESTER au village ? ").lower()
   
    if choix == "grotte":
        # On lance le combat et on récupère les résultats
        vivant, stock_potions = lance_combat(stock_potions)
       
        if vivant:
            print(f"\nTu sors de la grotte avec {stock_potions} potions en poche.")
            print("Félicitations, tu as terminé cette démo !")
    else:
        print("\nTu restes au village tranquillement et le vieil homme te laisse une étrange épée. Fin de cette démo.")
# --- LANCEMENT ---
jeu()
