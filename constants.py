"""Define constants for Sindarin trainer"""
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
# Constants #
#############

ROOT_EXCEPTIONS = ("d", "b", "g")

ROOT_EXCEPTIONS_STARTS = {
    "d": "n",
    "b": "m",
    "g": "n",
}

ROOT_EXCEPTIONS_FILES = {
    "d": "Resources/nd_roots.txt",
    "b": "Resources/mb_roots.txt",
    "g": "Resources/ng_roots.txt",
}

MUTATIONS_FILES = {
    1: "Resources/mutations_1_letter.csv",
    2: "Resources/mutations_2_letters.csv",
}

PLURAL_EXCEPTIONS_FILE = "Resources/plural_exceptions.csv"

PLURAL_MUTATIONS_FILES = {
    1: "Resources/plural_vowel_mutations_single.csv",
    2: "Resources/plural_vowel_mutations_diphthongs.csv"
}