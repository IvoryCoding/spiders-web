#! /usr/bin/env python3

import sys, string, os, re
import paramiko
import base64
import ast
import json
from threading import Thread
from ipaddress import ip_address
from string import ascii_uppercase, ascii_lowercase, digits
from cryptography.fernet import Fernet

# Add colours to use for a custom experience
GRAY = '\001\033[38;5;246m\002'
END = '\001\033[0m\002'
GREEN = '\001\033[38;5;82m\002'
ORANGE = '\033[0;38;5;202m\002'
RED = '\001\033[1;31m\002'
MAIN = '\001\033[38;5;85m\002'
LRED = '\033[0;38;5;202m\002'

# Prefixes
SUCCESS = f'[{GREEN}SUCCESS{END}]'
WARN = f'[{ORANGE}WARNING{END}]'
FAIL = f'[{RED}FAILED{END}]'

class Cmd_prompt:
    original_prompt = prompt = f"{MAIN}Spiders-Web >{END} "
    SPACE = '#>SPACE$<#'

class PromptHelp:
    commands = {

        'help' : {
            'details' : f'''
            \r  Really ?
            \r  Displays basic help information or detailed help.

            \r  Command Usage
            \r  --------------------------------------------------
            \r  help
            \r  \t\tor
            \r  help <command>
            ''',
            'min_args' : 0,
            'max_args' : 1
        },

        'create' : {
            'details' : f'''
            \r  Create a custom session with commands.
            \r  Allowing you to create sessions for ssh, ftp, wget, etc.
            \r  ALL SUPPORTED SESSIONS ARE LISTED BELOW. SEE SUPPORTS
            
            \r                    Supports
            \r      ------------------------------------
            \r      |   SSH         FTP         WGET   |
            \r      |   Python Scripts          NetCat |
            \r      ------------------------------------

            \r  Command Usage
            \r  --------------------------------------------------
            \r  create ssh <ip> <username> <password>
            \r  \t\tor
            \r  create ftp <ip> <username> <password>
            ''',
            'min_args' : 2,
            'max_args' : 4
        },

        'save' : {
            'details' : f'''
            \r  Creates a encrypted file with the information used to create
            \r  each session. Allowing you to quickly recreate previous sessions.

            \r  Command Usage
            \r  --------------------------------------------------
            \r  save <filename.extension> <encryption password>
            ''',
            'min_args' : 4,
            'max_args' : 4
        },

        'load' : {
            'details' : f'''
            \r  Loads an encrypted file with information previously used.
            \r  Allowing you to quickly recreate previous sessions.

            \r  Command Usage
            \r  --------------------------------------------------
            \r  load <filename.extension> <encryption password>
            ''',
            'min_args' : 4,
            'max_args' : 4
        },

        'exit' : {
            'details' : f'''
            \r  Closes the program and terminates any running sessions.

            \r  Command Usage
            \r  --------------------------------------------------
            \r  exit
            \r  \t\t or
            \r  close
            ''',
            'min_args' : 0,
            'max_args' : 0
        },

        'delete' : {
            'details' : f'''
            \r  Deletes a session that was created.
            \r  Takes only one arguement that is the session ID you wish to close.

            \r  Command Usage
            \r  --------------------------------------------------
            \r  delete <session ID>
            ''',
            'min_args' : 1,
            'max_args' : 1
        },

        'sessions' : {
            'details' : f'''
            \r  Displays all currently active sessions.
            \r  Displays session information: ID, User, IP Address, etc.

            \r  Command Usage
            \r  --------------------------------------------------
            \r  sessions
            ''',
            'min_args' : 0,
            'max_args' : 1
        },

        'connect' : {
            'details' : f'''
            \r  Connects to the thread that holds the session.
            \r  Allows you to interact with the session.

            \r  Command Usage
            \r  --------------------------------------------------
            \r  connect <session ID>
            ''',
            'min_args' : 0,
            'max_args' : 1
        },

        'monitor' : {
            'details' : f'''
            \r  Connects to the thread that holds the session.
            \r  Will monitor and send alerts for suspicious activity.

            \r  Command Usage
            \r  --------------------------------------------------
            \r  monitor <ip address>
            ''',
            'min_args' : 0,
            'max_args' : 1
        },

        #Do this for all of the commands

    }

    def print_small_help():
        print(
            f'''
            \r  Command             Decsription
            \r  --------------------------------------------------
            \r  help        [+]     Print this message.
            \r  create      [+]     Create custom sessions.
            \r  save        [+]     Saves all session data.
            \r  load        [+]     Loads saved session data.
            \r  delete      [+]     Deletes a session.
            \r  sessions            Lists all sessions.
            \r  connect     [+]     Connects to the session.
            \r  monitor     [+]     Monitors connected server.
            \r  exit                Closes the application.

            \r Commands with [+] may take additional arguements.
            \r For details use: help <COMMAND>
            '''
        )

    def print_details_help(cmd):
        print(PromptHelp.commands[cmd]['details']) if cmd in PromptHelp.commands.keys() else print(f'{FAIL} No details for command "{cmd}".')

