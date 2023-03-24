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

First install `git-lfs`

**Linux** (checked on Ubuntu 20.04.4)::

    $sudo apt install git-lfs

**Windows**: see `How to install Large File Storage <https://docs.github.com/en/repositories/working-with-files/managing-large-files/installing-git-large-file-storage?platform=windows>`_

*rhyme_rus*  is available for installing only from GitHub

Package is available only from GitHub:

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


+----+--------+-------+-----------+-------------------------------------------------------------------+
| id | rhyme  | score | assonance | pattern                                                           | 
+====+========+=======+===========+===================================================================+
| 0  | гость  |   1   |    0      | ('any_cons', 'same_stressed', 'same_cons', 'same_cons')           |
+----+--------+-------+-----------+-------------------------------------------------------------------+
| 5  | ость   |   1   |    0      | ('no_init_cons', 'same_stressed', 'same_cons', 'same_cons')       |
+----+--------+-------+-----------+-------------------------------------------------------------------+
| 14 | покосе |   4   |    1      | ('same_cons', 'same_stressed', 'same_cons', 'any_v')              |
+----+--------+-------+-----------+-------------------------------------------------------------------+
| 359| косят  |   8   |    1      | ('same_cons', 'same_stressed', 'same_cons', 'add_sound', 'palat') |
+----+--------+-------+-----------+-------------------------------------------------------------------+




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
                write input word with proper stressed_vowel like
                rhyme("за'мок")

To make code resume, you should restart the same function with the properly stressed word as an argument::

        rhyme("мандельшта'м")


How is rhyme constructed?
_________________________

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

 | Actually it picks up words as list of integers including the stressed vowel, the sound before it, if available, and all sounds after the stressed one: "дом" is represented as [6, 34, 26], while "стол" [47, 34, 24] (the first sound is not encoded as irrelevant for rhyming). 

**2.** The code compares the input word with its rhymes one by one, producing a series of possible rhyme patterns. For instance, in the rhyme 'кора' (stress on the first vowel) to the input word 'кобра', one sound is obviously removed. But the algorithm does not know exactly what sound to get rid of, and yields all possible variants, in this case just two ones: "кобр" ('a' removed) and "кора" ('б' removed). It should be noted that all operations are made on integer representations of words, and here we deal with string for the sake of simplicity.

**3.** The code has to select a proper pattern from a range of variants. To sort it out, the algorithm scores every sound presentation of the pattern against the corresponding sounds of the input word. The lower score is, the more properly pattern reflects rhyme relations. Say, "кора" scores less points than "кобр" as it fits perfectly with the compared rhyme "кора". 

**4.** The code converts selected integer presentations of rhyme patterns to strings according to following rules:


*  **same_cons** = marks the same consonant on the same position in both words, e.g. "дом" - "ком": "м" with index 2

*  **same_stressed_v** = same stressed vowel on the same position as the vowel "о" with index 1

*  **near_stressed_v** = `inverted` stressed_vowel on the same position as о-ё in "дом" - "ёд"

*  **same_v** = same vowel in corresponding position as 'а' in words "кобра" - "вобла"

*  **voice** = either voiced or voiceless consonant in the same position

*  **any_cons** = any consonant in the same position

*  **any_v** = any vowel in the same position

*  **no_sound** = removed sound from the current position: "дом" - "дзюдо", 'м' - sound removed from the end: ('same_cons', 'same_stressed', 'no_sound')

*  **add_sound** = added sound to the current position: "дому" - "гнедому", 'у' is added: ('same_cons', 'same_stressed', 'same_cons', 'add_sound')

**5.** The code also calculates assonants/ consonants. For instance, I do not consider 'кобра'-'оброк' rhymes, as having the same sounds, they have these sounds on different positions. Here the algorithm is simplified and compares words by characters not sounds, taking into account number of the same vowels/ consonants and length of words.

**6.** The code molds dataframe sorting all rhymes by rhyme pattern scores and assonance scores. Rhymes, which recieved high score are not included into the final chart.


Code
____
* OOP based: builder, factory method design patterns 
* multiprocessing
* 62 tests: unit, functional, integration
* coverage - 97%
* sqlite3 as portable database
* PyCharm with Vim as IDE on Kubuntu
 
