import multiprocessing as mp
from time import perf_counter
import pandas as pd
from pathlib import Path
import sys
import rhyme_rus.rhyme as r

# sys.path.insert(0, Path.cwd())


def switch_child_process(
    connection, word_with_stress, list_score_numbers, max_length_pat_of_ipa
):
    print("child process in on")
    output = r.rhyme_to_table(
        word_with_stress=word_with_stress,
        list_score_numbers=list_score_numbers,
        max_length_pat_of_ipa=max_length_pat_of_ipa,
    )


def rhyme_with_multiprocess(word_with_stress, max_length_pat_of_ipa):
    start_time = perf_counter()

    child_list_score_numbers = [[0, 5, 10, 15],  [20, 25,  30], [35, 40]]
    parent_list_score_numbers = [[0, 5, 10, 15]]
    print("start of processing")
    for list_score_numbers in split_list_score_numbers:
            
        print("start of processing")
        con_get, con_send = mp.Pipe()
        p = mp.Process(
            target=switch_child_process,
            args=(
                (
                    con_send,
                    word_with_stress,
                    list_score_numbers,
                    max_length_pat_of_ipa,
                )
            ),
            daemon=True,
        )

        p.start()
    
        print("parent process in on")
        output_1 = r.rhyme_to_table(
            word_with_stress=word_with_stress,
            list_score_numbers=split_list_score_numbers[0],
            max_length_pat_of_ipa=max_length_pat_of_ipa,
        )

    output_2 = con_get.recv()
    
        output = pd.concat((output_1, output_2), axis=1)
    return time_elapsed, output


def assess_time_oneprocess(word_with_stress, max_length_pat_of_ipa):
    print("assessment of one process is on")
    start_time = perf_counter()
    output_one = r.rhyme_to_table(word_with_stress, max_length_pat_of_ipa)
    time_passed = perf_counter() - start_time
    return time_passed, output_one


if __name__ == "__main__":
    word_with_stress = "о'блачный"
    max_length_pat_of_ipa = 8
    time_mult, output_mult = rhyme_with_multiprocess(
        word_with_stress, max_length_pat_of_ipa
    )
    time_one, output_one = assess_time_oneprocess(
        word_with_stress, max_length_pat_of_ipa
    )

    print("time_mult", time_mult)
    print("time_out", time_one)
else:
    print("it's not the __main__")
