#!/bin/bash
# @ Script  : Instal stegcracker
# @ Pembuat : Rofi

sudo chmod +x stegcracker

# Android 
if [[ $(uname -o == "Android") ]];
    pkg update
    pkg install steghide
    pkg install python3
    pip3 install -r requirements.txt
    mv stegcracker /data/data/com.termux/files/usr/bin
    echo "[•] Installation completed."
    echo "[•] You can run it by executing the command 'stegcracker --help'"
    exit 0

# Linux Ubuntu dan Debian beserta keturunannya
elif [[ $(uname -o == "Linux") ]]; then
    sudo apt-get update
    sudo apt-get install steghide
    sudo apt-get install python3-pip
    pip3 install -r requirements.txt
    mv stegcracker /usr/bin
    echo "[•] Installation completed."
    echo "[•] You can run it by executing the command 'stegcracker --help'"
    exit 0
fi
