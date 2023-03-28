import dill
from rhyme_rus.rhyme import rhyme, rhyme_with_stresses

target_words = ['ом', 'дом', 'кома', 'палама', 'сыл']
words_names = ['om', 'dom', 'koma', 'palama', 'syl']
words_names_stresses = ['om_stresses', 'dom_stresses', 'koma_stresses', 'palama_stresses', 'syl_stresses']


def get_integrated_mult():
    for word, name in zip(target_words, words_names):
        if word == 'палама':
            table = rhyme("пала'ма")
        else:
            table = rhyme(word)
        with open(f"{name}.pkl", "wb") as f:
            dill.dump(table, f)
            print(f"{name}.pkl was written")


def get_integrated_mult_stresses():
    for word, name in zip(target_words, words_names_stresses):
        if word == 'палама':
            table_all_stressed = rhyme_with_stresses("пала'ма")
        else:
            table_all_stressed = rhyme_with_stresses(word)
        with open(f"{name}.pkl", "wb") as f:
            dill.dump(table_all_stressed, f)
            print(f"{name}.pkl was written")


get_integrated_mult()

get_integrated_mult_stresses()
