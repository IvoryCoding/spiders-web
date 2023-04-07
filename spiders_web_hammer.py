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
        # Parse the activity into a dictionary as such -> {'ip': ['date&time-device name-username', 'date&time-device name 2-username'], 'ip2': ['date&time-device name-username', 'date&time-device name 2-username']}
        activityTimes = {}

        for line in activity.split('\n'):
            try:
                date_time = re.search(r'\w+\s+\d+ \d+:\d+:\d+', line).group()
                ip_address = re.search(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', line).group()

                # Now how the fuck do you take these and put them into a idexable list or a dictionary to compare the times

                print(f'{ip_address} | {date_time}')
            except:
                return
        
        print(f'[test] {activityTimes}')

    def DeterminePatterns():
        for key in Judgement.activeRules:
            if Judgement.activeRules[key] and key != 't':
                Judgement.ProcessActivity(Judgement.activityTable[key])
