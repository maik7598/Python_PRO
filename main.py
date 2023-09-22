meme_dict = {
    'CRINGE': 'Pena Ajena',
    'LOL': 'Una respuesta común a algo gracioso',
    'ROFL':  'una respuesta a una broma',
    'SHEESH': 'Ligera desaprobación',
    'CREEPY': 'aterrador, siniestro',
    'AGGRO': 'ponerse agresivo/enojado'
}

word = input("Escribe una palabra que no entiendas(en Mayuscula): ")

if word in meme_dict.keys():
    #Que debemos hacer si se encuentra la palabra
    print("meme_dict[word]")

else:
    #Que hacer si no se encuentra la palabra
    print("Tu palabra no esta")
