class To_do:
  def __init__(self, todo=[]):
    self.todo = todo
    self.quit_program = ""

    ######## CODE ########

todo = To_do()

while todo.quit_program != "oui":

    ####### CODE #####

    if todo.quit_program == "oui":
    ###### CODE #####
       import pandas as pd

       if str(input("Voulez-vous ecrire votre TO-DO dans un fichier csv ? ")) == "yes" or str(input("Voulez-vous ecrire votre TO-DO dans un fichier csv ? ")) == "oui" :
           (todo.to_csv('to_do.csv', sep = '\t')

        break
