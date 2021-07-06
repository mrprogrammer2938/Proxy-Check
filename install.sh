#!/usr/bin/env bash
# This code write by Mr.nope
# Proxy-Check 1.2.0

if [[ "$(id -u)" -ne 0 ]]; then
  echo "Please, Run This programm as Root!"
  echo ""
  exit 1
fi
clear
echo "Installing..."
sleep 2
chmod +x check.py
apt update
apt upgrade
apt install python
apt install python3
apt install python3-pip
pip3 install --upgrade pip
echo ""
echo "Installing..., Finish...!"
echo ""
exit 1