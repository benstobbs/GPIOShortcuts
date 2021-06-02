#!/bin/bash
if [[ "$EUID" = 0 ]]; then
    echo "Already root"
else
    sudo -k
    if sudo true; then
        echo "Sucessfully got root"
    else
        echo "Wrong password"
        exit 1
    fi
fi

sudo pip install pyautogui

sudo mkdir /etc/GPIOShortcuts
sudo cp config.txt /etc/GPIOShortcuts/
sudo cp service.py /etc/GPIOShortcuts/
sudo cp GPIOShortcuts.service /lib/systemd/system/
sudo chmod 644 /lib/systemd/system/GPIOShortcuts.service
sudo chmod +x /etc/GPIOShortcuts/service.py

sudo systemctl daemon-reload
sudo systemctl enable GPIOShortcuts.service
sudo systemctl start GPIOShortcuts.service

echo "Done"