import re

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
        activityTimes = {}

        for line in activity.split('\n'):
            try:
                date_time = re.search(r'\w+\s+\d+ \d+:\d+:\d+', line).group()
                ip_address = re.search(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', line).group()

                if ip_address not in activityTimes:
                    activityTimes[ip_address] = []

                activityTimes[ip_address].append(date_time)

            except:
                print()
        
        print(f'[times] {activityTimes}\n')

        # Add code to now filter and compare the activity and see if they are a match to the rules

    def DeterminePatterns():
        for key in Judgement.activeRules:
            if Judgement.activeRules[key] and key != 't':
                Judgement.ProcessActivity(Judgement.activityTable[key])
