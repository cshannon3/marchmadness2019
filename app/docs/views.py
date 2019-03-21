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
    teams = [[]]
    #points = 0
    bracket = "http://fantasy.espn.com/tournament-challenge-bracket/2018/en/entry?entryID=5444662"
    with urllib.request.urlopen(bracket) as response:
        html = response.read()
    mysoup = soup(html, 'html.parser')
    gameid = 0
    for gameid in range(64):
        match = mysoup.find("div", attrs={'data-slotindex': str(gameid)})
        teamid = int(match['data-teamid'][0])
        teamname = match.find('span', attrs={'class': 'name'}).text.strip()
        teamseed = match.find('span', attrs={'class': 'seed'}).text.strip()
        
        teams.append([teamid, teamname, teamseed])
     
    return view('listteams.html', teams=teams)

@docs.route('/connor')
def connorbracket():
    teams = [[]]
    #points = 0
    bracket = "http://fantasy.espn.com/tournament-challenge-bracket/2019/en/entry?entryID=27874548"
    with urllib.request.urlopen(bracket) as response:
        html = response.read()
    mysoup = soup(html, 'html.parser')
    gameid = 0
    for gameid in range(126):
        

        match = mysoup.find("div", attrs={'data-slotindex': str(gameid)})
        teamid = int(match['data-teamid'])
        teamname = match.find('span', attrs={'class': 'name'}).text.strip()
        teamseed = match.find('span', attrs={'class': 'seed'}).text.strip()
        pickedstatus = 0
        # pick status-- either:
        # 0      not picked -- game tbd // black
        # 1      picked - game tbd // blue
        # 2      picked incorrectly or out -- //red
        # 3      picked correctly -- // green
        pickedstatus = 0
        if gameid < 64:
            gametags = match.find("span")['class']
            if 'selectedToAdvance' in gametags:
                # picked by user 
                # if not picked by user it will stay equal to 0 and be black
                if 'winner' in gametags:
                    # user was right
                    pickedstatus=3
                elif 'loser' in gametags:
                    # user was wrong
                    pickedstatus=2
                else:
                    # game hasn't been played yet
                    pickedstatus = 1
        teams.append([teamid, teamname, teamseed, pickedstatus])
     
    return view('userbracket.html', teams=teams)


@docs.route('/dugall')
def connorbracket():
    teams = [[]]
    #points = 0
    bracket = "http://fantasy.espn.com/tournament-challenge-bracket/2019/en/entry?entryID=21937492"
    with urllib.request.urlopen(bracket) as response:
        html = response.read()
    mysoup = soup(html, 'html.parser')
    gameid = 0
    for gameid in range(126):
        

        match = mysoup.find("div", attrs={'data-slotindex': str(gameid)})
        teamid = int(match['data-teamid'])
        teamname = match.find('span', attrs={'class': 'name'}).text.strip()
        teamseed = match.find('span', attrs={'class': 'seed'}).text.strip()
        pickedstatus = 0
        # pick status-- either:
        # 0      not picked -- game tbd // black
        # 1      picked - game tbd // blue
        # 2      picked incorrectly or out -- //red
        # 3      picked correctly -- // green
        pickedstatus = 0
        if gameid < 64:
            gametags = match.find("span")['class']
            if 'selectedToAdvance' in gametags:
                # picked by user 
                # if not picked by user it will stay equal to 0 and be black
                if 'winner' in gametags:
                    # user was right
                    pickedstatus=3
                elif 'loser' in gametags:
                    # user was wrong
                    pickedstatus=2
                else:
                    # game hasn't been played yet
                    pickedstatus = 1
        teams.append([teamid, teamname, teamseed, pickedstatus])
     
    return view('userbracket.html', teams=teams)


@docs.route('/navarro')
def connorbracket():
    teams = [[]]
    #points = 0
    bracket = "http://fantasy.espn.com/tournament-challenge-bracket/2019/en/entry?entryID=25101213"
    with urllib.request.urlopen(bracket) as response:
        html = response.read()
    mysoup = soup(html, 'html.parser')
    gameid = 0
    for gameid in range(126):
        

        match = mysoup.find("div", attrs={'data-slotindex': str(gameid)})
        teamid = int(match['data-teamid'])
        teamname = match.find('span', attrs={'class': 'name'}).text.strip()
        teamseed = match.find('span', attrs={'class': 'seed'}).text.strip()
        pickedstatus = 0
        # pick status-- either:
        # 0      not picked -- game tbd // black
        # 1      picked - game tbd // blue
        # 2      picked incorrectly or out -- //red
        # 3      picked correctly -- // green
        pickedstatus = 0
        if gameid < 64:
            gametags = match.find("span")['class']
            if 'selectedToAdvance' in gametags:
                # picked by user 
                # if not picked by user it will stay equal to 0 and be black
                if 'winner' in gametags:
                    # user was right
                    pickedstatus=3
                elif 'loser' in gametags:
                    # user was wrong
                    pickedstatus=2
                else:
                    # game hasn't been played yet
                    pickedstatus = 1
        teams.append([teamid, teamname, teamseed, pickedstatus])
     
    return view('userbracket.html', teams=teams)


