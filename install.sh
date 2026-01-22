#!/bin/bash
# Phishing Detector CLI Installer
# Developer: Ayush Chaudhary | B.Tech IT

set -e

RED='\033[0;31m'; GREEN='\033[0;32m'; YELLOW='\033[1;33m'
BLUE='\033[0;34m'; NC='\033[0m'

print_header() {
    clear
    echo -e "${BLUE}"
    echo "╔══════════════════════════════════════════════════╗"
    echo "║      PHISHING DETECTOR CLI INSTALLATION          ║"
    echo "║      Developer: Ayush Chaudhary (B.Tech IT)      ║"
    echo "╚══════════════════════════════════════════════════╝"
    echo -e "${NC}"
}

main() {
    print_header
    
    echo -e "${YELLOW}[*] Checking dependencies...${NC}"
    
    # Check Python
    if ! command -v python3 &> /dev/null; then
        echo -e "${RED}[!] Python3 not found. Installing...${NC}"
        sudo apt update && sudo apt install -y python3 python3-pip
    fi
    
    echo -e "${GREEN}[✓] Python3 installed${NC}"
    
    # Install Python packages
    echo -e "${YELLOW}[*] Installing Python packages...${NC}"
    pip3 install requests
    
    # Create directories
    echo -e "${YELLOW}[*] Setting up directories...${NC}"
    sudo mkdir -p /opt/phishing-detector
    sudo cp -r src/* /opt/phishing-detector/
    
    # Make executable
    sudo chmod +x /opt/phishing-detector/phishdetect.py
    sudo chmod +x /opt/phishing-detector/phishdetect.sh
    
    # Create symlinks
    sudo ln -sf /opt/phishing-detector/phishdetect.py /usr/local/bin/phishdetect
    sudo ln -sf /opt/phishing-detector/phishdetect.sh /usr/local/bin/phishdetect-sh
    
    # Create config
    mkdir -p ~/.config/phishing-detector
    cat > ~/.config/phishing-detector/config.json << EOF
{
    "developer": "Ayush Chaudhary",
    "qualification": "B.Tech Information Technology",
    "version": "2.0.0"
}
EOF
    
    echo -e "${GREEN}"
    echo "══════════════════════════════════════════════════"
    echo "   ✅ INSTALLATION COMPLETED SUCCESSFULLY!"
    echo "══════════════════════════════════════════════════"
    echo -e "${NC}"
    
    echo -e "${YELLOW}Usage examples:${NC}"
    echo "  phishdetect -u \"http://example.com\""
    echo "  phishdetect -i (interactive mode)"
    echo "  phishdetect --developer"
    echo ""
    echo -e "${BLUE}Developer: Ayush Chaudhary | B.Tech IT${NC}"
}

main