# GPIOShortcuts
A Raspberry Pi service to permanently map GPIO button presses to keyboard shortcuts.

## Installation
1. Clone repo and enter directory.

    `git clone https://github.com/benstobbs/GPIOShortcuts/`

    `cd GPIOShortcuts`

2. Edit config file to configure your shortcuts. Buttons should be connected to GND on one side and directly to the GPIO pin on the other.

    `nano config.txt`

3. Make installation script executable and install.

    `chmod +x install.sh`

    `./install.sh`

4. Make sure service is up and running.

    `sudo systemctl status GPIOShortcuts`

5. Done!

## Updating configuration
To update the configuration, just change the cloned `config.txt` and re-run `config.sh` .