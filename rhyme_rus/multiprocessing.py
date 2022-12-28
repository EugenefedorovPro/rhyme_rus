from multiprocess import Process, Pipe
from rhyme_rus.rhyme import rhyme_to_table
import time
import pandas as pd


def rhyme_by_another_processor(connection, word_with_stress, list_score_numbers):
    print("child process in on")
    output = rhyme_to_table(
        word_with_stress=word_with_stress, list_score_numbers=list_score_numbers
    )
    return connection.send(output)


def rhyme_with_multiprocess(word_with_stress):
    start_time = time.perf_counter()

    split_list_score_numbers = [[0, 5, 10, 15, 20], [25, 30, 35, 40]]

    print("start of processing")
    con_get, con_send = Pipe()
    p = Process(
        target=rhyme_by_another_processor,
        args=((con_send, word_with_stress, split_list_score_numbers[1])),
        daemon=True,
    )

    p.start()

    print("parent process in on")
    output_1 = rhyme_to_table(
        word_with_stress=word_with_stress,
        list_score_numbers=split_list_score_numbers[0],
    )

    output_2 = con_get.recv()

    output = pd.concat((output_1, output_2), axis=1)
    time_elapsed = time.perf_counter() - start_time
    return time_elapsed, output
