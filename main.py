# Description: Jeu de devinette de mots
import random 


average_notes = 0
notes = []

class main():
    #List of words to guess
    def get_words():
        easy_words = ["banane", "pomme", "orange", "kiwi", "cerise"] #easy
        average_words = ["ananas", "fraise", "mangue", "raisin", "melon"] #average
        difficult_words = ["papaye", "framboise", "cassis", "groseille", "kiwano"] #difficult
        return easy_words, average_words, difficult_words # List of words to guess
    easy_words, average_words, difficult_words = get_words() 
    
    def calculer_score(tentatives_restantes, niveau, mot):
        multiplicateurs = {'1': 1, '2': 1.5, '3': 2}
        return int(tentatives_restantes * len(mot) * multiplicateurs[niveau])
    
    print("Je vais choisir un mot au hasard et vous devez le deviner.")
    print ("Choisissez le niveau de difficulté :")
    print("1. Facile - Tentatives = 10")
    print("2. Moyen - Tentatives = 10")
    print("3. Difficile - Tentatives = 10")
    print ("Prêt à relever le defi ? lancer le jeu et amusez-vous bien !")
    def get_difficulty():
        while True:
            difficulty = input("Entrez le niveau de difficulté  (1, 2 ou 3) : ")
            if difficulty in ['1', '2', '3']:
                return difficulty
            else:
                print("Veuillez entrer un nombre valide 1, 2 ou 3.") 
    difficulty = get_difficulty()
    if  difficulty == "1": 
        mot_a_deviner = random.choice(easy_words)
        Tentatives = 10
    elif difficulty == "2":
        mot_a_deviner = random.choice(average_words)
        Tentatives = 10
    elif difficulty == "3": 
        mot_a_deviner = random.choice(difficult_words)
        Tentatives = 10
    lettres_trouvees = []# List to store found letters
    affichage = ["_" for lettre in mot_a_deviner] # Display the word with underscores
    print(f"Le mot à deviner contient {len(mot_a_deviner)} lettres \n")  # Example: "banana", "apple"
    def get_word():
        return random.choice(easy_words + average_words + difficult_words)          
    while Tentatives > 0 and '_' in affichage :
        print (f"Il vous reste {Tentatives} tentatives")# Word display
        print(' '.join(affichage)) # Display the word with underscores
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
            for i in range(len(mot_a_deviner)):
                if lettre == mot_a_deviner[i]:
                    affichage[i] = lettre  # Valid because display has the same size as word_to_guess 
                lettres_trouvees.append(lettre)
           # Display current state
            print(' '.join(affichage))# Display the word with underscores
            print("\n")
            Tentatives -= 1
        if '_' not in  affichage:
            print("👏Félicitations, vous avez trouvé le mot :",(mot_a_deviner)) # Displays the result of the game
    else:
        print("👎Vous avez perdu, le mot était :",(mot_a_deviner) ) 
        def note_games(): # Function to rate the game
            while True:
                note = input("veuillez noter le jeu de (1-5):")
                if note in ['1', '2', '3', '4', '5']:
                    print("Merci pour votre note !")
                    notes.append(note) # Add the note to the list
                    # Calculate the average of the notes
                    average_notes = sum([int(note) for notes in note]) / len(notes)
                    print(f"Votre note moyenne est : {average_notes}")
                    break
                else: 
                    print("Veuillez entrer une note valide entre 1 et 5.")
        note_games()
    while True:
        replay = input("Voulez-vous rejouer ? (O/N) : ").lower()
        if replay == 'o'or replay == 'O':
            min()  #Restart the game
        elif replay == 'n' or replay == 'N':
            print("Merci d'avoir joué ! À la prochaine fois !")
            break
        else:
            print("Veuillez entrer 'O' pour rejouer ou 'N' pour quitter.") 
if __name__ == '__main__':
    main()
