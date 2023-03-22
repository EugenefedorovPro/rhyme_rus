=========
rhyme_rus
=========

``rhyme_rus`` is the python package, which finds rhymes to a Russian word

* Version 0.0.2
* Date: 2023, March, 15
* Developer: Eugene Proskulikov
* License: MIT
* Contact: `LinkedIn <https://www.linkedin.com/in/eugene-proskulikov-168050a4/>`_
* Home: https://github.com/EugenefedorovPro/rhyme_rus

Installation
_________________


Linux (checked on Ubuntu 20.04.4)::

    $sudo apt install git-lfs


*rhyme_rus*  is available for installing only from GitHub

::

    pip install git+https://github.com/EugenefedorovPro/rhyme_rus.git


Critical dependencies 
_________________________

``rhyme_rus`` critically depends on:  

* `a special branch <https://github.com/EugenefedorovPro/ipapy_eugene/tree/forpython310>`_ of my fork of `ipapy <https://github.com/pettarin/ipapy>`_ module. On installation the branch is uploaded from GitHub to your virtual environment. ``ipapy`` is a Python module to work with International Phonetic Alphabet (IPA) strings
* `put_stress_rus <https://github.com/EugenefedorovPro/put_stress_rus>`_ - Python package to put stress on a Russian word powered by the trained neural network
* `word2ipa_rus <https://github.com/EugenefedorovPro/word2ipa_rus>`_ - Python package to convert a Russian word to IPA transcription powered by the trained neural network 



Quick start
_________________________________________

------------------------------------------
Input word available in `database` 
------------------------------------------

::

    from rhyme_rus.rhyme import rhyme

    rhyme(word)

*word* accepts a Russian word under some conditions:

- low case
- 'ё' sensitive
- no blank spaces, no dashes



Let's see how it works ::

    rhyme("кость")


Output:


+----+-------+-----------+---------------------------------------------------------------------------------+--------+
| id | score | assonance | pattern                                                                         | rhyme  | 
+====+=======+===========+=================================================================================+========+
| 0  |   1   |    0      | ('any_cons', 'same_stressed', 'same_cons', 'same_cons')                         | гость  |
+----+-------+-----------+---------------------------------------------------------------------------------+--------+
| 5  |   1   |    0      | ('no_init_cons', 'same_stressed', 'same_cons', 'same_cons')                     | ость   |
+----+-------+-----------+---------------------------------------------------------------------------------+--------+
| 14 |   4   |    1      | ('same_cons', 'same_stressed', 'same_cons', 'any_v')                            | покосе |
+----+-------+-----------+---------------------------------------------------------------------------------+--------+
| 359|   8   |    1      | ('same_cons', 'same_stressed', 'same_cons', 'add_sound', 'palat')               | косят  |
+----+-------+-----------+---------------------------------------------------------------------------------+--------+




Columns explained:

* **0**, **5**, **14**, **359** - numbers of rhymes up to 1074 for the current input
* **score** - from 0 to 55, indicating how far from the input word a rhyme is: the loser score, the closer rhyme. 
  Rhyme reveals audial likeness of words, when sequence of sounds matter
* **assonance** - from 0 to 2. Assonance/consonance shows to what extend 
  words have similar sounds irrespective of their position 
  The lower number, the more likely words will be percieved as close to each other
* **patterns** - patterns, the algorithm uses to select rhymed words
* **rhyme** - rhymes to an input word


The default output for one- or two-syllable words may be rather extended. 
As a result, you will get a full table with max rows and column width. 
However, you can reduce the output by configuring it with::


    pd.set_option('display.max_rows', 50)
    pd.set_option('display.min_rows', 50)
    pd.set_option('display.max_colwidth', 50)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', None)
    

You can download resulting dataframe to an external file::
 
    rhyme("кость").to_csv("dom.csv")


------------------------------------------
Input word unavailable in `database` 
------------------------------------------
If a word you provide as an input to `rhyme` is unavailable in the package's `database`, 
or if there are omographs, the program will try and stress the word by itself deploying `put_stress_rus`. 
The accuracy of the neural network, standing behind the package, is 0.7945. 
The code will raise exception, e.g.::

        rhyme_rus.utils.exceptions.MultipleStresses: 
        мандельштам has  stress variants for a user to choose from 
        ["манде'льштам", "ма'ндельштам", "мандельшта'м"]

