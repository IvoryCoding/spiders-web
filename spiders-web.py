#! /usr/bin/env python3

#   Date:           2022/11/23
#   Author:         Emma Gillespie | YouTube: IvoryCoding | GitHub: IvoryCoding
#   Description:    A program that creates a web of network monitored devices. Capturing attacks
#                   and banning ips from machines within the spiders web.

import argparse
import sys

from spiders_web_core import *

def AsciiArt():
    print("\n\n")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡖⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠘⢦⠀⠀⠀⠀⠀⠀⠀⠀⢠⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠈⢳⡀⠀⠀⠀⠀⠀⣠⣾⠙⢦⣀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠔⠂")
    print("⠀⠀⠀⠀⠀⠀⠀⢸⡿⣗⡲⠶⠖⠋⣡⣯⡀⠀⠈⠉⠓⠒⠲⢶⣶⡖⠋⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⢀⡼⠁⡿⢯⠙⠛⠋⣹⡇⠙⠲⢤⣀⣀⡤⠖⢫⠏⠀⠀⠀⠀⠀")
    print("⠈⠙⠓⠶⢤⣴⣋⢀⣰⠃⠈⣿⡛⠉⣽⠙⠲⢤⡤⠞⢻⠀⢀⡏⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠈⢯⡙⢳⡲⢴⣇⣙⣄⣇⡤⠚⠉⡇⠀⢸⠀⢸⡇⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⣷⠀⣧⠀⣇⡼⢻⢿⡲⠤⣄⣧⠀⠸⡆⠈⣧⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⢠⡇⣠⣿⡊⠙⢦⡞⠀⠳⣴⠋⠉⢉⡷⠿⠤⣌⣦⡀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⣠⢾⣋⠁⠀⠙⢦⢸⡟⠉⠉⠙⣆⢠⠏⣠⠖⠋⠉⠉⠉⠓⠲⠤⡄")
    print("⠀⠀⣠⠖⠋⠁⠀⠈⠙⠦⡀⠈⣿⣠⠤⠴⠶⠾⢿⣠⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣆⡏⠀⠀⢀⣀⣀⣀⣻⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡷⠚⠉⠉⠁⠀⠀⠀⠙⣆⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⣼⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢧⡀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")

    print(f"{GRAY} ___  ____  ____  ____  ____  ____  ___      _    _  ____  ____ ")
    print("/ __)(  _ \\(_  _)(  _ \\( ___)(  _ \\/ __) ___( \\/\\/ )( ___)(  _ \\")
    print("\\__ \\ )___/ _)(_  )(_) ))__)  )   /\\__ \\(___))    (  )__)  ) _ <")
    print(f"(___/(__)  (____)(____/(____)(_)\\_)(___/    (__/\\__)(____)(____/{END}")

    print(f"\t\t\t\t{ORANGE}by IvoryCoding{END}\n\n")

