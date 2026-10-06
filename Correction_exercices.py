# ====================================================#
#===============CORRECTION DES EXERCICES==============#
#=====================================================#

# -- Tous les exercices données sont corrigés;
# -- Pour eviter de se perdre decommenter un à un puis lancer----#
# --- analyser les resultat via le fichier pdf
# ---------------------------------------------------------------#
 

# =====================================================#
# ================EXERCICE 1:==========================#
# =====================================================#
# 1er cas : 
# 1ere etape  : Importation d'un module pour pouvoir gerer le temps d'affichage
# import time
# 2eme etape : on fait la boucle des tours en imbriquant la boucle des fois pour chaque tour
# for tour in range(5):
#     print("=============Tour",tour)
#     for fois in range(5):
#         print("Bonjour")
#         time.sleep(1)
#         print("Bonsoir")
#         time.sleep(1)
#  2eme cas : 
# for tour in range(5):
#     print("============= Tour", tour + 1)

#     for fois in range(5):
#         print("Bonjour")

#         for i in range(10000000):
#             pass

#         print("Bonsoir")

#         for i in range(10000000):
#             pass

# =====================================================#
# ================EXERCICE 2:==========================#
# =====================================================#

# somme = 0
# produit = 1
# list_nombre = []

# # 1ere etape : On demande utilisateur de saisir le nombre fois qu'il souhaite taper un nombre
# while True:
#     try:
#         n = int(input("Veuillez saisir le nombre de valeurs à saisir : "))

#         if n > 0:
#             break
#         else:
#             print("Veuillez saisir un nombre entier strictement positif.")

#     except ValueError:
#         print("Entrez un nombre entier valide (pas de lettres).")

# # #  2eme etape : Saisir le nombre selon les fois precises predemment:
# for i in range(n):
#     while True:
#         try:
#             nombre = int(input(f"Veuillez saisir le nombre {i + 1} : "))
#             list_nombre.append(nombre)
#             break

#         except ValueError:
#             print("Entrez un nombre entier valide (pas de lettres).")

# #  3eme etape :
# # Calculer la somme des nombres pairs
# # Calculer le produit des nombres impairs
# for nombre in list_nombre:

#     if nombre % 2 == 0:
#         somme = somme + nombre

#     else:
#         produit = produit * nombre
# # 4eme etape :  Affichage des résultats obtenus
# print("Les nombres saisis :", list_nombre)
# print("La somme des nombres pairs :", somme)
# print("Le produit des nombres impairs :", produit)
# print("La différence entre les deux résultats :", produit-somme)

# =====================================================#
# ================EXERCICE 3:==========================#
# =====================================================#
# 1ere etape : Taper un nombre n'importe qu'il soit!

# while True:
#     try:
#         nombre = int(input("Veuillez taper un nombre entier : "))
#         break

#     except ValueError:
#         print("Erreur : vous devez taper un nombre entier.")

# # 2ere etape : verification et affichager d'un message de la valeur saisie!

# if nombre > 0:
#     print("Vous avez saisi un nombre positif.")

# elif nombre < 0:
#     print("Vous avez saisi un nombre négatif.")

# else:
#     print("Vous avez saisi un nombre nul.")

# =====================================================#
# ================EXERCICE 4:==========================#
# =====================================================#
# 1ere etape : Taper un nombre strictement positif! le nombre negatif prise en compte
# somme = 0 
# while True:
#     try:
#         nombre = int(input("Veuillez taper un nombre entier : "))
#         if nombre > 0:
#             break
#         else:
#             print("Veuillez saisir un nombre entier strictement positif.")

#     except ValueError:
#         print("Erreur : vous devez taper un nombre entier.")

# # 2eme etape : Affichage demandée!

# for i in range(1,nombre+1):
#     print(i)
#     somme = somme+i
# print("voici la somme",somme)

# =====================================================#
# ================EXERCICE 5:==========================#
# =====================================================#

# # 1ere etape : Taper un nombre strictement positif! le nombre negatif prise en compte
# produit=1
# while True:
#     try:
#         nombre = int(input("Veuillez taper un nombre entier : "))
#         if nombre > 0:
#             break
#         else:
#             print("Veuillez saisir un nombre entier strictement positif.")

#     except ValueError:
#         print("Erreur : vous devez taper un nombre entier.")
        
