'''
Created on Mar 5, 2020

@author: ealygg
'''
from Src.Team import Team

class Offense(Team):
    def __init__(self, teamName, activity):
        Team.__init__(self, teamName, activity)

class Defense(Team):
    pass