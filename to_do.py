class To_do:

    def __init__(self, todo=[]):
        self.todo = todo
        self.quit_program = ""

    def show_todo(self):
        print("\nVoici votre to-do du jour \n ------- \n")
        for item in self.todo:
            print(item)
        print("\n")

    def ajout_item(self, todo):
        item = input("Que devez vous faire ? \n Si vous devez ajouter plusieurs todo à la fois, séparez les par une virgule")
        new_items = item.split(",")
        for item in new_items:
            todo += [item]
        return todo

    def enlever_item(self, todo):
        item = input("Qu'avez vous fait ? \n Si vous avez fait plusieurs todo to à la fois, séparez les par une virgule")
        remove_items = item.split(",")
        for item in remove_items:
            todo.remove(item)
        return todo

to_do = To_do()

while to_do.quit_program != "oui":

    to_do.show_todo()

    ajouter = input("Voulez vous ajouter un item --> Ecrivez OUI ou NON \n")
    ajouter = ajouter.lower()

    if ajouter == "oui":
        to_do.ajout_item(to_do.todo)
        to_do.show_todo()

    elif ajouter == "non":
        enlever = input("Voulez vous enlever un item --> Ecrivez OUI ou NON \n")
        enlever = enlever.lower()
        if enlever == "oui":
            to_do.enlever_item(to_do.todo)
            to_do.show_todo()
        else:
            print("Okay, votre to-do reste la suivante \n")
            to_do.show_todo()
    else:
        print("Je ne suis pas sur d'avoir compris")

    quit_program = input("Souhaitez vous sortir de l'application ? Tapez OUI pour sortir ou NON pour revoir votre TODO")
    quit_program = quit_program.lower()

    if quit_program == "oui":
        import pandas as pd
        todo = pd.DataFrame(to_do.todo)
        todo.to_csv("to_do.csv")
        break
