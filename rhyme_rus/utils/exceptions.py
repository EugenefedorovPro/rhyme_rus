class MultipleStresses(Exception):

    def __init__(self, unstressed_word, all_stresses):
        self.unstressed_word = unstressed_word
        self.all_stresses = all_stresses

    def __str__(self):
        return f"{self.unstressed_word} has  stress variants for a user to choose from {self.all_stresses}"
