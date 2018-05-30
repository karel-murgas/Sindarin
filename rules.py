"""Define grammar rules for Sindarian trainer"""
#    Copyright (C) 2017  Karel "laird Odol" Murgas
#    karel.murgas@gmail.com
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.


#############
# Libraries #
#############

from utilities import *
from constants import *


#############
# Functions #
#############

# TODO Add multiple mutation (and plural) variants when needed (like barad (tower vs doomed)) - indicate in exception
# TODO lists as second column, probably


# Mutations #

def modify_for_root_exception(word):
    """Return modified word if the word's root begins with nasal or unchanged word in other cases"""
    char = word[0]
    if char in ROOT_EXCEPTIONS:
        exceptions = loadtable(ROOT_EXCEPTIONS_FILES[char], separator=",")
        if word in [row[0] for row in exceptions]:
            return ROOT_EXCEPTIONS_STARTS[char] + word
    return word


def create_mutation_dictionary(prefixes, end):
    """Create the dictionary with names and values of mutations"""
    return {
        "1-soft": prefixes[1] + end,
        "2-nasal": prefixes[2] + end,
        "3-stop": prefixes[3] + end,
        "4-liquid": prefixes[4] + end,
        "5-mixed": prefixes[5] + end,
    }


def try_mutation(word, length):
    mutation_table = loadtable(MUTATIONS_FILES[length], separator=",")
    start = word[:length]
    end = word[length:]
    for row in mutation_table:
        if row[0] == start:
            return create_mutation_dictionary(row, end)
    return None


def mutate(word):
    """Return the dictionary with all mutations of given word"""

    word = modify_for_root_exception(word)
    if len(word) > 1:
        mutations = try_mutation(word, 2)
    if len(word) == 1 or mutations is None:
        mutations = try_mutation(word, 1)
    if mutations is None:
        mutations = create_mutation_dictionary([""]*6, word)
    return mutations


# Pluralisation #

def try_plural_exception(word):
    """Look into list of exception, if there is the given word, then return its plural"""

    exceptions = loadtable(PLURAL_EXCEPTIONS_FILE, separator=",")
    for row in exceptions:
        if row[0] == word:
            return row[1]
    return None


def is_vowel(char):
    """True if character is a vowel of any length"""

    # â = alt + 131
    # ê = alt + 136
    # î = alt + 140
    # ô = alt + 147
    # û = alt + 150
    # ŷ = ???

    if char in ("a", "á", "â", "e", "é", "ê", "i", "í", "î", "o", "ó", "ô", "u", "ú", "û", "y", "ý", "ŷ"):
        return True
    else:
        return False


def is_diphthong(duo):
    """True if given two characters are legitimate diphthongs in Sindarian"""

    if duo in ("ae", "ai", "au", "ei", "ie", "io", "iô", "oe", "ui"):
        return True
    else:
        return False


def mutate_vowel(chars, is_last):
    """Mutate diphthong according to table"""

    mutation_table = loadtable(PLURAL_MUTATIONS_FILES[len(chars)], separator=",")
    if is_last:
        column = 2
    else:
        column = 1
    for row in mutation_table:
        if row[0] == chars:
            return row[column]
    return chars


def plural_mutation(word):
    """Mutate vowels of given word to return its plural"""

    plural = ""
    index = len(word) - 1
    is_last = True
    while index >= 0:
        single = word[index]
        duo = word[index-1]+word[index]
        if is_vowel(single):
            if index > 0 and is_diphthong(duo):
                plural = mutate_vowel(duo, is_last) + plural
                index -= 2
            else:
                plural = mutate_vowel(single, is_last) + plural
                index -= 1
            is_last = False
        else:
            plural = single + plural
            index -= 1

    return plural


def pluralize(word):
    """Return plural of given word"""

    plural = try_plural_exception(word)
    if plural is None:
        return plural_mutation(word)
    return plural
