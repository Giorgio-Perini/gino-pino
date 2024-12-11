registro = {
}
n = 0

print("1. Aggiungi studente")# fatto
print("2. Visualizza registro") # fatto
print("3. Modifica studente")
print("4. Rimuovi studente")
print("0. Esci") # fatto

while True:

    valore = int(input("inserisci qui valore: "))

    if valore == 0 :
        print("arrivederci")
        break
    elif valore == 1:
        n = n + 1 
        nome = input(f"stai per inserire il nome del {n}° studente: ")
        cognome = input("inserisci il suo cognome: ")
        media = int(input("inserisci media: "))
        registro[n] = {"nome" : nome, "cognome": cognome, "media": media}

    elif valore == 2:
        print(registro)
    elif valore == 3:
        print("che studente vuoi modificare ?")
        studente = int(input("inserisci indice"))
        print(registro[studente])
        print("che cosa vuoi modificare ?")
        valore = input("inserisci sono nome, cognome o media: ")
        if valore == nome:
            
        elif valore == cognome:

        elif valore == media:

        else:
            print("inserisci un valore valido")
    elif valore == 4:
        studente = int(input("che studente vuoi rimuovere:"))
        registro[studente]
        print("studente rimosso")
    else:
        print("inserisci un valore valido")
        print()
        print("1. Aggiungi studente")
        print("1. Aggiungi studente")
        print("2. Visualizza registro")
        print("3. Modifica studente")
        print("4. Rimuovi studente")
        print("0. Esci")
