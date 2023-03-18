import pandas as pd
from rhyme_rus.utils.word_statistics import WordStatistics

pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)
pd.set_option("display.max_colwidth", None)

time_table = WordStatistics().measure_time_all_rhymes(seed = False, cycles = 5)
time_table.to_csv("time_table_random.csv")
print(time_table)
