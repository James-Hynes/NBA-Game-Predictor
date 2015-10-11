"""
Gather stats from stats.nba.com's resources with json.
They will be used later to determine outcomes of games.

Author: James Hynes
Initial Date: October 11, 2015
Recent Commit: October 11, 2015
Recent Update: None

"""

import requests

teams = {
    'Atlanta Hawks': 0,
    'Boston Celtics': 1,
    'Brooklyn Nets': 2,
    'Charlotte Hornets': 3,
    'Chicago Bulls': 4,
    'Cleveland Cavaliers': 5,
    'Dallas Mavericks': 6,
    'Denver Nuggets': 7,
    'Detroit Pistons': 8,
    'Golden State Warriors': 9,
    'Houston Rockets': 10,
    'Indiana Pacers': 11,
    'Los Angeles Clippers': 12,
    'Los Angeles Lakers': 13,
    'Memphis Grizzlies': 14,
    'Miami Heat': 15,
    'Milwaukee Bucks': 16,
    'Minnesota Timberwolves': 17,
    'New Orleans Pelicans': 18,
    'New York Knicks': 19,
    'Oklahoma City Thunder': 20,
    'Orlando Magic': 21,
    'Philadelphia 76ers': 22,
    'Phoenix Suns': 23,
    'Portland Trailblazers': 24,
    'Sacramento Kings': 25,
    'San Antonio Spurs': 26,
    'Toronto Raptors': 27,
    'Utah Jazz': 28,
    'Washington Wizards': 29
}


class TeamGeneralStats:

    def __init__(self, teamname):
        self.teamname = teamname

        self.url = 'http://stats.nba.com/stats/leaguedashteamstats?'

        self.params = {'Conference': '', 'DateFrom': '', 'DateTo': '', 'Division': '', 'GameScope': '', 'GameSegment': '',
                  'LastNGames': '0', 'LeagueID': '00', 'Location': '', 'MeasureType': 'Base', 'Month': '0',
                  'OpponentTeamID': '0', 'Outcome': '', 'PORound': '', 'PaceAdjust': 'N', 'PerMode': 'PerGame',
                  'Period': '0', 'PlayerExperience': '', 'PlayerPosition': '', 'PlusMinus': 'N', 'Rank': 'N',
                  'Season': '2014-15', 'SeasonSegment': '', 'SeasonType': 'Regular Season', 'ShotClockRange': '',
                  'StarterBench': '', 'TeamID': '0', 'VsConference': '', 'VsDivision': ''}

    def base_stats(self):
        page = requests.get(self.url, self.params)

        values = page.json()['resultSets'][0]['rowSet']
        headers = page.json()['resultSets'][0]['headers']
        return [dict(zip(headers, value)) for value in values][teams[self.teamname]]

    def adv_stats(self):
        # Change MeasureType param to Advanced
        self.params['MeasureType'] = 'Advanced'

        page = requests.get(self.url, self.params)

        values = page.json()['resultSets'][0]['rowSet']
        headers = page.json()['resultSets'][0]['headers']
        return [dict(zip(headers, value)) for value in values][teams[self.teamname]]

    def four_factors(self):
        # Change MeasureType param to Four Factors
        self.params['MeasureType'] = 'Four Factors'

        page = requests.get(self.url, self.params)

        values = page.json()['resultSets'][0]['rowSet']
        headers = page.json()['resultSets'][0]['headers']
        return [dict(zip(headers, value)) for value in values][teams[self.teamname]]

    def misc_stats(self):
        # Change MeasureType param to Misc
        self.params['MeasureType'] = 'Misc'

        page = requests.get(self.url, self.params)

        values = page.json()['resultSets'][0]['rowSet']
        headers = page.json()['resultSets'][0]['headers']
        return [dict(zip(headers, value)) for value in values][teams[self.teamname]]

    def scoring_stats(self):
        # Change MeasureType param to Scoring
        self.params['MeasureType'] = 'Scoring'

        page = requests.get(self.url, self.params)

        values = page.json()['resultSets'][0]['rowSet']
        headers = page.json()['resultSets'][0]['headers']
        return [dict(zip(headers, value)) for value in values][teams[self.teamname]]

    def opponent_stats(self):
        # Change MeasureType param to Opponent
        self.params['MeasureType'] = 'Opponent'

        page = requests.get(self.url, self.params)

        values = page.json()['resultSets'][0]['rowSet']
        headers = page.json()['resultSets'][0]['headers']
        return [dict(zip(headers, value)) for value in values][teams[self.teamname]]


print(TeamGeneralStats('Golden State Warriors').opponent_stats())
