class To_do:
    def __init__(self, todo=[]):
        self.todo = todo
        self.quit_program = ""

    def edit(self):
        try:
            l = int(input("Veuillez choisir un numéro d'item à modifier: "))

        except:
            print("Ceci n'est pas un numero d'item")
            self.edit()

        else:
            v = input("Veuillez renseigner un nouveau contenu pour cette item: ")
            self.todo[l-1] = v
            self.write()


    def add(self):
        task = input("Quelle tâche voulez-vous ajouter ? ")
        if not task in self.todo:
            self.todo += task
            print("La tâche {} a bien été ajoutée.".format(task))
        
    def remove(self):
        task = input("Quelle tâche(s) voulez-vous supprimer ? ")
        if task in self.todo:
            if input("Etes-vous sûr (Y/N) ? ").upper() == "Y":
                self.todo.remove(task)
                print("La tâche {} a bien été supprimée.".format(task))
        else:
            print("La tâche {} n'existe pas.".format(task))


todo = To_do()

while todo.quit_program != "oui":

    ####### CODE #####

    if todo.quit_program == "oui":
    ###### CODE #####
       import pandas as pd

       if str(input("Voulez-vous ecrire votre TO-DO dans un fichier csv ? Y/N ")) == "Y" :
           todo = pd.DataFrame(todo)
           todo.to_csv('to_do.csv', sep = '\t')

       break
