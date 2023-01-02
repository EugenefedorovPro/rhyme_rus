word_with_stress = "пушкин"
list_list_score_numbers = [[0, 5, 10, 15, 20, 25, 30], [35], [40]]
max_length_pat_of_ipa = 18
items = [
    (word_with_stress, max_length_pat_of_ipa, item) for item in list_list_score_numbers
]


def init_worker(data):
    global shared_data
    shared_data = data 
    print("init_worker is issued ____________", shared_data)

def measure_obj_size():
    import sys
    
    total_obj_size_loc = sum([sys.getsizeof(item) for item 
        in locals().keys()]) 
    total_obj_size_glob= sum([sys.getsizeof(item) for item 
        in globals().keys()]) 
    
    total_obj_size = total_obj_size_loc + total_obj_size_glob
    print("total_obj_size", total_obj_size)
    for obj_l in locals().keys():
        print("local ", obj_l, "=", sys.getsizeof(obj_l))
    for obj_g in globals().keys():
        print("global ", obj_g, "=", sys.getsizeof(obj_g))


def measure_ram():
    import psutil

    vms_ram = psutil.Process().memory_info().vms / 1_000_000
    vms_ram = round(vms_ram, 0)
    return vms_ram


def task(word_with_stress, max_length_pat_of_ipa, list_score_numbers):
    from time import perf_counter
    import pandas as pd
    from rhyme_rus.rhyme import rhyme_to_table

    time_start = perf_counter()
    print("child on: ", list_score_numbers)

    child_output = rhyme_to_table(
        word_with_stress, max_length_pat_of_ipa, list_score_numbers
    )
    measure_obj_size()
    child_time_passed = round((perf_counter() - time_start) / 60, 2)
    print(f"cild off with {list_score_numbers} scores and {child_time_passed} time")
    print("child_vms", measure_ram())
    return child_output


def assess_time_oneprocess(word_with_stress, max_length_pat_of_ipa):
    from time import perf_counter
    import pandas as pd
    from rhyme_rus.rhyme import rhyme_to_table
    
    print("assessment of one process is on")
    start_time = perf_counter()
    output_one = rhyme_to_table(word_with_stress, max_length_pat_of_ipa)
    time_one = round((perf_counter() - start_time) / 60, 2)
    return time_one, output_one


if __name__ == "__main__":
    from multiprocess.pool import Pool
    from time import perf_counter
    import pandas as pd
    
    data = "eugene"

    time_start = perf_counter()
    with Pool(initializer = init_worker, initargs=((data),)) as pool:
        results = pool.starmap_async(
                task, 
                items,
                chunksize=1)

        list_results = []
        for result in results.get():
            list_results.append(result)

        output = pd.concat(list_results, axis=1)
        all_child_time_passed = round((perf_counter() - time_start) / 60, 2)

        print("length", len(output))
        # print(output["rhymes"])
        print("all_child_time_passed", all_child_time_passed)

        print("___________")
        print("assess_time_oneprocess on")

        time_one, output_one = assess_time_oneprocess(
            word_with_stress, max_length_pat_of_ipa
        )
        print("time_one", time_one)
        print("parent_vms", measure_ram())
