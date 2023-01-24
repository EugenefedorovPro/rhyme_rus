from rhyme_rus.utils.fetch_stressed_word import (
    FetchStressFromDb,
    FetchStressFromNn,
    FactoryStress)

def test_fetch_stress_from_db():
    one_stressed_word = FetchStressFromDb.fetch_stress("быль")
    assert ["бы'ль"] == one_stressed_word


