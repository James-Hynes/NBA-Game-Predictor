from GatherStats import *
from random import *
from math import *
import threading
import time

loadVar = 'Loading.'

team1, team2 = 'Golden State Warriors', 'Los Angeles Lakers'

TeamOneStats, TeamTwoStats = TeamGeneralStats(team1, team2), TeamGeneralStats(team2, team1)


def get_score():
    teamOneBase, teamTwoBase = TeamOneStats.base_stats(), TeamTwoStats.base_stats()
    teamOneAdv, teamTwoAdv = TeamOneStats.adv_stats(), TeamTwoStats.adv_stats()

    TeamOneStats.change_opponent(), TeamTwoStats.change_opponent()

    teamOneBaseOpp, teamTwoBaseOpp = TeamOneStats.base_stats(), TeamTwoStats.base_stats()
    teamOneAdvOpp, teamTwoAdvOpp = TeamOneStats.adv_stats(), TeamTwoStats.adv_stats()

    teamOneNormalPointsScored, teamTwoNormalPointsScored = teamOneBase['PTS'], teamTwoBase['PTS']
    teamOneAgainstOppPointsScored, teamTwoAgainstOppPointsScored = teamOneBaseOpp['PTS'], teamTwoBaseOpp['PTS']

    teamOneAverage = (teamOneNormalPointsScored + teamOneAgainstOppPointsScored) / 2
    teamTwoAverage = (teamTwoNormalPointsScored + teamTwoAgainstOppPointsScored) / 2

    print(teamOneBase['TEAM_NAME'], teamOneAverage, teamTwoBase['TEAM_NAME'], teamTwoAverage)

score_thread = threading.Thread(target=get_score)
score_thread.start()


while score_thread.is_alive():
    time.sleep(1)
    print(loadVar)

score_thread.join()
