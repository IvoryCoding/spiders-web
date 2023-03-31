
#rulesTable = {}

class Hammer(): # Class for enforcing the rules

    def BanHammer():
        print(f'The hammer of banning ip addresses.')

class Judgement():
    rulesTable = {}
    activityTable = {}
    activeRules = { 'pa' : 0, 'af' : 0, 't': 0 }
    # if value ! 0 then Determine pattern from activity

    def ProcessCommands():
        print(f'{Judgement.activeRules}')

        # for key in rulesTable:
        #   list = rulesTable[key].split('-')
        #   for item in list[1:]:
        #       key, value = item.split(' ')
        #       activeRules[key] = value

    def ProcessActivity(activty):
        print(f'Dict \n{Judgement.activityTable}')

        # sudo code for this function

        # last thing this function does
        # if activity match activeRules then call BanHammer on ip address

    def DeterminePatterns():
        print(f'Where it determines a pattern if it fits within the rules')
        
        # if activeRules pa value > 0 --> check activityTable pa for pattern that matchs activeRules pa value
        # if activeRules af value > 0 --> check activityTable af for pattern that matchs activeRules pa value

        # -------------------------------- something like this --------------------------------
        # for key in activeRules:
        #   if activeRules[key] > 0:
        #       Judgement.ProcessActivity(activityTable[key])