# # 2eme etape :  Faire la multiplication et affichage de la table de multiplication
# for i in range(1,11):
#     # print(i)
#     produit = nombre*i
#     print(nombre,"*",i,"=",produit)

# =====================================================#
# ================EXERCICE 6:==========================#
# =====================================================#
# list_nombre = []
# somme = 0
# moyenne = 0
# while True:
#     try:
#         nombre = int(input("Veuillez taper un nombre entier : "))
#         list_nombre.append(nombre)
#         if nombre == 0:
#             break
#     except ValueError:
#         print("Erreur : vous devez taper un nombre entier.")
        
# print("voici notre liste construite:",list_nombre)
# for compteur in range(0,len(list_nombre)):
   
#     somme = somme+list_nombre[compteur]
#     moyenne = somme/len(list_nombre)

# # Affichage des resultats:
# print("la somme des elements de liste est",somme)
# print("la moyenne depend de la taille des nombres saisi donc on prend la somme qui est",somme,"divise par",len(list_nombre),"qui est egale a :",moyenne)

# =====================================================#
# ================EXERCICE 7:==========================#
# =====================================================#

# # 1ere étape : saisir un nombre strictement positif
# while True:
#     try:
#         n = int(input("Veuillez saisir le nombre de notes à saisir : "))

#         if n > 0:
#             break
#         else:
#             print("Veuillez saisir un nombre entier strictement positif.")

#     except ValueError:
#         print("Entrez un nombre entier valide (pas de lettres).")


# # 2eme étape : remplissage de la liste
# list_note = []

# for i in range(n):

#     while True:
#         try:
#             note = int(input("Veuillez saisir la note : "))
#             if note >= 0 and note <= 20:
#                 list_note.append(note)
#                 break
#             else:
#                 print("Erreur : la note doit être comprise entre 0 et 20.")

#         except ValueError:
#             print("Erreur : vous devez taper un nombre entier.")


# # 3eme étape : calcul de la moyenne et recherche
# # de la note maximale et minimale

# somme = 0
# note_max = list_note[0]
# note_min = list_note[0]

# for i in range(len(list_note)):

#     note_trouve = list_note[i]

#     somme = somme + note_trouve

#     if note_trouve > note_max:
#         note_max = note_trouve

#     if note_trouve < note_min:
#         note_min = note_trouve

# # Calcul de la moyenne
# moyenne = somme / len(list_note)
# # 4eme étape : affichage des résultats

# print("Les notes saisies :", list_note)
# print("La moyenne générale :", moyenne)
# print("La note la plus basse :", note_min)
# print("La note la plus élevée :", note_max)

# if moyenne >= 10:
#     print("L'étudiant est admis.")
# else:
#     print("L'étudiant a échoué.")
    
# =====================================================#
# ================EXERCICE 8:==========================#
# =====================================================#

# # 1ere étape : préciser le nombre d'utilisateurs que vous souhaitez saisir

# while True:
#     try:
#         n_utilisateur = int(input("Veuillez taper le nombre d'utilisateurs que vous voulez saisir : "))

#         if n_utilisateur > 0:
#             break
#         else:
#             print("Veuillez saisir un nombre entier strictement positif.")

#     except ValueError:
#         print("Erreur : vous devez taper un nombre entier.")


# # 2eme étape : remplir la liste

# user_list = []

# for i in range(n_utilisateur):
#     print("Utilisateur numéro", i + 1)

#     user = input("Utilisateur : ")
#     user_list.append(user)


# print("La liste des utilisateurs est :", user_list)


# # 3eme étape : filtrer les noms de plus de 5 caractères

# user_list_with_five_caractere = []

# for user in range(len(user_list)):

#     user_five = user_list[user]

#     if len(user_five) > 5:
#         user_list_with_five_caractere.append(user_five)


# # 4eme étape : afficher le résultat

# print("Voici les utilisateurs ayant plus de 5 caractères :")
# print(user_list_with_five_caractere)

# =====================================================#
# ================EXERCICE 9:==========================#
# =====================================================#

# # 1ere étape : préciser le nombre de prix à saisir

# while True:
#     try:
#         n_prix = int(input("Veuillez taper le nombre de prix que vous voulez saisir : "))

