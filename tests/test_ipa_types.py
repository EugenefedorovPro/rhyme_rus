from rhyme_rus.utils.ipa_types import *
import json


def test_get_voice_cons():
    with open("tests/test_ipa_types/get_voic_cons.json", "r") as f:
        voice_cons = json.load(f)
    assert voice_cons == str(IpaTypes.get_voice_cons())


def test_get_palatal_cons():
    with open("tests/test_ipa_types/get_palat_cons.txt", "r") as f:
        palatal_cons = f.read()
    assert palatal_cons == str(IpaTypes.get_palatal_cons())


def test_get_near_stressed_v():
    with open("tests/test_ipa_types/get_near_stressed_v.txt", "r") as f:
        near_stressed_v = f.read()
    assert near_stressed_v == str(IpaTypes.get_near_stressed_v())


def test_make_voice_cons_to_n():
    with open("tests/test_ipa_types/IpaTypes.make_voice_cons_to_n().txt", "r") as f:
        voice_cons_to_n = f.read()
    assert voice_cons_to_n == str(IpaTypes.make_voice_cons_to_n())


def test_make_palatal_cons_to_n():
    with open("tests/test_ipa_types/IpaTypes.make_palatal_cons_to_n().txt", "r") as f:
        palatal_cons_to_n = f.read()
    assert palatal_cons_to_n == str(IpaTypes.make_palatal_cons_to_n())


def test_make_near_stressed_v_to_n():
    with open("tests/test_ipa_types/IpaTypes.make_near_stressed_v_to_n().txt", "r") as f:
        near_stressed_v_to_n = f.read()
    assert near_stressed_v_to_n == str(IpaTypes.make_near_stressed_v_to_n())


def test_generate_all_cons_n():
    with open("tests/test_ipa_types/IpaTypes.generate_all_cons_n().txt", "r") as f:
        all_cons_n = f.read()
    assert all_cons_n == str(IpaTypes.generate_all_cons_n())


def test_generate_all_vowels_n():
    with open("tests/test_ipa_types/IpaTypes.generate_all_vowels_n().txt", "r") as f:
        all_vowels_n = f.read()
    assert all_vowels_n == str(IpaTypes.generate_all_vowels_n())
