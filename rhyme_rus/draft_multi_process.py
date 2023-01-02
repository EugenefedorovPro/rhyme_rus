import sys
from pathlib import Path

# sys.path.insert(0, Path.cwd())
import multiprocess as mp
from time import perf_counter
import pandas as pd
import rhyme_rus.rhyme as r


def switch_child_process(
    connection, word_with_stress, list_score_numbers, max_length_pat_of_ipa
):
    print("child process in on")
    output = r.rhyme_to_table(
        word_with_stress=word_with_stress,
        list_score_numbers=list_score_numbers,
        max_length_pat_of_ipa=max_length_pat_of_ipa,
    )
    return connection.send(output)


def rhyme_with_multiprocess(word_with_stress, max_length_pat_of_ipa):
    start_time = perf_counter()

    child_list_score_numbers = [[0, 5, 10], [15, 20], [25, 30], [35, 40]]
    # parent_list_score_numbers = [[0, 5, 10, 15]]

    list_con_get = []
    for list_score_numbers in child_list_score_numbers:

        con_get, con_send = mp.Pipe()
        list_con_get.append(con_get)
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
            daemon=None,
        )

        p.start()

    list_outputs = []
    for c_get in list_con_get:
        try:
            _output = c_get.recv()
            list_outputs.append(_output)
        except EOFError:
            break
    output_2 = pd.concat(list_outputs, axis=1)

    # print("parent process in on")
    # output_1 = r.rhyme_to_table(
    # word_with_stress = word_with_stress,
    # list_score_numbers = parent_list_score_numbers,
    # max_length_pat_of_ipa = max_length_pat_of_ipa,
    # )

    # output = pd.concat((output_1, output_2), axis=1)
    time_mult = perf_counter() - start_time
    return time_mult, output_2


def assess_time_oneprocess(word_with_stress, max_length_pat_of_ipa):
    print("assessment of one process is on")
    start_time = perf_counter()
    output_one = r.rhyme_to_table(word_with_stress, max_length_pat_of_ipa)
    time_one = perf_counter() - start_time
    return time_one, output_one


print("__________", __name__)
if __name__ == "__main__":
    word_with_stress = "пра'зднество"
    max_length_pat_of_ipa = 18
    time_mult, output_mult = rhyme_with_multiprocess(
        word_with_stress, max_length_pat_of_ipa
    )
    time_one, output_one = assess_time_oneprocess(
        word_with_stress, max_length_pat_of_ipa
    )
    print(output_mult)
    print("time_mult", time_mult)
    print("time_one", time_one)
else:
    print("it's not the __main__")