#         if n_prix > 0:
#             break
#         else:
#             print("Veuillez saisir un nombre entier strictement positif.")

#     except ValueError:
#         print("Erreur : vous devez taper un nombre entier.")


# # 2eme étape : remplir la liste

# prix_list = []
# total_prix = 0

# for i in range(n_prix):

#     while True:
#         try:
#             prix = int(input("Veuillez saisir le prix : "))

#             if prix > 0:
#                 prix_list.append(prix)
#                 break
#             else:
#                 print("Erreur : le prix doit être strictement positif.")

#         except ValueError:
#             print("Erreur : vous devez taper un nombre entier.")


# # 3eme étape : calculer le total

# for j in range(len(prix_list)):
#     total_prix = total_prix + prix_list[j]


# # 4eme étape : appliquer la réduction si nécessaire

# if total_prix > 100:
#     reduction = total_prix * 10 / 100
#     total_prix = total_prix - reduction
#     print("Une réduction de 10% a été appliquée.")
# else:
#     print("Aucune réduction n'a été appliquée.")


# # 5eme étape : affichage

# print("Les prix saisis :", prix_list)
# print("Le total final à payer :", total_prix)

# =====================================================#    
# ================EXERCICE 10:=========================#
# =====================================================#

# # 1ere étape : demander une phrase à l'utilisateur

# phrase = input("Veuillez saisir une phrase : ")

# # 2eme étape : créer une fonction qui compte les caractères

# def compter_caracteres(phrase):
#     nombre_caracteres = 0

#     for caractere in phrase:
#         nombre_caracteres = nombre_caracteres + 1

#     return nombre_caracteres


# # 3eme étape : créer une fonction qui compte les voyelles

# def compter_voyelles(phrase):
#     nombre_voyelles = 0

#     for caractere in phrase:
#         if caractere in "aeiouAEIOU":
#             nombre_voyelles = nombre_voyelles + 1

#     return nombre_voyelles


# # 4eme étape : appeler les fonctions

# nombre_caracteres = compter_caracteres(phrase)
# nombre_voyelles = compter_voyelles(phrase)


# # 5eme étape : afficher les résultats

# print("La phrase saisie :", phrase)
# print("Le nombre de caractères :", nombre_caracteres)
# print("Le nombre de voyelles :", nombre_voyelles)

# # =====================================================#
# # ================EXERCICE 11:=========================#
# # =====================================================#

# # 1ere étape : demander combien de nombres l'utilisateur veut saisir

# while True:
#     try:
#         n = int(input("Combien de nombres voulez-vous saisir ? : "))

#         if n > 0:
#             break
#         else:
#             print("Veuillez saisir un nombre entier strictement positif.")

#     except ValueError:
#         print("Erreur : vous devez saisir un nombre entier.")


# # 2eme étape : remplir la liste

# liste_nombres = []

# for i in range(n):

#     while True:
#         try:
#             nombre = int(input("Veuillez saisir le nombre : "))
#             liste_nombres.append(nombre)
#             break

#         except ValueError:
#             print("Erreur : vous devez saisir un nombre entier.")


# # 3eme étape : afficher la liste

# print("La liste des nombres :", liste_nombres)


# # 4eme étape : demander le nombre à rechercher

# while True:
#     try:
#         nombre_recherche = int(input("Quel nombre voulez-vous rechercher ? : "))
#         break

#     except ValueError:
#         print("Erreur : vous devez saisir un nombre entier.")


# # 5eme étape : rechercher le nombre dans la liste

# position = -1

# for i in range(len(liste_nombres)):

#     if liste_nombres[i] == nombre_recherche:
#         position = i
#         break


# # 6eme étape : afficher le résultat

# if position != -1:
#     print("Le nombre", nombre_recherche, "existe dans la liste.")
#     print("Sa position est :", position)
# else:
#     print("Le nombre", nombre_recherche, "n'existe pas dans la liste.")

# # =====================================================#
# # ================EXERCICE 12:=========================#
# # =====================================================#

# # 1ere étape : demander combien de nombres l'utilisateur veut saisir

# while True:
#     try:
#         n = int(input("Combien de nombres voulez-vous saisir ? : "))

#         if n > 0:
#             break
#         else:
#             print("Veuillez saisir un nombre entier strictement positif.")