@docs.route('/mike')
def connorbracket():
    teams = [[]]
    #points = 0
    bracket = "http://fantasy.espn.com/tournament-challenge-bracket/2019/en/entry?entryID=26993737"
    with urllib.request.urlopen(bracket) as response:
        html = response.read()
    mysoup = soup(html, 'html.parser')
    gameid = 0
    for gameid in range(126):
        

        match = mysoup.find("div", attrs={'data-slotindex': str(gameid)})
        teamid = int(match['data-teamid'])
        teamname = match.find('span', attrs={'class': 'name'}).text.strip()
        teamseed = match.find('span', attrs={'class': 'seed'}).text.strip()
        pickedstatus = 0
        # pick status-- either:
        # 0      not picked -- game tbd // black
        # 1      picked - game tbd // blue
        # 2      picked incorrectly or out -- //red
        # 3      picked correctly -- // green
        pickedstatus = 0
        if gameid < 64:
            gametags = match.find("span")['class']
            if 'selectedToAdvance' in gametags:
                # picked by user 
                # if not picked by user it will stay equal to 0 and be black
                if 'winner' in gametags:
                    # user was right
                    pickedstatus=3
                elif 'loser' in gametags:
                    # user was wrong
                    pickedstatus=2
                else:
                    # game hasn't been played yet
                    pickedstatus = 1
        teams.append([teamid, teamname, teamseed, pickedstatus])
     
    return view('userbracket.html', teams=teams)

@docs.route('/julia')
def connorbracket():
    teams = [[]]
    #points = 0
    bracket = "http://fantasy.espn.com/tournament-challenge-bracket/2019/en/entry?entryID=32616442"
    with urllib.request.urlopen(bracket) as response:
        html = response.read()
    mysoup = soup(html, 'html.parser')
    gameid = 0
    for gameid in range(126):
        

        match = mysoup.find("div", attrs={'data-slotindex': str(gameid)})
        teamid = int(match['data-teamid'])
        teamname = match.find('span', attrs={'class': 'name'}).text.strip()
        teamseed = match.find('span', attrs={'class': 'seed'}).text.strip()
        pickedstatus = 0
        # pick status-- either:
        # 0      not picked -- game tbd // black
        # 1      picked - game tbd // blue
        # 2      picked incorrectly or out -- //red
        # 3      picked correctly -- // green
        pickedstatus = 0
        if gameid < 64:
            gametags = match.find("span")['class']
            if 'selectedToAdvance' in gametags:
                # picked by user 
                # if not picked by user it will stay equal to 0 and be black
                if 'winner' in gametags:
                    # user was right
                    pickedstatus=3
                elif 'loser' in gametags:
                    # user was wrong
                    pickedstatus=2
                else:
                    # game hasn't been played yet
                    pickedstatus = 1
        teams.append([teamid, teamname, teamseed, pickedstatus])
     
    return view('userbracket.html', teams=teams)

@docs.route('/ely')
def connorbracket():
    teams = [[]]
    #points = 0
    bracket = "http://fantasy.espn.com/tournament-challenge-bracket/2019/en/entry?entryID=28875636"
    with urllib.request.urlopen(bracket) as response:
        html = response.read()
    mysoup = soup(html, 'html.parser')
    gameid = 0
    for gameid in range(126):
        

        match = mysoup.find("div", attrs={'data-slotindex': str(gameid)})
        teamid = int(match['data-teamid'])
        teamname = match.find('span', attrs={'class': 'name'}).text.strip()
        teamseed = match.find('span', attrs={'class': 'seed'}).text.strip()
        pickedstatus = 0
        # pick status-- either:
        # 0      not picked -- game tbd // black
        # 1      picked - game tbd // blue
        # 2      picked incorrectly or out -- //red
        # 3      picked correctly -- // green
        pickedstatus = 0
        if gameid < 64:
            gametags = match.find("span")['class']
            if 'selectedToAdvance' in gametags:
                # picked by user 
                # if not picked by user it will stay equal to 0 and be black
                if 'winner' in gametags:
                    # user was right
                    pickedstatus=3
                elif 'loser' in gametags:
                    # user was wrong
                    pickedstatus=2
                else:
                    # game hasn't been played yet
                    pickedstatus = 1
        teams.append([teamid, teamname, teamseed, pickedstatus])
     
    return view('userbracket.html', teams=teams)

@docs.route('/manno')
def connorbracket():
    teams = [[]]
    #points = 0
    bracket = "http://fantasy.espn.com/tournament-challenge-bracket/2019/en/entry?entryID=28024719"
    with urllib.request.urlopen(bracket) as response:
        html = response.read()
    mysoup = soup(html, 'html.parser')
    gameid = 0
    for gameid in range(126):
        

        match = mysoup.find("div", attrs={'data-slotindex': str(gameid)})
        teamid = int(match['data-teamid'])
        teamname = match.find('span', attrs={'class': 'name'}).text.strip()
        teamseed = match.find('span', attrs={'class': 'seed'}).text.strip()
        pickedstatus = 0
        # pick status-- either:
        # 0      not picked -- game tbd // black
        # 1      picked - game tbd // blue
        # 2      picked incorrectly or out -- //red
        # 3      picked correctly -- // green
        pickedstatus = 0
        if gameid < 64:
            gametags = match.find("span")['class']
            if 'selectedToAdvance' in gametags:
                # picked by user 
                # if not picked by user it will stay equal to 0 and be black
                if 'winner' in gametags:
                    # user was right
                    pickedstatus=3
                elif 'loser' in gametags:
                    # user was wrong
                    pickedstatus=2
                else:
                    # game hasn't been played yet
                    pickedstatus = 1
        teams.append([teamid, teamname, teamseed, pickedstatus])
     
    return view('userbracket.html', teams=teams)