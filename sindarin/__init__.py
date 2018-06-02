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


"""Define webpage-function flask relations for html version"""


#############
# Libraries #
#############

from flask import Flask
from flask import request
from flask import render_template

from sindarin.rules import *


#############
# Functions #
#############


#########
# Flask #
#########

app = Flask(__name__)


@app.route("/")
def crossroad():
    return render_template("crossroad.html")


@app.route("/result")
def res():
    word = request.args.get("word").lower()
    chosen_rules = request.args.getlist("rules")
    mutations = None
    mutation_keys = None
    plural = None
    if word:
        if "mutate" in chosen_rules:
            mutations = mutate(word)
            mutation_keys = sorted(mutations)
        if "pluralize" in chosen_rules:
            plural = pluralize(word)

    return render_template("result.html", word=word, mutation_keys=mutation_keys, mutations=mutations, plural=plural)
