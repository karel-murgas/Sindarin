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

from rules import *
from flask import Flask
from flask import request
from flask import render_template


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
    word = request.args.get("word")
    rules = request.args.getlist("rules")
    if "mutate" in rules:
        mutations = mutate(word)
    else:
        mutations = None
    if "pluralize" in rules:
        plural = pluralize(word)
    else:
        plural = None

    return render_template("result.html", word=word, mutations=mutations, plural=plural)
