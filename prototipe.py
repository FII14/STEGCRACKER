#!/usr/bin/env python3

import os
import time
import argparse
import subprocess
from colorama import Fore
from datetime import datetime

g = Fore.LIGHTGREEN_EX
r = Fore.LIGHTRED_EX
p = Fore.RESET
b = Fore.LIGHTBLUE_EX
c = Fore.CYAN
gb = Fore.GREEN
pb = Fore.LIGHTWHITE_EX

os.system("clear")

print(f"""{b}
     _                                 _
 ___| |_ ___  __ _  ___ _ __ __ _  ___| | _____ _ __
/ __| __/ _ \/ _` |/ __| '__/ _` |/ __| |/ / _ \ '__|
\__ \ ||  __/ (_| | (__| | | (_| | (__|   <  __/ |
|___/\__\___|\__, |\___|_|  \__,_|\___|_|\_\___|_|
             |___/
{p}""")

# Mencoba kata sandi file steghide menggunakan wordlist
parser = argparse.ArgumentParser(description='Crack the steghide file password.')
parser.add_argument('-f', '--file', help='Path to steghide file', required=True)
parser.add_argument('-w', '--wordlist', help='Path to wordlist', required=True)
args = parser.parse_args()

try:
    # Mengecek keberadaan file steghide
    with open(args.file):
        pass
except FileNotFoundError:
    print(f"{r}[-] {p}Error: Steghide file '{args.file}' not found.\n")
    exit(1)

try:
    # Mengecek keberadaan file wordlist
    with open(args.wordlist):
        pass
except FileNotFoundError:
    print(f"{r}[-] {p}Error: Wordlist file '{args.wordlist}' not found.\n")
    exit(1)

try:
    now = datetime.now()
    print(f"{r}[!] {p}Please remember that the use of Steghide to crack steghide files should be done with proper permission and only for legitimate purposes. Do not use this tool for illegal activities or without the necessary authorization.\n")
    time.sleep(7)
    print(f"{p}[*] Starting @ {now.strftime('%H:%M:%S %d/%m/%Y')}\n")
    time.sleep(3)

    # Melakukan iterasi pada setiap kata sandi dalam wordlist
    with open(args.wordlist, 'r') as wordlist_file:
        for line in wordlist_file:
            now = datetime.now()
            password = line.strip()
            command = ['steghide', 'extract', '-sf', args.file, '-p', password, '-f']
            result = subprocess.run(command, capture_output=True, text=True)

            if result.returncode == 0:
                print(f"{p}[{c}{now.strftime('%H:%M:%S')}{p}] [{g}INFO{p}] {pb}Password found: {g}{password}{p}")
                cracked_file = f"{args.file}.out"
                command_s = ['steghide', 'extract', '-sf', args.file, '-p', password, '-xf', cracked_file]
                subprocess.run(command_s, capture_output=True, text=True)
                print(f"{p}[{c}{now.strftime('%H:%M:%S')}{p}] [{g}INFO{p}] {pb}Cracked file saved as: {g}{cracked_file}{p}")
                break
            else:
                print(f"{p}[{c}{now.strftime('%H:%M:%S')}{p}] [{gb}INFO{p}] {p}Incorrect password: {r}{password}{p}")

        else:
            print(f"\n{r}[-] {p}No matching password found in the wordlist.")

    print(f"\n{p}[*] Ending @ {datetime.now().strftime('%H:%M:%S %d/%m/%Y')}")

except Exception as e:
    print(f"{r}[-] {p}An error occurred: {str(e)}")
