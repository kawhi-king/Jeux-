# Description: Jeu de devinette

import random 


def main():
    #List of words to guess
    easy_words = ["python","soleil","facile", "poulet","maison"]
    average_words = ["variable","boucle","fonction", "tableau", "classe","methode"]
    difficult_words = ["encapsulation", "heritage", "Xavier", "abstraction", "interface"]
    
    #Choose a random word
    #new feature 1: choose the difficulty level
    print("Bienvenue dans le jeu de devinette !")
    print("Je vais choisir un mot au hasard et vous devez le deviner.")
        
    
    print ("Choisissez le niveau de difficulté :")
    print("1. Facile - Tentatives = 10")
    print("2. Moyen - Tentatives = 10")
    print("3. Difficile - Tentatives = 10")
    print ("Prêt à relever le defi ? lancer le jeu et amusez-vous bien !")
    # Choice of difficulty level
    def get_difficulty():
        while True:
            difficulty = input("Entrez le niveau de difficulté  (1, 2 ou 3) : ")
            if difficulty in ['1', '2', '3']:
                return difficulty
            else:
                print("Veuillez entrer un nombre valide 1, 2 ou 3.")
        #if the user types 1, 2 or 3: it activates the
        
        
    #new feature 2: word choice
    difficulty = get_difficulty()
    if  difficulty == "1": 
        mot_a_deviner = random.choice(easy_words)
        Tentatives = 10
       #if the user types 1: it activates easy_words
    elif difficulty == "2":
        mot_a_deviner = random.choice(average_words)
        Tentatives = 10
        #if the user types 2: it activates middle_words
    elif difficulty == "3": 
        mot_a_deviner = random.choice(difficult_words)
        Tentatives = 10
        
       #if the user types 3: it activates difficult_words
        
        
     # Ensure the word is lowercase
    lettres_trouvees = []
    affichage = ["_" for lettre in mot_a_deviner]
    
    # Select a random word

    print(f"Le mot à deviner contient {len(mot_a_deviner)} lettres \n")  # Example: "banana", "apple", "laptop"
    
    # Main loop            
    while Tentatives > 0 and '_' in affichage :
        print (f"Il vous reste {Tentatives} tentatives")
        # Word display
        print(' '.join(affichage))
        # Letter verification
        if Tentatives == 0:
            print("Merci d'avoir joué")
        lettre = input("Entrez une lettre : \n ").lower()
        if len(lettre) == 0:
            print("Entrez une lettre valable.")
        else:
            if lettre not in 'abcdefghijklmnopqrstuvwxyz':
                print("Entrez une lettre valable.")
            if lettre in lettres_trouvees:
                letter_found = "Vous avez déjà proposé la lettre '{0}'".format(lettre)
                print(letter_found)
            if lettre not in mot_a_deviner:
                print("Dommage ! essaie encore")
            else:
                print ("Bien joué !")
            # Display updated
            for i in range(len(mot_a_deviner)):
                if lettre == mot_a_deviner[i]:
                    affichage[i] = lettre  # Valid because display has the same size as word_to_guess 
                # Adding the letter to the list of found letters
                lettres_trouvees.append(lettre)

           # Display current state
            print(' '.join(affichage))
            print("\n")
            Tentatives -= 1
        
    # Displays the result of the game
    if '_' not in  affichage:
        print("👏Félicitations, vous avez trouvé le mot :",(mot_a_deviner))
    else:
        print("👎Vous avez perdu, le mot était :",(mot_a_deviner) )
        #check if user wants to replay or quit the game
        
    while True:
        replay = input("Voulez-vous rejouer ? (O/N) : ").lower()
        if replay == 'o'or replay == 'O':
            main()  #Restart the game
        elif replay == 'n' or replay == 'N':
            print("Merci d'avoir joué ! À la prochaine fois !")
            break
        else:
            print("Veuillez entrer 'O' pour rejoeur ou 'N' pour quitter.")
            
if __name__ == '__main__':
    main()
#End of the program
