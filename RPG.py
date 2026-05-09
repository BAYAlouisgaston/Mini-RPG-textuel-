#ajout d'un module pour importer des données aleatoire
Import random 
#systeme de combat
def lance_combat(potion_joueur): 
  pv_j = 150
  pv_m = 100
  print("Un loup apparait !!! ")
  print("\n--- UN LOUP BARRE LE CHEMIN ! ---")
  while pv_j>0 and pv_m>0:
   print(f"Tes PV: {pv_j} | PV Monstre: {pv_m} | Potions: {potions_joueur}")
   action = input("Action (ATTAQUER / SOIGNER) :").lower()
   if action == "attaquer":
    degats =random.randint(10,30)
    pv_m -= degats 
    print(f"Tu as infliger  un  coup!! -{degats} PV pour le loup!!.")
   elif action == "soigner":
           if potions_joueur > 0:
               soin = random.randint(20, 40)
                pv_j += soin
                potions_joueur -= 1
                print(f"Potion bue ! +{soin} PV. Il te reste {potions_joueur} potions.")
            else:
                print("tu n'a plus de  potions !")
