#!/bin/bash
# Phishing Detector - Bash Version
# Developer: Ayush Chaudhary | B.Tech IT

RED='\033[0;31m'; GREEN='\033[0;32m'; YELLOW='\033[1;33m'
BLUE='\033[0;34m'; CYAN='\033[0;36m'; NC='\033[0m'

print_banner() {
    echo -e "${BLUE}"
    echo "┌────────────────────────────────────────────────┐"
    echo "│     PHISHING DETECTOR - Bash CLI               │"
    echo "│     Developer: Ayush Chaudhary                 │"
    echo "│     B.Tech Information Technology              │"
    echo "└────────────────────────────────────────────────┘"
    echo -e "${NC}"
}

check_url() {
    url="$1"
    echo -e "\n${CYAN}[*] Analyzing: $url${NC}"
    
    score=100
    warnings=()
    
    if [[ ! "$url" =~ ^https:// ]]; then
        ((score -= 30))
        warnings+=("No HTTPS")
    fi
    
    if [[ "$url" =~ \.(xyz|top|gq|ml|tk)$ ]]; then
        ((score -= 25))
        warnings+=("Suspicious TLD")
    fi
    
    if [[ "$url" =~ [0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3} ]]; then
        ((score -= 40))
        warnings+=("Uses IP")
    fi
    
    if [ $score -ge 80 ]; then
        echo -e "${GREEN}[+] SAFE ($score/100)${NC}"
    elif [ $score -ge 50 ]; then
        echo -e "${YELLOW}[!] SUSPICIOUS ($score/100)${NC}"
    else
        echo -e "${RED}[-] DANGEROUS ($score/100)${NC}"
    fi
    
    if [ ${#warnings[@]} -gt 0 ]; then
        echo -e "${YELLOW}⚠️  Warnings:${NC}"
        for w in "${warnings[@]}"; do echo "  • $w"; done
    fi
}

# Main
print_banner
if [ $# -eq 0 ]; then
    echo "Usage: $0 <url1> <url2> ..."
    echo "Example: $0 \"http://test.com\""
    exit 1
fi

for url in "$@"; do
    check_url "$url"
done