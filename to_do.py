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
            try:
                self.todo[l-1] = v
            raise:
                print("ce n'est pas un numéro d'item valide")
            self.write()


    ######## CODE ########


todo = To_do()

while todo.quit_program != "oui":

    ####### CODE #####

    if todo.quit_program == "oui":
    ###### CODE #####

        break