if __name__ == '__main__':
    AsciiArt()
    connections_dict = {}

    # Create NetCat shell to listen on
    
    while True:
        try:
            usr_input = input(Cmd_prompt.prompt).strip()

            if usr_input == '':
                continue

            # Handle single/double quoted arguements
            single_quoted = re.findall("'{1}[\s\S]*'{1}", usr_input)
            double_quoted = re.findall('"{1}[\s\S]*"{1}', usr_input)
            quoted_args = single_quoted + double_quoted

            if len(quoted_args):
                for arg in quoted_args:
                    space_escaped = arg.replace(' ', Cmd_prompt.SPACE)

                    if (space_escaped[0] == "'" and space_escaped[-1] == "'") or (space_escaped[0] == '"' and space_escaped[-1] == '"'):
                        space_escaped = space_escaped[1:-1]
                    
                    usr_input = usr_input.replace(arg, space_escaped)

            # Create cmd-line args list
            usr_input = usr_input.split(' ')
            command_list = [w.replace(Cmd_prompt.SPACE, ' ') for w in usr_input if w]
            command_list_len = len(command_list)
            command = command_list[0].lower() if command_list else ''

            if command == 'help':
                if command_list_len == 1:
                    PromptHelp.print_small_help()
                elif command_list_len == 2:
                    PromptHelp.print_details_help(command_list[1])

            elif command == 'create':
                # Now check the list 1 for type of command (i.e. ssh, ftp, etc)
                if (command_list[1] == "ssh") and (command_list_len == 5):
                    #Format for how sessions are created:
                    # 1. Create a ssh connection
                    # 2. If established then create thread (for function to run commands)
                    #       - Create thread id, IP address, date created, Status
                    # 3. If suspend keys are pressed then move thread (session) to background

                    ssh_client = SSH.CreateSSH(command_list)

                    thread_ID = Base64Conversion.EncodeString(command_list)

                    conns_update = {thread_ID: [ssh_client, command_list[1], command_list[2], command_list[3], command_list[4]]}
                    connections_dict.update(conns_update)
                
                elif command_list[1] == "ftp":
                    print("ftp")

                elif command_list[1] == "python3":
                    print("Python Script")

                else: #Change this to check if varaible connection established or con_est is not true
                      # Else it is true and print success
                    print(f"\n{FAIL} {command_list[1]} session for {ORANGE}{command_list[2]}{END} failed to create.\n  Please check help or try again!\n\n")
                    continue

            elif command == 'save':
                print(f"\n[{ORANGE}Encrypting{END}] Saving data to a file.\n")
                try:
                    for key in connections_dict:
                        temp_client = connections_dict[key][0]
                        del connections_dict[key][0]
                    
                    EncDecFile.FileEncryption(connections_dict)

                    for key in connections_dict:
                        connections_dict[key].insert(0, temp_client)

                    print(f"{SUCCESS} Connections saved and file encrypted.")
                except:
                    print(f"{FAIL} Saving connections was not successful.")

            elif command == 'load':
                print(f"\n[{ORANGE}Loading{END}] Decrypting file and loading sessions.")

                try:
                    EncDecFile.FileDecryption(connections_dict)
                    print(f"{SUCCESS} All connections have been loaded.\n")
                except:
                    print(f"{FAIL} Loading connections was not successful.")

            elif command == 'delete':
                client = connections_dict[command_list[1]][0]
                # try: execpt: couldnt find connection ID. Use sessions to get ID. continue
                try:
                    if connections_dict[command_list[1]][1] == 'ssh':
                        SSH.CloseConnectionSSH(client)
                        # Remove the id and connection from the connections_dict
                        connections_dict.pop(command_list[1])

                        print(f"\n{SUCCESS} Connection was removed.\n")
                    # Else
                    #   Connection does not exist
                except:
                    print(f"{FAIL} Was not able to delete connection. Please Try Again!")

            elif command == 'sessions':
                print(f"\n[{ORANGE}Grabbing{END}] Checking connections!\n")
                # if connections ! empty then grab coonections

                try:
                    for key in connections_dict:
                        print(f"Session ID: {GREEN}{key}{END}")
                        print(f"Connection Type: {GRAY}{connections_dict[key][1]}{END}")
                        print(f"IP Address: {GRAY}{connections_dict[key][2]}{END}")
                        print(f"Username : {GRAY}{connections_dict[key][3]}{END}")
                        print(f"Password: {GRAY}{connections_dict[key][4]}{END}\n")

                    print(f"{SUCCESS} All sessions were grabbed and displayed.\n")
                except:
                    print(f"{FAIL} Could not grab session data. Please Try Again!")

            elif command == 'connect' and command_list_len == 2:
                print(f"\n[{ORANGE}Connecting{END}] Connecting to session.")

                try:
                    client = connections_dict[command_list[1]][0]
                    # try: execpt: couldnt find connection ID. Use sessions to get ID. continue
                    if connections_dict[command_list[1]][1] == 'ssh':
                        SSH.ExecuteCMDSSH(client, connections_dict[command_list[1]][2])
                    # Else
                    #   No connection with ID {ID} could be found.
                except:
                    print(f"{FAIL} Connection was not able to established. Please Try Again!")

            elif command == 'exit' or command == 'close':
                print(f"\n[{ORANGE}Closing{END}] All sessions in your SPIDER WEB will now close!")
                # Need to close each connection before exiting the program

                for key in connections_dict:
                    client = connections_dict[key][0]
                    SSH.CloseConnectionSSH(client)

                print(f"\n{SUCCESS} All sessions are now closed.")

                sys.exit(0)
            
            elif command == 'monitor' and command_list_len == 2:
                # This command needs to be developed
                # There will be a function that gets called to monitor the sessions
                print('Setup a monitor connection for listed sessions and or specific sessions')
                
                if command_list[1] == 'all':
                    print('will monitor all sessions')
                    print(connections_dict)
                    # for each key in connections_dict:
                    #   Create or use ssh client to monitor server
                else:
                    print('will monitor specific session')
                    # if session_id == key:
                    #   create or use ssh client to monitor server

            else:
                print(f"{FAIL} Command \"{command}\" was not found. Use the help command.")

        except KeyboardInterrupt:
            print(f"\n[{ORANGE}Closing{END}] All sessions in your SPIDER WEB will now close!")

            for key in connections_dict:
                    client = connections_dict[key][0]
                    SSH.CloseConnectionSSH(client)

            print(f"\n{SUCCESS} All sessions are now closed.")
            sys.exit(0)

# Need to do:
#   Error handling and try except statements
#   Handling of what connections are loaded ie if statements for ssh, elif ftp, etc.
#   Classes in core for ftp, and python scripts
#   Be more specific with why a command failed if it is a proper command (error handling)