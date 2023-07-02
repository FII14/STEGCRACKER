sudo apt-get update -y
sudi apt-get install steghide -y
sudo apt-get install python3-pip -y
pip3 install -r requirements.txt
sudo chmod +x stegcracker
sudo mv stegcracker /usr/bin
stegcracker --help
