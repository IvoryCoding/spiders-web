
#rulesTable = {}

class Hammer(): # Class for enforcing the rules

    def BanHammer():
        print(f'The hammer of banning ip addresses.')

class Judgement():
    rulesTable = {}

    def ProcessCommands(cmd_list):
        # Add to rules table. More will come later.
        Judgement.rulesTable[cmd_list[0]] = ' '.join(cmd_list[1:])

        # Process the rule command first
        # ie: ban -pa 3
        #       or
        # ie: ban -pa 2 -t 100
        # (2 password attempts in 100 milliseconds or 1 second) == ban

    def ProcessActivity(act_list):
        print(f'Processing the activity')
        print(f'{act_list}')

    def DeterminePatterns():
        print(f'Where it determines a pattern if it fits within the rules')
        # For each rule in rule list:
        # compare activity to rule
        # if action required, call BanHammer()
