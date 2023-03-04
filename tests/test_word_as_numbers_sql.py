import json
import pytest
from rhyme_rus.seeds.mysql_connect import MySql
from rhyme_rus.seeds.ipa_dicts import IpaDicts


uni_string_0 = "ɐˈprʲelʲ"
uni_string_1 = "jɪrɐˈvoj"
uni_string_2 = "sjɪˈdobnɨj"
list_uni = [uni_string_0, uni_string_1, uni_string_2]

def list_uni_to_numbers(list_uni):
    numbers = []
    for uni in list_uni:
        numbers.append(IpaDicts().unistring_to_numbers(uni))
    return numbers

expected_numbers = list_uni_to_numbers(list_uni)

@pytest.mark.parametrize("uni_string, expected_number", [(list_uni[0], expected_numbers[0]),
                                                           (list_uni[1], expected_numbers[1]),
                                                           (list_uni[2], expected_numbers[2])])
def test_word_as_numbers_sql(uni_string, expected_number):
    query = f"select word_as_numbers from wiki_pickled where sounds = '{uni_string}'"
    received_number = MySql().cur_execute(query)
    received_number = json.loads(received_number[0][0])
    assert expected_number == received_number
