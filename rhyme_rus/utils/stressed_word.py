from rhyme_rus.utils.exceptions import MultipleStresses
def get_stressed_word(all_stresses, unstressed_word):
    if len(all_stresses) == 1:
        return all_stresses[0]
    else:
        raise MultipleStresses(unstressed_word, all_stresses)
