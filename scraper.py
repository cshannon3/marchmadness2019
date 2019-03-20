#import urllib2
from bs4 import BeautifulSoup as soup
import urllib.request

## last years

entryIds = {
    'Connor':'5444662',
    # 'Danny': '11512636',
    # 'Gerard' : '12285356',
    # 'Dugall' : '2471683',
    # 'Navarro' : '16940832',
    }
seedweight = [ 0, 1, 1.1, 1.1, 1.2, 1.3, 1.5, 1.8, 2.3, 3.1, 4.4, 6.5, 9.9, 15.4, 24.3, 38.7, 62]

for user, entryid in entryIds.items():
    points = 0
    bracket = "http://fantasy.espn.com/tournament-challenge-bracket/2018/en/entry?entryID=" + entryid
    with urllib.request.urlopen(bracket) as response:
        html = response.read()
    mysoup = soup(html, 'html.parser')
    gameid = 0

    
    for gameid in range(126):

        match = mysoup.find("div", attrs={'data-slotindex': str(gameid)})
        # round 1
        if gameid < 64:
            #print(match.find("span")['class'])
            gametags = match.find("span")['class']
            # game has already been played
            if ['actual', 'selectedToAdvance', 'winner'] == gametags:
                    seed = match.find('span', attrs={'class': 'seed'})
                    points += seedweight[int(seed.text.strip())]
                    print(seed.text.strip())
            
        # round 2
        elif gameid < 96:
            gametags = match.find_all("span")[1]['class']
            print(gametags)
           
        # # sweet sixteen
        # elif gameid < 112:
        
        # # elite 8
        # elif gameid< 120:
            
        # # final 4
        # elif gameid<124:
         
    

