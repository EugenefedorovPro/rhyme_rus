from rhyme_rus.utils import nn_usage


def test_accentuate(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "шукши'н")
    assert "шукши'н" == nn_usage.NnUsage.accentuate("шукшин")


def test_get_ipa_shortened():
    assert "batɨj" == str(nn_usage.NnUsage.get_ipa_shortened("kəstʊrˈbatɨj"))