class SSH:
    def CreateSSH(command_list):
        host = command_list[2]
        username = command_list[3]
        password = command_list[4]

        print(f"\n[{LRED}CONNECTING{END}] Trying the information provided:")
        print(f" Connection:\t\tSSH")
        print(f" Host:\t\t\t{host}")
        print(f" Username:\t\t{username}")
        print(f" Password:\t\t{password}\n")

        try:
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(host, username=username, password=password)
            #client.close()

            print(f"{SUCCESS} Connection to {command_list[1]} successful.")
            print(f"  Type {GREEN}pause{END} to suspend session while in one.\n")
        except:
            print(f"{FAIL} IP, Password, or Username is wrong.\n  Connection was not established.")

        return client
    
    def ExecuteCMDSSH(client, ip):
        print(f"\n{SUCCESS} Connection established.\n")
        while True:
            cmd = input(f"{GREEN}{ip}/SSH>{END} ")

            if cmd != "pause":
                _stdin, _stdout, _stderr = client.exec_command(cmd)
                print(_stdout.read().decode())
            else:
                print()
                break

    def CloseConnectionSSH(client):
        client.close()

class Base64Conversion:
    def EncodeString(command_list):
        raw_string = f"{command_list[2]}{command_list[3]}{command_list[4]}".encode("ascii")
        base64_string = base64.b64encode(raw_string).decode("ascii")

        raw_classifier = f"{command_list[1]}".encode("ascii")
        base64_classifier = base64.b64encode(raw_classifier).decode("ascii")

        encoded_string = f"{base64_classifier}-{base64_string}"

        return encoded_string

class EncDecFile():

    def FileEncryption(data): # Add data_filename, and key_filename
        key = Fernet.generate_key()

        with open('enc_key.key', 'wb') as file:
            file.write(key)

        fernet = Fernet(key)
        encrypted = fernet.encrypt(json.dumps(data).encode())
        with open('saved_data.txt', 'wb') as file:
            file.write(encrypted)

    def FileDecryption(connections_dict): # Add data_filename, and key_filename
        with open('enc_key.key', 'rb') as file:
            key = file.read()

        fernet = Fernet(key)
        with open('saved_data.txt', 'rb') as file:
            data = json.loads(fernet.decrypt(file.read()))

        for key in data:
            command_list = ["create", data[key][0], data[key][1], data[key][2], data[key][3]]
            ssh_client = SSH.CreateSSH(command_list)

            thread_ID = Base64Conversion.EncodeString(command_list)

            conns_update = {thread_ID: [ssh_client, command_list[1], command_list[2], command_list[3], command_list[4]]}
            connections_dict.update(conns_update)
