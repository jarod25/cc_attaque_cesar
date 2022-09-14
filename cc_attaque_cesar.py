def decrypt(text,step):
    result = ""

    for i in range (len(text)):
        char=text[i]
        if not char.isalpha():
            result += char
        elif char.isupper():
            result += chr((ord(char)+step-65)%26+65)
        else:
            result += chr((ord(char)+step-97)%26+97)
    return result
try:
    f=open("/home/jarod/Documents/Cours/S3/Crypto/message-chiffre.txt", 'r')
    f1=open("/home/jarod/Documents/Cours/S3/Crypto/message-dechiffre.txt", 'w')

    step=int(input("Entrez le nombre de décalage des lettres : "))
    text=f.read()
    f1.write(decrypt(text, 26-step))
    f.close()
    f1.close()
    print("Le message chiffré est disponible sous le nom message-dechiffre.txt")

except Exception as e:
    print("Le fichier n'est pas existant.", e)
