import random

class Quiz:
    def __init__(self):
        self.score = 0

    def question(self):
        questions = [
            {"Question": "Quelle est la capitale de la France ?",
             "Options": ["A) Paris", "B) Londres", "C) Berlin", "D) Madrid"],
             "Reponse": "A"},

            {"Question": "Quel est le plus grand océan du monde ?",
             "Options": ["A) Atlantique", "B) Indien", "C) Arctique", "D) Pacifique"],
             "Reponse": "D"},

            {"Question": "Quelle est la capitale du Gabon ?",
             "Options": ["A) Libreville", "B) Port-Gentil", "C) Franceville", "D) Omboué"],
             "Reponse": "A"},

            {"Question": "Quel est le plus grand pays du monde ?",
             "Options": ["A) Canada", "B) Chine", "C) Russie", "D) États-Unis"],
             "Reponse": "C"},

            {"Question": "Quel est le plus petit pays du monde ?",
             "Options": ["A) Monaco", "B) Vatican", "C) Nauru", "D) Saint-Marin"],
             "Reponse": "B"},
        ]
        return questions

    def start_quiz(self):
        questions = self.question()
        random.shuffle(questions)
        print("Bienvenue dans le quiz !")
        for q in questions:
            print(q["Question"])
            for option in q["Options"]:
                print(option)
            answer = input("Entrez votre réponse (A, B, C ou D) : ").upper()
            if answer == q["Reponse"]:
                print("Correct !\n")
                self.score += 1
            else:
                print("Incorrect. La bonne réponse est :", q["reponse"], "\n")

        print("Quiz terminé ! Votre score est :", self.score, "/", len(questions))
        
        replay = input("Voulez-vous rejouer ? (O/N) : ").upper()
        if replay == "O" or replay == "o":
            self.score = 0
        elif replay == "N" or replay == "n":
            print("Merci d'avoir joué !")
            return
        else:
            print("Réponse invalide. Veuillez entrer O ou N.")
            self.start_quiz()

if __name__ == "__main__":
    quiz = Quiz()
    quiz.start_quiz()
