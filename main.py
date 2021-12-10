import random

participantes = [
    "Beatriz Lopes",
    "Brenda Noronha",
    "Bruno Gomes",
    "Edson Neto",
    "Eduardo Lima",
    "Erik Andersen (opcional)",
    "Fabio Zanelato",
    "Gabrielle Macedo",
    "Jean Silveira",
    "Rachel Rehlinger",
    "Rafael Palomino",
    "Samuel Francisco",
    "Silvio Gomes",
    "Tainá Gusmão",
    "Thais Bianchini",
    "Wellington Ferreira"
]

random.shuffle(participantes)

for idx, val in enumerate(participantes):
    print(idx+1, "-",val)