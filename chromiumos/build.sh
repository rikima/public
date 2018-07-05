#!/usr/bin/env bash
sudo apt-get update
sudo apt-get install -y git-core gitk git-gui subversion curl lvm2 thin-provisioning-tools python-pkg-resources python-virtualenv expect
git clone https://chromium.googlesource.com/chromium/tools/depot_tools.git
export PATH=$PATH:$PWD/depot_tools
git config --global user.email "you@example.com"
git config --global user.name "Your Name"
(
echo '#!/bin/sh';
echo 'echo Defaults \!tty_tickets > $1';
echo 'echo Defaults timestamp_timeout=180 >> $1';
) > sudo_editor
chmod +x ./sudo_editor
sudo EDITOR=./sudo_editor visudo -f /etc/sudoers.d/relax_requirements
expect -c "
set timeout -1
spawn repo init -u https://chromium.googlesource.com/chromiumos/manifest.git
expect \"Enable color display in this user account (y/N)?\"
send \"y\n\"
"
repo sync
export BOARD=amd64-generic
cros_sdk -- ./build_packages --board=${BOARD}
cros_sdk -- ./build_image --board=${BOARD}
cros_sdk -- cros flash --board=${BOARD} file:///home/ubuntu/chromiumos.iso
