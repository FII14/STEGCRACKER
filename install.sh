sudo apt-get update -y
sudo apt-get install steghide -y
sudo apt-get install python3-pip -y
sudo apt-get install wordlists
gzip -d /usr/share/wordlists/rockyou.txt
pip3 install -r requirements.txt
sudo chmod +x stegcracker
sudo mv stegcracker /usr/bin
stegcracker --help
