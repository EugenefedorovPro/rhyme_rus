from rhyme_rus.utils.pattern import Pattern
from rhyme_rus.utils.score import Score
from rhyme_rus.seeds.mysql_connect import MySql
import json
import dill

word_0 = "до'м"
word_1 = "ло'м"
word_2 = "лё'д"
list_words = [word_0, word_1, word_2]


def fetch_words(words: list[str]) -> list:
    my_sql = MySql()
    fetches = []
    for word in words:
        query = f'''select intipa from wiki_pickled where accent = "{word}"'''
        fetch = my_sql.cur_execute(query)
        fetches.append(fetch)
    return fetches


list_fetches = fetch_words(list_words)
print(list_fetches)


def depack_fetches(list_fetches):
    list_intipa = []
    for fetch in list_fetches:
        list_intipa.append(json.loads(fetch[0][0]))
    return list_intipa


list_intipa = depack_fetches(list_fetches)
print(list_intipa)

intipa_dom = list_intipa[0]
intipa_lom = list_intipa[1]
intipa_led = list_intipa[2]

pats = Pattern(intipa_dom, [intipa_lom, intipa_led]).get_all_pattern_pads()
print(pats)

path_pat = "../test_pattern/test_pattern.pkl"
with open(path_pat, "wb") as f:
    dill.dump(pats, f)

scores = Score(intipa_dom, [intipa_lom, intipa_led]).get_all_rhymes_scores()
print(scores)

path_score = "../test_score/test_score.pkl"
with open(path_score, "wb") as f:
    dill.dump(scores, f)
