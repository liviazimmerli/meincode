benutzername = input ("Benutzername eingeben")
#Das Programm überprüft den eingegebenen Benutzername.
if benutzername == ("livia"):
    #Wenn der Benutzername korrekt eigegeben wurde, wird nach dem Passwort gefragt.
    password= input("Passwort eingeben")
    #Wenn das Passwort korrekt eigegeben wurde, wird das Login genehmigt.
    if password == "gutentag":
        print ("Passwort genehmigt")
        #Wenn das Passwort falsch war, hat man weitere Versuche um sich einzuloggen.
    else: 
        print ("passwort falsch")
# Wenn der Benutzername schon falsch eingegeben wird, läuft das Programm nicht weiter.
else:
    print("Benutzername falsch")


