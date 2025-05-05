import webbrowser
while True :
    playlist = {
        "joyeuse" :[ 
            ["Happy - Pharrell Williams", "https://youtu.be/ZbZSe6N_BXs?si=gIXLWj_hZ-qv1_61"], 
            ["Can't Stop The Feeling - Justin Timberlake", "https://youtu.be/ru0K8uYEZWw?si=ZINTJ9zlyLwisq3s"]
            ],
        "triste" : [
            ["Fix You - Coldplay", "https://youtu.be/k4V3Mo61fJM?si=xt9gXPun62iHbHaH"],
            ["All I Want - Kodaline","https://youtu.be/mtf7hC17IBM?si=wnYeB4xbOA79_0tF"]
            ] ,
        "motivé" :[
            ["Eye of the Tiger - Survivor", "https://youtu.be/btPJPFnesV4?si=AtWnTY8RKbB2wJPU"],
            ["Stronger - Kanye West", "https://youtu.be/PsO6ZnUZI0g?si=WOpLU2WtgRjbybH8"]
            ],
        "chill" : [
            ["Sunset lover - Night trouble", "https://youtu.be/L1bbk3Ul3YY?si=p8ra5HlLPRH93jA"],
            ["Sunset Lover - Petit Biscuit", "https://youtu.be/4fQeaM62mOY?si=DIplg7J_NyGj3jDF"]
            ],
        "nostalgique" :[
            ["Let Her Go - Passenger", "https://youtu.be/RBumgq5yVrA?si=jPo4eo0cHuaBZADx"],
            ["Someone Like You - Adele", "https://youtu.be/hLQl3WQQoQ0?si=mjDsA2qg_VgpCeOW"]
            ]
    }
    print("Bienvenue dans le générateur de playlist émotionnelle !")
    while True :
        print("Comment vous sentez-vous ?")
        choix= input("Choississez parmis ces émotions : Joyeuse, Triste, Motivé, Chill ou Nostalgique : ").lower()

        if choix in playlist :
            print("Voici la playlist", choix, ":")

            for musique in playlist[choix]:
                print("-", musique[0])
            ecouter = input("Voulez vous écouter ? ( oui / non ) : ").lower()

            if ecouter == "oui" :
                for musique in playlist[choix]:
                    webbrowser.open(musique[1])
                
            break
        else:
            print("Cette émotion n'est pas valide. Réessayez")     