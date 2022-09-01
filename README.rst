=========
rhyme_rus
=========

``rhyme_rus`` is the python package, which finds rhymes to a Russian word

* Version 0.0.1
* Date: 2022, July, 31
* Developer: Eugene Proskulikov
* License: MIT
* Contact: `LinkedIn <https://www.linkedin.com/in/eugene-proskulikov-168050a4/>`_
* Home: https://github.com/EugenefedorovPro/rhyme_rus

Installation
_________________

*rhyme_rus* package incules `wiktionary_rus` dependency with a large data file, which is managed by `Git Large File Storage (LFS) <https://git-lfs.github.com/>`_. To upload it properly to Linux machines you should have LFS installed on your PC.

Linux (checked on Ubuntu 20.04.4)::

    $sudo apt install git-lfs


*rhyme_rus*  is available for installing only from GitHub

::

    pip install git+https://github.com/EugenefedorovPro/rhyme_rus.git


Critical dependencies 
_________________________

``rhyme_rus`` critically depends on: 

* `a special branch <https://github.com/EugenefedorovPro/ipapy_eugene/tree/forpython310>`_ of my fork of `ipapy <https://github.com/pettarin/ipapy>`_ module. On installation the branch is uploaded from GitHub to your virtual environment. ``ipapy`` is a Python module to work with International Phonetic Alphabet (IPA) strings
* `wiktionary_rus <https://github.com/EugenefedorovPro/wiktionary_rus>`_ - Russian wiktionary preprocessed for neural networks: word, lowcase, accent, stem, part of speech, meanings, unicode transcription
* `put_stress_rus <https://github.com/EugenefedorovPro/put_stress_rus>`_ - Python package to put stress on a russian word powered by the trained neural network
* `word2ipa_rus <https://github.com/EugenefedorovPro/word2ipa_rus>`_ - Python package to convert a russian word to IPA transcription powered by the trained neural network 



Quick start
_________________________________________

------------------------------------------
Input word available in `wiktionary_rus` 
------------------------------------------

::

    from rhyme_rus.rhyme import rhyme, rhyme_only_words

`rhyme_rus` processes the whole inbuilt `wiktionary_rus` with every fresh input word. It does not pick up preselected rhymes from the database. As a consequence `rhyme_rus` works faster or slower, depending on the number of syllables after the stressed vowel an input word has. The algorythm provides a set of arguments for you to trade-off between speed and number of rhymes in the output::

    rhyme(word)

*word* accepts a russian word under some conditions:

- low case
- 'ё' sensitive
- no blank spaces, no dashes


to get a string of rhymed words to your input word

::

    rhyme_only_words("палка")
  
    
Output:: 
    
    'палка, перепалка, шлангбалка, балка, рыбалка, валка...'

to get a table of rhymed words::

    rhyme("дом")


Output:


+----+--------+-------------------------------------------------+-----------+-----+
|    |rhyme   |pattern                                          |part_speech|score|
+====+========+=================================================+===========+=====+
|0   | дроздом|(same_cons, same_stressed_v, same_cons)          |noun       |0    |
+----+--------+-------------------------------------------------+-----------+-----+
|... |...     |...                                              | ...       |...  |
+----+--------+-------------------------------------------------+-----------+-----+
|114 |пешком  |('any_cons', 'same_stressed_v', 'same_cons')     |     adv   |15   |
+----+--------+-------------------------------------------------+-----------+-----+
| ...|...     |...                                              |...        |...  |
+----+--------+-------------------------------------------------+-----------+-----+
|3062|ромб    |(any_cons, same_stressed_v, same_cons, add_sound)|    noun   |40   |
+----+--------+-------------------------------------------------+-----------+-----+

Columns explained:

* **0**, **114**, **3062** - numbers of rhymes up to 3126 for the current input
* **rhyme** - rhymes to an input word
* **patterns** - patterns, the algorythm uses to select rhymed words
* **part_speech** - part of speech of a rhyme: "noun", "verb", "adj", "name", "adv", "num", "pron"
* **score** - from 0 to 100, indicating how far from the input word a rhyme is: the higher score, the worse rhyme


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
 
    rhyme("дом").to_excel("dom.xlsx")

You will enjoy more comfort with  Jupyter, JupyterLab or Colab



------------------------------------------
Input word unavailable in `wiktionary_rus` 
------------------------------------------
If a word you provide as an input to `rhyme` or `rhyme_only_words` is unavailable in `wiktionary_rus`, or if there are omographs, the program will try and stress the word by itself deploying `put_stress_rus`. The accuracy of the neural network, standing behind the package, is 0.7945. To check if the word is properly accentuated, you will be asked to print "Y" or press Enter, if correct, or print the stressed word, if not

Omographs:: 
    
    rhyme("замок")
    print(rhyme_only_words("замок"))

:: 

    > Wiktionary has 2 omographs: замо'к, за'мок. Print the stressed word you choose -

Word unavailable in `wiktionary_rus`::

    rhyme("коцюбинский")
    print(rhyme_only_words("коцюбинский"))

:: 

    > Neural Netword stressed коцюбинский as коцюби'нский. Print 'Y' if the stress is put correctly, or print word with a proper accent -



Algorythm
__________
I founded `rhyme_rus` on my understanding, why we hear some
pairs of words as harmonious, other as not, and why contemporary poetry does not use precise rhymes:

* I do not rhyme characters, I do rhyme sounds. That's why I use specifically parsed wiktionary as the only available source enjoying Russian words with IPA transcription

* stressed vowel is a key. No matter how far from the input word the rhymes is, the stressed vowel should remain suffering the slightest modifications

* the sound before the stressed vowel has to be takes into account. The rest of the previous sounds has to be neglected.

* one gets close rhymes changing consonants to their palatalized, voiced or voiceless counterparts, altering vowels to their close peers 

* substituting vowels and consonants of an input word for any other sounds proves fruitful

* one gets remoter rhymes by adding or removing sounds from the input word's pattern

* The whole algorythm is based on generating reasonable number of sounds' changes, mutations, removals or additions


Say, we have a pair "дом - судом". It is a precise rhyme, which 
I encode with the next pattern: 
*("same_cons", "same_stressed_v", "same_cons)*. Actually,
the pattern is a command for a script to find all words 
from wiki Dictionary, which complies with this pattern. 
Surely, the *("same_cons", "same_stressed_v", "same_cons)* 
suits "дроз **дом**", кон **дом**, тру **дом**, etc.

- **same_cons** = find a word from wiki dictionary with the same consonant on the same position  
- **same_stressed_v** = same stressed vowel
- **near_stressed_v** = find a word with a vowel close to the original one: e.g. "о" is a near stressed vowel to "ё", "ю" - "у", etc.  
- **same_v** = same vowel
- **voice_cons** = either voiced or voiceless consonant 
- **any_cons** = any consonant 
- **any_v** = any vowel
- **no_sound** = remove sound from the current position 
- **add_sound** = add sound (any consonant + any vowel) to the current position  

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
  
    
    