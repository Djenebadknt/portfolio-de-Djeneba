while True :
    print("Bienevenue dans le convertisseur !")
    print("Que voulez vous convertir ? ")
    print("1. Température")
    print("2. Monnaie")
    print("3. Temps")
    print("4. Longueur")
    print("0.Tapez 0 pour quitter le programme")
    choix = input("Choisissez 1, 2, 3, 4 ou 0 :")


    if choix =="0":
        print("Merci d'avoir utilisé le convertisseur. A bienot !")
        break
    
    elif choix== "1":
        while True : 
            print("Conversion de température")
            choix_temperature = input("Tapez 1 pour convertir °C en °F ou 2 pour °F en °C : ")
            
        
            if choix_temperature =="1" :
                temperature = float(input("Entrez la température à convertir : ")) 
                resultat = temperature * 9/5 + 32
                print(" Résultat : ", resultat," °F")
                break
        
            elif  choix_temperature =="2":
                temperature = float(input("Entrez la température à convertir : ")) 
                resultat = (temperature - 32) * 5/9
                print(" Résultat : ", resultat," °C")
                break
            else:
                print("Choix invalide. Réessayez")
        
    elif choix== "2":
        while True :
            print ("Conversion de monnaie")
            choix_monnaie = input("Tapez 1 pour convertir € en $ ou 2 pour $ en € ")
        
        
            if choix_monnaie =="1" :
                monnaie = float(input("Entrez le montant à convetir : "))
                resultat = monnaie * 1.1
                print(" Résultat : ", resultat,"$")
                break
            elif choix_monnaie =="2":
                monnaie = float(input("Entrez le montant à convetir : "))
                resultat = monnaie / 1.1
                print(" Résultat : ", resultat,"€")
                break
            else:
                print("Choix invalide. Réessayez")


    elif choix== "3":
        while True :
            print("Conversion de temps") 
            choix_temps = input("Tapez 1 pour convertir heures en minutes ou 2 pour minutes en heures ")
        
        
            if choix_temps =="1" :
                temps = float(input("Entrez la valeur à convetir : "))
                resultat = temps * 60
                print(" Résultat : ", resultat,"minutes")
                break
        
            elif choix_temps =="2":
                temps = float(input("Entrez la valeur à convetir : "))
                resultat = temps / 60
                print(" Résultat : ", resultat,"heures")
                break  
            else:
                print("Choix invalide. Réessayez")
            

    elif choix== "4":
        while True :
            print(" Conversion de longueur")
            choix_longueur = input("Tapez 1 pour convertir M en CM ou 2 pour CM en M ")
            
        
            if choix_longueur == "1" :
                longueur = float(input("Entrez la longueur à convetir : "))
                resultat = longueur * 100
                print(" Résultat : ", resultat,"centimètres")
                break

            elif choix_longueur =="2":
                longueur = float(input("Entrez la longueur à convetir : "))
                resultat = longueur / 100
                print(" Résultat : ", resultat,"mètres")
                break
            else:
                print("Choix invalide. Réessayez")

    else:
        print("Choix invalide. Réessayez")