from flask import Blueprint, render_template as view
from bs4 import BeautifulSoup as soup
import urllib.request


docs = Blueprint('docs', __name__, static_folder='static', template_folder='templates')


@docs.route('/')
def index():
    """
    Show an index template
    :return:
    """
    return view('index.html')


@docs.route('/bracket')
def bracket():
    return view('bracket.html')


@docs.route('/listteams')
def listteams():
    teams = []
    #points = 0
    bracket = "http://fantasy.espn.com/tournament-challenge-bracket/2018/en/entry?entryID=5444662"
    with urllib.request.urlopen(bracket) as response:
        html = response.read()
    mysoup = soup(html, 'html.parser')
    gameid = 0
    for gameid in range(64):
        match = mysoup.find("div", attrs={'data-slotindex': str(gameid)})
        teamname = match.find('span', attrs={'class': 'name'})
        teams.append(teamname)
     
    return view('listteams.html', teams=teams)