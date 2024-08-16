import requests
from bs4 import BeautifulSoup
import pandas as pd

#reusable URLs to help us get the different categories that we want. 

pro_football_reference_main = 'https://www.pro-football-reference.com/years/'
most_recent_season = '2023'

passing_stats = '/passing.htm'
rushing_stats = '/rushing.htm'
receiving_stats = '/receiving.htm'
fantasy_stats = '/fantasy.htm'


def get_stats(url):
    """Downloads the web page and we will return a beautiful soup doc."""
    response = requests.get(url)
        
    # verify that we are receiving the correct response
    
    if response.status_code != 200:
        raise Exception(f'Unable to download page{url}')
        
    # Get the HTML from the page
    page_content = response.text
    
    # create our bs4 doc
    doc = BeautifulSoup(response.text, 'html.parser')
    return doc





# In[7]:


def get_all_qbs(qb_stats):
    qbs = qb_stats.find('tbody').find_all('tr')
    all_qbs_data = []
    for qb in qbs:
        
        try:
            all_stats = {
                'name': qb.find('td').find('a').text,
                'pos' :     qb.find(attrs = {'data-stat' : 'pos'}).text,
                'comp_pct': qb.find(attrs = {'data-stat' : 'pass_cmp_pct'}).text,
                'pass_yds': qb.find(attrs = {'data-stat' : 'pass_yds'}).text,
                'pass_td' : qb.find(attrs = {'data-stat' : 'pass_td'}).text,
                'pass_int' : qb.find(attrs = {'data-stat' : 'pass_int'}).text,
                'pass_td_%' : qb.find(attrs = {'data-stat': 'pass_td_pct'}).text,
                'QB_Rating' : qb.find(attrs = {'data-stat' : 'qbr'}).text,
                'Fourth_Qtr_Comebacks': qb.find(attrs = {'data-stat' : 'comebacks'}).text  
        }
        
        except:
            all_qbs_data.append({})
            print('No data here')
        all_qbs_data.append(all_stats)
    return all_qbs_data


def write_csv(items, path):
    #open the file in write mode
    with open(path, 'w') as f:
        #return nothing if there's nothing to write
        if len(items) == 0:
            return
        
        #write the headers in the first line of csv
        headers = list(items[0].keys())
        f.write(','.join(headers) +'\n')
        
        #write one item per line from our dictionary
        for item in items:
            values = []
            for header in headers:
                values.append(str(item.get(header, '')))
            f.write(','.join(values) + '\n')



def get_all_teams(team_stats):
    qbs = qb_stats.find('tbody').find_all('tr')
    all_qbs_data = []
    for qb in qbs:
        
        try:
            all_stats = {
                'name': qb.find('td').find('a').text,
                'pos' :     qb.find(attrs = {'data-stat' : 'pos'}).text,
                'comp_pct': qb.find(attrs = {'data-stat' : 'pass_cmp_pct'}).text,
                'pass_yds': qb.find(attrs = {'data-stat' : 'pass_yds'}).text,
                'pass_td' : qb.find(attrs = {'data-stat' : 'pass_td'}).text,
                'pass_int' : qb.find(attrs = {'data-stat' : 'pass_int'}).text,
                'pass_td_%' : qb.find(attrs = {'data-stat': 'pass_td_pct'}).text,
                'QB_Rating' : qb.find(attrs = {'data-stat' : 'qbr'}).text,
                'Fourth_Qtr_Comebacks': qb.find(attrs = {'data-stat' : 'comebacks'}).text  
        }
        
        except:
            print('No data here')
        all_qbs_data.append(all_stats)
    return all_qbs_data





def get_all_teams(team_stats):
    teams = team_stats.find('tbody').find_all('tr')
    all_teams_data = []
    for team in teams:
        
        try:
            all_stats = {
                'team': team.find('th', attrs={"data-stat": "team"}).find('a').text,
                'wins' :     team.find(attrs = {'data-stat' : 'wins'}).text,
                'win_loss_perc': team.find(attrs = {'data-stat' : 'win_loss_perc'}).text,
                'points': team.find(attrs = {'data-stat' : 'points'}).text,
                'points_opp' : team.find(attrs = {'data-stat' : 'points_opp'}).text,
                'points_diff' : team.find(attrs = {'data-stat' : 'points_diff'}).text,
                'mov' : team.find(attrs = {'data-stat': 'mov'}).text,
                'sos_total' : team.find(attrs = {'data-stat' : 'sos_total'}).text,
                'srs_total': team.find(attrs = {'data-stat' : 'srs_total'}).text ,
                'srs_offense': team.find(attrs = {'data-stat' : 'srs_offense'}).text,
                'srs_defense': team.find(attrs = {'data-stat' : 'srs_defense'}).text 
        }
        
        except:
            all_stats = {}
            print('No data here')
        all_teams_data.append(all_stats)
    return all_teams_data


def main():
    qb_stats = get_stats(pro_football_reference_main + most_recent_season + passing_stats)
    write_csv(get_all_qbs(qb_stats), '2023_qb_stats.csv')
    
    team_stats = get_stats(pro_football_reference_main + most_recent_season)
    write_csv(get_all_teams(team_stats), '2023_team_stats.csv')


