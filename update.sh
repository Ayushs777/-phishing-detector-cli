#!/bin/bash
# Update Phishing Detector CLI

echo "Updating Phishing Detector CLI..."
cd /opt/phishing-detector
sudo git pull origin main
sudo pip3 install -r requirements.txt --upgrade
echo "✅ Update completed!"