class Word:
    def __init__(self,
                 input_word: str,
                 variants_stressed_word: tuple = (),
                 stressed_word: int = ""
    ):
        self.input_word = input_word
        self.variants_stressed_word = variants_stressed_word
        self.stressed_word = stressed_word



