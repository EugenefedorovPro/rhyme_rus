from wiktionary_rus.wiktionary import wiki_instances, find_item_from_wiki


def test_unpack_wiki_parsed():
    print("inside_test_unpack_wiki_parsed")
    assert 422821 == len(wiki_instances)
    assert "dom" == find_item_from_wiki("до'м")[0].sounds
