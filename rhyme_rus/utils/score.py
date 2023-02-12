import dill
from pathlib import Path
from rhyme_rus.utils.intipa import IpaDicts


class Score:
    def __init__(self, word_intipa, list_intipa):
        self.word_intipa: list[int] = word_intipa
        self.list_intipa: list[tuple[int]] = list_intipa
        self.all_vowels: tuple[int] = tuple()
        self.similarities: dict[int, dict[int, int]] = {}
        self.__get_similarities()
        self.__get_all_vowels()

    def __get_all_vowels(self):
        self.all_vowels: tuple[int] = IpaDicts().numbers_vowels

    def __get_similarities(self):
        # TODO similarities data is in seeds folder, not in data
        path = Path(__file__).parent.parent / "seeds/similarities_score.pkl"
        with open(path, "rb") as f:
            self.similarities: dict[int, dict[int, int]] = dill.load(f)

    def __get_rhyme_score(self, rhyme_intipa) -> tuple[int]:
        rhyme_score: list = []
        for _int_word, _int_rhyme in zip(self.word_intipa, rhyme_intipa):
            similarity: dict[int, int] = self.similarities[_int_word]
            try:
                score: int = similarity[_int_rhyme]
                rhyme_score.append(score)
            except KeyError:
                # no_sound in patterns = 0 in scores
                # no_sound occurs when a rhymed intipa does not have a previous consonant
                # like in words дом - ом
                if _int_rhyme == -1:
                    rhyme_score.append(0)
                else:
                    rhyme_score.append(3)
        rhyme_score: tuple[int] = tuple(rhyme_score)
        return rhyme_score

    def get_all_rhymes_scores(self) -> dict[tuple[int], list[tuple[int]]]:
        all_rhymes_scores: dict[tuple[int], list[tuple[int]]] = {}
        for rhyme_intipa in self.list_intipa:
            rhyme_score: tuple[int] = self.__get_rhyme_score(rhyme_intipa)
            if rhyme_score not in all_rhymes_scores:
                all_rhymes_scores[rhyme_score] = [rhyme_intipa]
            else:
                list_rhyme_intipa = all_rhymes_scores[rhyme_score]
                list_rhyme_intipa.append(rhyme_intipa)
                all_rhymes_scores[rhyme_score] = list_rhyme_intipa
        return all_rhymes_scores
