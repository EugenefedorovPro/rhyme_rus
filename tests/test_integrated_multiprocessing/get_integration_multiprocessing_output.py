import dill
from rhyme_rus.rhyme import rhyme

target_words = ['ом', 'дом', 'кома', 'палама', 'сыл']
words_names = ['om', 'dom', 'koma', 'palama', 'syl']


def get_integrated_mult():
    for word, name in zip(target_words, words_names):
        if word == 'палама':
            table = rhyme(word, "пала'ма")
        else:
            table = rhyme(word)
        with open(f"{name}.pkl", "wb") as f:
            dill.dump(table, f)
            print(f"{name}.pkl was written")


get_integrated_mult()
