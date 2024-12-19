
import string

stats = {}

# normalization
with open("song.txt", "r", encoding="utf8") as f:

    for line in f:
        line = line.casefold().strip()

        for punc in string.punctuation:
            line = line.replace(punc, " ")
        
        # processing
        words = line.split()

        for word in words:
            if word in stats:
                stats[word] += 1
            else:
                stats[word] = 1

# display
def obtenir_critere_de_tri(paire_cle_valeur):
    return paire_cle_valeur[1] # trier sur la valeur et non la clé


sorted_words = sorted(stats.items(), key=obtenir_critere_de_tri, reverse=True)

for word, score in sorted_words[:5]:
    print(word, ":", score)