To make code resume, you should restart the same function with the properly stressed word as an argument::

        rhyme(мандельштам, "мандельшта'м")


How does rhyme constructed?
__________
I founded `rhyme` on my understanding, why we hear some
pairs of words as harmonious, others as not, and why contemporary poetry does not use precise rhymes:

* I do not rhyme characters, I do rhyme sounds. That's why I use IPA transcription of Russian words

* stressed vowel is a key. No matter how far from the input word the rhymes is, 
  the stressed vowel should remain, suffering the slightest modifications, if any

* the sound before the stressed vowel should to be takes into account. 
  The rest of the previous sounds has to be neglected.

* one gets rhymes changing consonants to their palatalized, voiced or voiceless counterparts, 
  altering vowels to their close peers 

* substituting vowels and consonants of an input word for any other sounds proves fruitful

* one gets remoter rhymes by adding or removing sounds from the input word's pattern

* assonants/ consonants matter, and should be added to rhymes

* The whole algorithm is based on selecting a pool of words with the same stressed vowel, 
  and same (+-3) number of sounds after stressed vowel


Algorithm
_________

I want to find rhymes to word "дом". Let's have a look under the hood.


**1.** The code requests sqlite3 database and selects a pile of words, which satisfy the two conditions. They have:

* the same stressed vowel or `near stressed vowel`: 'a'-'æ' (а-я), 'o'-'ɵ'(о-ё) 
* +-3 sounds after stress: 'агроном' - same 1 sound after stress, 'удодом' - 3 sounds

**2.** The code yields `rhyme pattern` for every selected word:


*  **same_cons** = marks the same consonant on the same position in both words, e.g. "дом" - "ком": "м" with index 2

*  **same_stressed_v** = same stressed vowel on the same position as the vowel "о" with index 1

*  **near_stressed_v** = `inverted` stressed_vowel on the same position as о-ё in "дом" - "ёд"

*  **same_v** = same vowel in corresponding position as 'а' in words "кобра" - "вобла"

*  **voice** = either voiced or voiceless consonant in the same position

*  **any_cons** = any consonant in the same position

*  **any_v** = any vowel in the same position

*  **no_sound** = removed sound from the current position: "дом" - "дзюдо", 'м' - sound removed from the end: ('same_cons', 'same_stressed', 'no_sound')

*  **add_sound** = added sound to the current position: "дому" - "гнедому", 'у' is added: ('same_cons', 'same_stressed', 'same_cons', 'add_sound')







If we change the pattern to 
**("any_cons", "near_stressed_v", "same_cons)**, 
what rhymes will the algorythm find? Among others -
"битьём", "путём", "почём". Sounds standing behind
characters 'ть', 'т', 'ч' are encoded by "any_cons", meanwhile, 
'ё' is a "near_stressed_v" in relation to 'о',

Do you guess if `rhyme` will find the word 
'рог' with input 'рок' and pattern
**("same_cons", "same_stressed_v", "same_cons)**? Yes, it will, 
despite two different characters at the end 'г' vs 'к'. 
In Russian these letters represent the same sounds, so that you 
cannot differentiate them by ear. That's one of the 
most significant features of `rhyme_rus` algorythm. 
It finds correspondences not by comparing characters, 
but by comparing sounds using International Phonetic Alphabet (IPA).
The words 'рог' and 'рок' have the same 
pronunciation 'rok'.

What does `rhyme` briefly do to produce the result? The algorythm: 


*1.*
**chops a part of the word**, which plays role in rhyming. 
That is a\) stressed vowel, b) every sound after the stressed vowel, 
c) the consonant before the stressed vowel
 
* 'судьба' will be cut to 'ba'
* 'аорта' - 'ortə' \('a' is omitted) 
* 'дом' - 'dom'

In fact, all these chops of IPA sounds were preprocessed,
converted into integers, and stored in 'wiki_parsed.pkl'. So, the program just
fetches necessary data from permanent storage, uploaded in cache as a Class.

