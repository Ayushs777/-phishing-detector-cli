#!/bin/bash
# Uninstall Phishing Detector CLI

echo "Uninstalling Phishing Detector CLI..."
echo "Developer: Ayush Chaudhary | B.Tech IT"

sudo rm -f /usr/local/bin/phishdetect
sudo rm -f /usr/local/bin/phishdetect-sh
sudo rm -rf /opt/phishing-detector
rm -rf ~/.config/phishing-detector

echo "✅ Uninstallation complete!"