#     except ValueError:
#         print("Erreur : vous devez saisir un nombre entier.")


# # 2eme étape : remplir la liste

# liste_nombres = []

# for i in range(n):

#     while True:
#         try:
#             nombre = int(input("Veuillez saisir le nombre : "))
#             liste_nombres.append(nombre)
#             break

#         except ValueError:
#             print("Erreur : vous devez saisir un nombre entier.")


# # 3eme étape : afficher la liste avant le tri

# print("Liste avant le tri :", liste_nombres)


# # 4eme étape : trier la liste manuellement

# for i in range(len(liste_nombres)):

#     for j in range(i + 1, len(liste_nombres)):

#         if liste_nombres[i] > liste_nombres[j]:

#             temporaire = liste_nombres[i]

#             liste_nombres[i] = liste_nombres[j]

#             liste_nombres[j] = temporaire


# # 5eme étape : afficher la liste après le tri

# print("Liste après le tri :", liste_nombres)

# # =====================================================#
# # ================EXERCICE 13:=========================#
# # =====================================================#

# # 1ere étape : créer une fonction qui vérifie le mot de passe

# def verifier_mot_de_passe(mot_de_passe):

#     # Vérifier si le mot de passe contient au moins 6 caractères
#     if len(mot_de_passe) < 6:
#         return False

#     # Vérifier s'il contient au moins un chiffre
#     contient_chiffre = False

#     for caractere in mot_de_passe:

#         if caractere >= "0" and caractere <= "9":
#             contient_chiffre = True
#             break

#     # Vérifier le résultat
#     if contient_chiffre == True:
#         return True
#     else:
#         return False


# # 2eme étape : demander le mot de passe

# while True:

#     mot_de_passe = input("Veuillez saisir votre mot de passe : ")


#     # 3eme étape : vérifier le mot de passe

#     if verifier_mot_de_passe(mot_de_passe):
#         print("Mot de passe valide.")
#         break

#     else:
#         print("Mot de passe invalide.")
#         print("Le mot de passe doit contenir au moins 6 caractères")
#         print("et au moins un chiffre.")


# # =====================================================#
# # ================EXERCICE 14:=========================#
# # =====================================================#

# # 1ere étape : demander combien d'utilisateurs seront enregistrés

# while True:
#     try:
#         n = int(input("Combien d'utilisateurs voulez-vous enregistrer ? : "))

#         if n > 0:
#             break
#         else:
#             print("Veuillez saisir un nombre entier strictement positif.")

#     except ValueError:
#         print("Erreur : vous devez saisir un nombre entier.")


# # 2eme étape : créer la liste des utilisateurs

# liste_utilisateurs = []


# # 3eme étape : enregistrer les utilisateurs

# for i in range(n):

#     print("Utilisateur numéro", i + 1)

#     nom = input("Veuillez saisir le nom : ")

#     while True:
#         try:
#             age = int(input("Veuillez saisir l'âge : "))

#             if age >= 0:
#                 break
#             else:
#                 print("L'âge ne peut pas être négatif.")

#         except ValueError:
#             print("Erreur : vous devez saisir un nombre entier.")


#     # Créer une liste contenant le nom et l'âge
#     utilisateur = [nom, age]

#     # Ajouter l'utilisateur dans la liste principale
#     liste_utilisateurs.append(utilisateur)


# # 4eme étape : créer une fonction pour afficher les utilisateurs majeurs

# def afficher_utilisateurs_majeurs(liste):

#     print("===== UTILISATEURS MAJEURS =====")

#     for i in range(len(liste)):

#         utilisateur = liste[i]

#         nom = utilisateur[0]
#         age = utilisateur[1]

#         if age >= 18:
#             print("Nom :", nom)
#             print("Age :", age)
#             print("--------------------")


# # 5eme étape : afficher tous les utilisateurs enregistrés

# print("===== TOUS LES UTILISATEURS =====")

# for i in range(len(liste_utilisateurs)):

#     utilisateur = liste_utilisateurs[i]

#     print("Nom :", utilisateur[0])
#     print("Age :", utilisateur[1])
#     print("--------------------")


# # 6eme étape : afficher uniquement les utilisateurs majeurs

# afficher_utilisateurs_majeurs(liste_utilisateurs)





    
        

        
        
    

    
    
    