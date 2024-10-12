import string

def crypt(message):
    # Créez une chaîne de caractères avec toutes les lettres, les chiffres et les caractères spéciaux
    caracteres = string.ascii_letters + string.digits + " " + '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'  # Ajoutez les caractères de ponctuation ici
    result = ""
    
    for char in message:
        if char in caracteres:
            # Trouver l'index du caractère et prendre le suivant
            index = caracteres.index(char)
            next_char = caracteres[(index + 1) % len(caracteres)]  # On revient au début si on atteint la fin
            result += next_char
        else:
            result += char  # On garde les caractères non présents
    
    return result
