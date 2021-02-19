def decrypt(text,step):
    result = ""

    for i in range (len(text)):
        char=text[i]
        if not char.islower():
            result += char
        elif char.isupper():
            result += chr((ord(char)+s-65)%26+65)
        else:
            result += chr((ord(char)+s-97)%26+97)
        return result
try:
    f=open(sys.argv[1], 'r')
    f1=open("message-dechiffre.txt", 'w')

    step=int(input("Entrez le nombre de décalage des lettres : "))
    text=f. ()
    f1. (encrypt(text, 26-step))
    f.close()
    f1.close()
    print("Le message chiffré est disponible sous le nom message-dechiffre.txt")

except Exception:
    print("Le fichier n'est pas existant.")
    
    
