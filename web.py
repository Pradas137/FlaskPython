from __future__ import print_function

from flask import Flask
app = Flask(__name__)

from collections import OrderedDict
from flask import render_template
from flask import request
from flask import current_app
import random
import logging
import sys

from collections import OrderedDict

def file():
    participantes = []
    file = open("equips.cfg", "r")
    for team in file:
        participantes.append(team.rstrip("\n"))
    return participantes

def CrearLiga():
    Liga = {}
    for Local in teams:
        Liga[Local] = {}
        for Visitantes in teams:
            if Visitantes == Local:
                Liga[Local][Visitantes] = "X"
            else:
                Liga[Local][Visitantes] = ""
    return Liga


def CrearRanking():
    ranking = {}
    for Local in teams:
        ranking[Local] = 0
    return ranking


def Actualizar(Local, Visitantes, golesL, golesV):
    Liga[Local][Visitantes] = golesL
    Liga[Visitantes][Local] = golesV


def Ranking():
    global ranking
    ranking = CrearRanking()
    equipos = []
    for Local in Liga:
        for visitantes in Liga[Local]:
            if Liga[local][Visitantes] != "":
                if Local and visitantes not in equipos and Local != Visitantes:
                    points = check_ranking_points(
                        Liga[Local][Visitantes], Liga[Visitantes][Local])
                    set_ranking_points(points, Local, Visitantes)
        equipos.append(Local)


def check_ranking_points(Local, Visitantes):
    """Check how many points did the local team win."""
    if Local != "":
        if Local > Visitantes:
            return 3
        elif Local == Visitantes:
            return 1
        else:
            return 0
    else:
        return 0


def set_ranking_points(points, Local, Visitantes):
    """Sum the points depending on the condition."""
    if points == 3:
        ranking[Local] += points
    elif points == 1:
        ranking[Local] += points
        ranking[Visitantes] += points
    else:
        ranking[Local] += points
        ranking[Visitantes] += 3


equips = file()
Liga = CrearLiga()
ranking = CrearRanking()

@app.route('/')
def Menu():
    return render_template("Menu.html")


@ app.route('/Partidos')
def Partidos():
    return render_template("Partidos.html", Liga=Liga, equips=equips)


@ app.route('/Equipos')
def Equipos():
    return render_template("Equipos.html", equips=equips)


@app.route('/Goles')
def Goles(error=None):
    return render_template("Partidos.html", equips=equips, error=error)


@app.route('/Ranking')
def Ranking(error=None):
    Ranking()
    return render_template("Ranking.html", ranking=sorted(ranking.items(), key=lambda x: x[1], reverse=True))


@app.route('/goals', methods=["POST"])
def goals_input_post():
    Local = request.form["localTeam"]
    Visitantes = request.form["visitantTeam"]
    golesL = request.form["localTeamScore"]
    golesV = request.form["visitantTeamScore"]
    if Local == Visitantes:
        return Goles("sameTeams")
    else:
        Actualizar(Local, Visitantes, golesL, golesV)
        return redirect(url_for("league_grid"))


if __name__ == '__main__':
    app.run()