*2.*
**makes a sound schema of a chopped word** 

* 'dom' will correspond to *\['cons', 'stress_v', 'cons']*
* 'ortə' - *\['stress_v', 'cons', 'cons', 'vowel']*

*3.*
**produces all possible combinations** of different types of consonants and
vowels out of the scheme 

* Every element of the scheme can be decoded into different sound types:: 

    combinations = {  
                    "cons": ["same_cons", "voice_cons", "palatal_cons", "any_cons", "no_sound"],  
                    "stress_v": ["same_stressed_v", "near_stressed_v"],  
                    "vowel": ["same_v", "any_v", "no_sound"],  
                    }

* 'dom' scheme yields the following patterns among others: 
* * ('same_cons', 'same_stressed_v, 'same_stressed_v')
* * ('any_cons,'same_stressed_v', 'voice_cons')

*4.*
**adds 'no_sound' to all positions in all generated patterns**

* Fore example: ('cons', 'add_sound',' 'stress_v', 'cons'), ('cons', 'stress_v', 'cons', 'add_sound')

* As a result we have a lot of pattern combinations, the more sounds in a word, the greater number of variants
* 'dom' - **3** sounds, which yield **250** patterns
* 'ortə' - **4** sounds - **900** patterns
* 'общество' \('opɕːɪstvə') - **9** sounds and **562 500** patterns
* 'заведующая' \('vʲedʊjʉɕːɪjə') - **10** sounds and **6 075 000** patterns 
* 'выравнивание' \('vɨˈravnʲɪvənʲɪje') - **11** sounds and **32 906 250** patterns

Number of combinations grow dramatically with number of sounds in a word.
In ideal world I would prefer to deal with all possible patterns,
but in reality CPU and memory resources limited. That's why the rest of the
algorythm is focused on setting restrictions to this pleroma of variants.  

*5.*
**filters patterns, removing less productive ones**

* I will partially clarify this piece of the algorythm in the section "Arguments to `rhyme()`" 
 

**iterates customized wiki Dictionary to find all words, which fit
selected patterns**

* all words in wiki are stored as instances of Dictionary class
* to fasten the code, and reduce memory consumption I preprocessed all words (chopped and converted them to integers), used generators, hashed means of data storage (classes, dicts, sets), C-based solutions (itertools), lru_cache, and different algorithms to cope with long vs short words.


Arguments to `rhyme()`, `rhyme_only_words()`
__________________________________________________________

Both commands in the title to the section accepts the same args::

    rhyme_only_words(word,
                     max_length_pat_of_ipa = 6,
                     list_score_numbers=range(45, 55, 5),
                     max_number_hard_sounds_in_one_pat=1
                     )
    

* **word** accepts a russian words under some conditions:
  * available in inside parsed wiki dict with more than 400k items
  * low case
  * 'ё' sensitive
  * no blank spaces, no dashes

* **list_score_numbers** accepts list of integers from 0 to 100 with step 5.
  * 0 score corresponds to precise rhymes ('дом' - 'ведом')
  * 100 score corresponds to rhymes, which can hardly be associated with an input ('дом' - 'бредём')


* **max_length_pat_of_ipa** sets a number of sounds, which will be taken to generate all possible patterns

* * if max_length_pat_of_ipa is set to 6 \(default) the algorithm will generate patterns only for first 6 sounds, while remaining all other sounds in the tail of the word unchanged. It means, that, e.g. word 'беженец' \(bʲeʐɨnʲɪt͡s') will find rhymes, which will end on unchanged 7th sound \('ц'): 'соперни**ц**', 'столешни**ц**', etc.
* **max_number_hard_sounds_in_one_pat** defines number of 'hard_sounds' to be picked up in a pattern. "Hard_sounds" stands for CPU-consuming sounds, especially 'any_v', 'any_cons', 'add_sounds', but also 'palatal_cons', 'voice_cons'

* * if you set *max_number_hard_sounds_in_one_pat* to 1 \(default) no pattern has more than 1 sound of this type: ('any_cons', 'same_vowel', 'palatal_cons')
* * if you set arg to 2 the algorythm produces also patterns of this sort ('any_cons', 'same_vowel', 'palatal_cons', 'any_cons') - two 'any_cons' in a pattern


To make a trade-off between fast execution and extended output, 
three arguments to `rhyme()` are available. The following code reveals
the **default values**::

    word = "беженец"
    table_word_pat_score = rhyme(word,
                                 max_length_pat_of_ipa=6,
                                 list_score_numbers=range(0, 45, 5),
                                 max_number_hard_sounds_in_one_pat=1
                                 )
    print(table_word_pat_score)

It takes 18 seconds to find rhymes to the word *беженец* 
with 9 rows of the output in a table: 'беженец', 'приверженец',
'соперниц', 'грешниц', 'столешниц', 'бедренец', 'первенец', 'перельниц', 
'перечниц'.

You guess 18 secs too long to wait. Let's try and make it a bit faster, by
**setting list_score_numbers** from `range(0, 45, 5)` to `range(0, 35, 5)`:: 


    word = "беженец"
    table_word_pat_score = rhyme(word,
                                 max_length_pat_of_ipa=6,
                                 list_score_numbers=range(0, 35, 5),
                                 max_number_hard_sounds_in_one_pat=1
                                 )
    print(table_word_pat_score)
    

* Time of execution: 7.9 sec. Much faster, but with some cost.
* Number of rhymed words: 5. It means -3 words, with only 'беженец', 'приверженец', 'соперниц', 'грешниц', 'столешниц'.


It seems the output is too scarce. Let's shift our trade-off to results' side, 
by returning default to `list_score_numbers=range(0, 45, 5)` and
increasing **max_length_pat_of_ipa*`** from 6 to 7::

    word = "беженец"
    table_word_pat_score = rhyme(word,
                                 max_length_pat_of_ipa=7,
                                 list_score_numbers=range(0, 45, 5),
                                 max_number_hard_sounds_in_one_pat=1
                                 )
    print(table_word_pat_score)
   

* Time of execution: 45 sec.
* Number of rhymed words: 15. It means +6 rhymes to default output, with additional 'беженки', 'беженце', 'беженцы', 'беженца', 'убежище'.

The most unexpected rhymes you can achieve by changing the last parameter.
Let's check the output produced by **max_number_hard_sounds_in_one_pat** value
changed from 1 to 2 with other arguments set to default::


    word = "беженец"
    table_word_pat_score = rhyme(word,
                                 max_length_pat_of_ipa=7,
                                 list_score_numbers=range(0, 45, 5),
                                 max_number_hard_sounds_in_one_pat=2
                                 )
    print(table_word_pat_score)
    

* Time of execution: 49 sec.
* Number of rhymed words: 64. Much more than all default, but with many rhymes moving far from traditional patterns: 'ежели', 'нежити', 'тибетец', 'сеянец', 'подснежник', etc.


Utils to explore `rhyme()` output
__________________________________

You can explore the output table generated by `rhyme(word)`::

    from rhyme_rus.rhyme import rhyme
    from rhyme_rus.utils.explore_rhymes import ExploreRhymes
    word = "кот"
    table_word_pat_score = rhyme(word)
    
    # subtract output table by number of score, arg accepts int
    score_number = 5
    rhymes_by_score = ExploreRhymes.find_rhymes_by_score(score_number, table_word_pat_score)
    print(rhymes_by_score)
    
    # subtract output table by rhyme pattern, arg accepts tuple
    pattern = ('palatal_cons', 'near_stressed_v', 'same_cons')
    rhymes_by_pattern = ExploreRhymes.find_rhymes_by_pattern(pattern, table_word_pat_score)
    print(rhymes_by_pattern)
    
    # subtract output table by part of speech, arg accepts string
    # "noun","verb","adj","name","adv","num","pron"
    part_speech = "adv"
    rhymes_by_pos = ExploreRhymes.find_rhymes_by_pos(part_speech, table_word_pat_score)
    print(rhymes_by_pos)
    
    # subtract output table by word, arg accepts string
    word = "бот"
    rhymes_by_word = ExploreRhymes.find_rhymes_by_word(word, table_word_pat_score)
    print(rhymes_by_word)
  
    
    
