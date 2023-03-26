
rulesTable = {}

class Hammer(): # Class for enforcing the rules

    def BanHammer():
        print(f'The hammer of banning ip addresses.')

class Judgement():

    def ProcessCommands(cmd_list):
        # Add to rules table. More will come later.
        rulesTable[cmd_list[0]] = ' '.join(cmd_list[1:])

    def ProcessActivity(act_list):
        print(f'Processing the activity')
        print(f'{act_list}')

    def DeterminePatterns():
        print(f'Where it determines a pattern if it fits within the rules')
