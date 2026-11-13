meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "BRO": "Una manera de llamar a tu amigo",
            }
word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

if word in meme_dict.keys():
    print (word,": ",meme_dict[word])
    # ¿Qué debemos hacer si se encuentra la palabra?
else:
    print ("nose a encontrado la plabra en clave")
    # ¿Qué hacer si no se encuentra la palabra
