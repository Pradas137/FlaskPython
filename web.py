from flask import Flask, request, redirect, url_for, render_template
app = Flask(__name__)




def Equipos():
    """Load teams and append to list from file."""
    Lista_equipos = []
    file = open("equips.cfg", "r")
    for equips in file:
        Lista_equipos.append(equips.rstrip("\n"))
    return Lista_equipos


def CrearLiga():
    """ Creates the league matrix."""
    Liga = {}
    for Local in equips:
        Liga[Local] = {}
        for Visitante in equips:
            if Visitante == Local:
                Liga[Local][Visitante] = "X"
            else:
                Liga[Local][Visitante] = ""
    return Liga



equips = Equipos()
Ligas = CrearLiga()


@app.route('/')
def Menu():
    return render_template("Menu.html")

@ app.route('/Equipos')
def Lista_equipos():
    return render_template("Equipos.html", equips=equips)

@ app.route('/Partidos')
def league_grid():
    return render_template("Partidos.html", Ligas=Ligas, equips=equips)


def update_league(local_team, visitant_team, local_goals, visitant_goals):
    """Update goals on the league matrix."""
    league[local_team][visitant_team] = local_goals
    league[visitant_team][local_team] = visitant_goals


def update_ranking():
    """TODO: Work on a better function."""
    global ranking
    ranking = create_ranking()
    done_teams = []
    for local_team in league:
        for visitant_team in league[local_team]:
            if league[local_team][visitant_team] != "":
                if local_team and visitant_team not in done_teams and local_team != visitant_team:
                    points = check_ranking_points(
                        league[local_team][visitant_team], league[visitant_team][local_team])
                    set_ranking_points(points, local_team, visitant_team)
        done_teams.append(local_team)


def check_ranking_points(local, visitant):
    """Check how many points did the local team win."""
    if local != "":
        if local > visitant:
            return 3
        elif local == visitant:
            return 1
        else:
            return 0
    else:
        return 0


def set_ranking_points(points, local_team, visitant_team):
    """Sum the points depending on the condition."""
    if points == 3:
        ranking[local_team] += points
    elif points == 1:
        ranking[local_team] += points
        ranking[visitant_team] += points
    else:
        ranking[local_team] += points
        ranking[visitant_team] += 3

        
@app.route('/Partidos', methods=["POST"])
def goals_input_post():
    Local = request.form["EquipoLocal"]
    Visitante = request.form["EquipoVisitante"]
    GolesL = request.form["PuntuacionLocal"]
    GolesV = request.form["Puntuacionvisitante"]
    if Local == visitante:
        return goals_input("sameTeams")
    else:
        update_league(Local, Visitante, Golesl, GolesV)
        return redirect(url_for("league_grid"))
if __name__ == '__main__':
    app.run()