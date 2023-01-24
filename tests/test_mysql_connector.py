import mysql.connector

from rhyme_rus.seeds.mysql_connect import MySql
from unittest.mock import patch
import pytest

@pytest.mark.parametrize("test_input, expected", [("2+2", 4), ("5+3", 9)])
def test_check_param(test_input, expected):
    assert eval(test_input) == expected

@patch.object(MySql, "cur_execute", return_value = "до'м")
def test_mysql(mock_MySql_cur_execute):
    query_0 = "select accent from wiki_pickled where word = 'дом'"
    stressed_word = MySql.cur_execute(query_0)
    assert stressed_word == [("до'м",)]


def test_something():
    assert 1 == 1