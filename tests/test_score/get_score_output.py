import dill
from rhyme_rus.utils.score import Score

index_stressed_v = 1
all_pattern_pads: dict[tuple[str, ...], list[tuple[int, ...]]] = \
    {
     ("voice",
      "same_stressed"
      ): [(0,0,0)]
    }

if __name__ == "__main__":
    all_score_patterns = Score(index_stressed_v, all_pattern_pads).get_all_score_patterns()
    # with open("test_score.pkl", "wb") as f:
    #     dill.dump(all_score_patterns, f)
    print(all_score_patterns)
