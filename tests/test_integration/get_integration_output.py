import dill
from rhyme_rus.utils.word import Word
from rhyme_rus.utils.procedure import Procedure

target_words = ['ом', 'дом', 'кома', 'палама', 'сыл']
words_names = ['om', 'dom', 'koma', 'palama', 'syl']


def dump_tables(words, names):
    for w, name in zip(words, names):
        word = Word(w)
        if w == 'палама':
            word = Word("пала'ма")
        word = Procedure(word).build()
        with open(f"{name}.pkl", "wb") as f:
            dill.dump(word.table, f)
            print(f"{name}.pkl was written")


if __name__ == "__main__":
    dump_tables(target_words, words_names)
