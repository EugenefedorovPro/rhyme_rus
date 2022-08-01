from rhyme_rus.data.wiki_class import Dictionary


def test_unpack_wiki_parsed():
    print("inside_test_unpack_wiki_parsed")
    assert 422821 == Dictionary.get_number_of_instances()
    assert "dom" == Dictionary.get_word_from_Dict('дом')[0].sounds
