from rhyme_rus.utils import nn_usage


def test_select_none():
    assert [] == nn_usage.NnUsage.select("улисс")


def test_select_from_several_user(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "за'мок")
    assert "за'мок" == nn_usage.NnUsage.select("замок")


def test_select_from_several_items():
    assert "ко'рчи" == nn_usage.NnUsage.select("корчи")


def test_select_single():
    assert "до'м" == nn_usage.NnUsage.select("дом")


def test_accentuate(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "шукши'н")
    assert "шукши'н" == nn_usage.NnUsage.accentuate("шукшин")


def test_get_ipa_shortened():
    assert "batɨj" == str(nn_usage.NnUsage.get_ipa_shortened("kəstʊrˈbatɨj"))
