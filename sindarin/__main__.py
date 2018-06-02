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


"""Main code for Sindarin trainer"""


#############
# Libraries #
#############

from sindarin.rules import *


#############
# Functions #
#############

def mutations():
    """Ask for Sindarin word and prints it's mutations"""

    word = input("Which word would you like to mutate?\n").lower()
    if word == "exit":
        return False
    elif len(word) > 0:
        mutation_list = mutate(word)
        print("\n".join("{}:  \t{}".format(k, v) for k, v in sorted(mutation_list.items())) + "\n")
    else:
        print("Type something")
    return True


def plurals():
    """Ask for Sindarin word and prints it's plural"""

    word = input("Which word would you like to pluralize?\n").lower()
    if word == "exit":
        return False
    elif len(word) > 0:
        plural = pluralize(word)
        print(plural + "\n")
    else:
        print("Type something")
    return True


def choose_exercise():
    """Ask for exercise type and return it's code"""

    exercise = input("Which rule do you want to test?\n"
                     "(m) Mutations\n"
                     "(p) Pluralization\n"
                     "(e) Exit\n").lower()
    if exercise not in ("m", "p", "e"):
        exercise = choose_exercise()
    return exercise


def run():
    """The main code calling specific lessons"""

    repeat = True
    while repeat:
        exercise = choose_exercise()
        if exercise == "m":
            repeat = mutations()
        elif exercise == "p":
            repeat = plurals()
        else:
            repeat = False


if __name__ == '__main__':
    run()
