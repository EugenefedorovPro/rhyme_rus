from rhyme_rus.utils.exceptions import MultipleStresses


def get_stressed_word(all_stresses, unstressed_word, stressed_word):
    if stressed_word:
        return stressed_word
    elif len(all_stresses) == 1:
        return all_stresses[0]
    else:
        raise MultipleStresses(unstressed_word, all_stresses)
