import dill
import pytest
from rhyme_rus.utils.score import Score

def test_score_all():
    index_stressed_v = 1
    all_pattern_pads: dict[tuple[str, ...], list[tuple[int, ...]]] = \
        {
            ("same_stressed",
             "same_v",
             "same_cons",
             "near_stressed",
             "near_v",
             "add_init_cons",
             "no_init_cons",
             "prolong",
             "voice",
             "voice_prolong",
             "palat",
             "any_cons",
             "any_v",
             "add_sound",
             "no_sound"
             ): [(0, 0, 0)]
        }
    actual_all_score_patterns = Score(index_stressed_v, all_pattern_pads).get_all_score_patterns()
    with open("test_score/test_score.pkl", "rb") as f:
        expected_all_score_patterns = dill.load(f)
    assert actual_all_score_patterns == expected_all_score_patterns

@pytest.mark.parametrize("index_stressed_v, all_pattern_pads, expected_all_score_patterns",[
    (1,
     {
         ("voice",
          "same_stressed"
          ): [(0, 0, 0)]
     },
     {(1, 0): [('voice', 'same_stressed')]}
     ),
    (1,
     {
         ("voice_prolong",
          "same_stressed"
          ): [(0, 0, 0)]
     },
     {(1, 0): [('voice_prolong', 'same_stressed')]}
     ),
    (1,
     {
         ("palat",
          "same_stressed"
          ): [(0, 0, 0)]
     },
     {(1, 0): [('palat', 'same_stressed')]}
     ),
    (1,
     {
         ("any_cons",
          "same_stressed"
          ): [(0, 0, 0)]
     },
     {(1, 0): [('any_cons', 'same_stressed')]}
     )

]
                         )
def test_score_initial(index_stressed_v, all_pattern_pads, expected_all_score_patterns):
    index_stressed_v = 1
    actual_all_score_patterns = Score(index_stressed_v, all_pattern_pads).get_all_score_patterns()
    assert actual_all_score_patterns == expected_all_score_patterns


