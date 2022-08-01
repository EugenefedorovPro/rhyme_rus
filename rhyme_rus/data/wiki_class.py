from functools import lru_cache
import dill
from pathlib import Path


class Dictionary:
    instances = []

    def __init__(self, word, pos, forms, senses, sounds, status, word_lowcase, stem,
                 grammeme, meanings, accent, ipa, npipa, intipa):
        self.instances.append(self)
        self.word = word
        self.word_lowcase = word_lowcase
        self.stem = stem
        self.pos = pos
        self.grammeme = grammeme
        self.forms = forms
        self.senses = senses
        self.meanings = meanings
        self.accent = accent
        self.sounds = sounds
        self.status = status
        self.ipa = ipa
        self.npipa = npipa
        self.intipa = intipa

    @classmethod
    def get_word_from_Dict(cls, word):
        dict_items_for_word = [item for item in cls.instances if item.word == word]
        return dict_items_for_word

    @classmethod
    def get_number_of_instances(cls):
        number_of_instances = len(cls.instances)
        return number_of_instances


@lru_cache
def unpack_wiki_parsed(path):
    with open(path, "rb") as f:
        instances = dill.load(f)
    print("Wiki Dictionary loaded")
    return instances


path_wiki = Path(__file__).parent / "wiki_parsed.pkl"
Dictionary.instances = unpack_wiki_parsed(path_wiki)
