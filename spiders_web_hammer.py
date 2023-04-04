
#rulesTable = {}

class Hammer(): # Class for enforcing the rules

    def BanHammer():
        print(f'The hammer of banning ip addresses.')

class Judgement():
    rulesTable = {}
    activityTable = {}
    activeRules = { 'pa' : 0, 'af' : 0, 't': 0 }

    def ProcessCommands():
        for key in Judgement.rulesTable:
            rules_list = Judgement.rulesTable[key].split('-')
            
            for item in rules_list[1:]:
                item_list = item.split(' ')
                Judgement.activeRules[item_list[0]] = item_list[1]

    def ProcessActivity(activity):
        print(f'Info \n{activity}')

        # sudo code for this function

        # Parse the activity into a dictionary as such -> {'ip': ['date&time-device name-username', 'date&time-device name 2-username'], 'ip2': ['date&time-device name-username', 'date&time-device name 2-username']}

        # last thing this function does
        # if activity match activeRules then call BanHammer on ip address

    def DeterminePatterns():
        for key in Judgement.activeRules:
            if Judgement.activeRules[key] and key != 't':
                Judgement.ProcessActivity(Judgement.activityTable[key])
