# STEGCRACKER

![GitHub repo size](https://img.shields.io/github/repo-size/Fii14/STEGCRACKER?style=flat-square)
[![GitHub last commit](https://img.shields.io/github/last-commit/Fii14/STEGCRACKER?style=flat-square)](https://github.com/Fii14/STEGCRACKER/commits/main)
![GitHub contributors](https://img.shields.io/github/contributors/FII14/STEGCRACKER?style=flat-square)
[![GitHub license](https://img.shields.io/github/license/Fii14/STEGCRACKER?style=flat-square)](https://github.com/Fii14/STEGCRACKER/blob/main/LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/Fii14/STEGCRACKER?style=flat-square)](https://github.com/Fii14/STEGCRACKER/stargazers)

![Steghide Password Cracker](https://github.com/FII14/STEGCRACKER/blob/main/39cc597bb65662ee9a8e7c96fa777ade.jpg)

## Description
This Python program cracks steghide file passwords using a wordlist. It utilizes the steghide command-line tool to extract information from steghide files by attempting different passwords from the specified wordlist.

## Prerequisites
- Python 3.x
- Steghide

## Install
```
$ git clone https://github.com/FII14/STEGCRACKER.git

$ cd STEGCRACKER

$ pip3 install -r requirements.txt

$ python3 stegcracker.py --help
```

## Usage
```
python3 stegcracker.py -f path/to/steghide_file -w path/to/wordlist_file
```

Replace `path/to/steghide_file` with the actual path to your steghide file and `path/to/wordlist` with the actual path to your wordlist file.

Wait for the program to finish. It will iterate through each password in the wordlist and attempt to extract information from the steghide file using the password. If a matching password is found, it will be displayed. If no matching password is found, a message will be shown.

## Disclaimer
Please remember that the use of Steghide to crack steghide files should be done with proper permission and only for legitimate purposes. Do not use this tool for illegal activities or without the necessary authorization.
