# link: https://www.codewars.com/kata/51e056fe544cf36c410000fb


# description: Write a function that, given a string of text (possibly with punctuation and line-breaks),
#              returns an array of the top-3 most occurring words, in descending order of the number of occurrences.

# assumptions:
#  A word is a string of letters (A to Z) optionally containing one or more apostrophes (') in ASCII.
#  Apostrophes can appear at the start, middle or end of a word ('abc, abc', 'abc', ab'c are all valid)
#  Any other characters (e.g. #, \, / , . ...) are not part of a word and should be treated as whitespace.
#  Matches should be case-insensitive, and the words in the result should be lowercased.
#  Ties may be broken arbitrarily.
#  If a text contains fewer than three unique words, then either the top-2 or top-1 words should be returned, or an empty array if a text contains no words.


import re


def top_3_words(text):
    pattern = r"[^a-zA-Z']+"
    modified_text = re.sub(pattern, " ", text)
    modified_text = re.sub(r" '+ ", " ", modified_text)
    w_freq = {}
    for w in modified_text.split():
        w = w.lower()
        if w not in w_freq:
            w_freq[w] = 0
        w_freq[w] += 1
    return list(
        map(
            lambda i: i[0], sorted(w_freq.items(), key=lambda i: i[1], reverse=True)[:3]
        )
    )
