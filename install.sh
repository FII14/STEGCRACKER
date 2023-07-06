#!/bin/bash
# @ Script  : Instal stegcracker
# @ Pembuat : Rofi

g="\e[1;32m"
r="\e[0m"

chmod +x src/stegcracker

# Android (Termux)
if [[ $(uname -o) == "Android" ]]; then
    pkg update
    pkg install steghide
    pkg install python3
    pip3 install -r requirements.txt
    mv src/stegcracker /data/data/com.termux/files/usr/bin
    echo -e "${g}[•] ${r}Installation completed."
    echo -e "${g}[•] ${r}You can run it by executing the command 'stegcracker --help'"
    exit 0

# Linux Ubuntu dan Debian beserta keturunannya
elif [[ $(uname -o) == "GNU/Linux" ]]; then
    sudo apt-get update 
    sudo apt-get install steghide 
    sudo apt-get install python3-pip
    pip3 install -r requirements.txt 
    mv src/stegcracker /usr/bin
    echo -e "${g}[•] ${r}Installation completed."
    echo -e "${g}[•] ${r}You can run it by executing the command 'stegcracker --help'"
    exit 0
fi
