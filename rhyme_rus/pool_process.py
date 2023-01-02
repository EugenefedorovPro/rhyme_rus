from multiprocess.pool import Pool
import pandas as pd
from rhyme_rus.rhyme import rhyme_to_table


def task(word_with_stress, max_length_pat_of_ipa, list_score_numbers):
    print(f"cild on with {list_score_numbers} scores")
    child_output = rhyme_to_table(
        word_with_stress, max_length_pat_of_ipa, list_score_numbers
    )
    print(f"cild off with {list_score_numbers} scores")
    return child_output


def rhyme_multiprocess(word_with_stress):
    if __name__ == "rhyme_rus.pool_process":
        list_list_score_numbers = [[0, 5, 10, 15, 20, 25, 30], [35], [40]]
        max_length_pat_of_ipa = 18
        items = [
            (word_with_stress, max_length_pat_of_ipa, item)
            for item in list_list_score_numbers
        ]
        with Pool() as pool:
            results = pool.starmap_async(task, items, chunksize=1)

            list_results = []
            for result in results.get():
                list_results.append(result)
            output = pd.concat(list_results, ignore_index=True, axis=0)
            return output
    else:
        print("error in __name__ = ", __name__)
