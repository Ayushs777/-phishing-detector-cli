#!/usr/bin/env python3
"""
===============================================================================
🛡️  PHISHING URL DETECTOR - CLI TOOL
Version: 2.0.0 | Developer: Ayush Chaudhary (B.Tech IT)
===============================================================================
"""

import sys
import re
import requests
import json
import argparse
from datetime import datetime
from urllib.parse import urlparse
import time
import os

class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

DEVELOPER_INFO = {
    "name": "Ayush Chaudhary",
    "qualification": "B.Tech Information Technology",
    "github": "github.com/ayushchaudhary-it",
    "version": "2.0.0"
}

API_KEY = "AIzaSyB7RWWslgozNptNtUjVg63DAXujdP2Btuw"

def print_developer_banner():
    banner = f"""
    {Colors.BLUE}{Colors.BOLD}
    ╔═══════════════════════════════════════════════════════════╗
    ║                                                           ║
    ║  🛡️  PHISHING URL DETECTOR - CLI TOOL                   ║
    ║  Professional Cybersecurity Utility                       ║
    ║                                                           ║
    ║  👨‍💻 DEVELOPER: {DEVELOPER_INFO['name']:<20}             ║
    ║  🎓 QUALIFICATION: {DEVELOPER_INFO['qualification']:<15} ║
    ║  📦 VERSION: v{DEVELOPER_INFO['version']:<25}           ║
    ║  📄 LICENSE: MIT License                                 ║
    ║                                                           ║
    ╚═══════════════════════════════════════════════════════════╝
    {Colors.END}
    """
    print(banner)

def check_url_with_google(url):
    try:
        api_url = f"https://safebrowsing.googleapis.com/v4/threatMatches:find?key={API_KEY}"
        payload = {
            "client": {"clientId": "phishing-detector", "clientVersion": "2.0.0"},
            "threatInfo": {
                "threatTypes": ["MALWARE", "SOCIAL_ENGINEERING"],
                "platformTypes": ["ANY_PLATFORM"],
                "threatEntryTypes": ["URL"],
                "threatEntries": [{"url": url}]
            }
        }
        response = requests.post(api_url, json=payload, timeout=10)
        return response.json() if response.status_code == 200 else None
    except:
        return None

def local_url_analysis(url):
    score = 100
    warnings = []
    url_lower = url.lower()
    
    try:
        domain = urlparse(url).netloc
    except:
        domain = url_lower.split('/')[0]
    
    if not url_lower.startswith('https://'):
        score -= 30
        warnings.append("No HTTPS")
    
    if any(tld in domain for tld in ['.xyz', '.top', '.gq', '.ml', '.tk']):
        score -= 25
        warnings.append("Suspicious domain")
    
    if re.search(r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b', url_lower):
        score -= 40
        warnings.append("Uses IP address")
    
    if '@' in url_lower:
        score -= 35
        warnings.append("Contains @ symbol")
    
    if len(url_lower) > 100:
        score -= 20
        warnings.append(f"Very long URL ({len(url_lower)} chars)")
    
    score = max(0, min(100, score))
    return {"score": score, "warnings": warnings, "domain": domain}

def print_result(url, google_result, local_result):
    print(f"\n{Colors.CYAN}{'='*60}{Colors.END}")
    print(f"{Colors.BOLD}📊 ANALYSIS REPORT - {DEVELOPER_INFO['name']}{Colors.END}")
    print(f"{Colors.CYAN}{'='*60}{Colors.END}")
    
    print(f"{Colors.YELLOW}👨‍💻 Developer:{Colors.END} {DEVELOPER_INFO['name']}")
    print(f"{Colors.YELLOW}🔗 URL:{Colors.END} {url}")
    print(f"{Colors.YELLOW}🌐 Domain:{Colors.END} {local_result['domain']}")
    
    if google_result and google_result.get('matches'):
        print(f"\n{Colors.RED}🚨 GOOGLE SAFE BROWSING - THREAT DETECTED!{Colors.END}")
    
    score = local_result['score']
    if score >= 80:
        status_color = Colors.GREEN
        status = "✅ SAFE"
    elif score >= 50:
        status_color = Colors.YELLOW
        status = "⚠️ SUSPICIOUS"
    else:
        status_color = Colors.RED
        status = "🚨 DANGEROUS"
    
    print(f"\n{Colors.BOLD}Security Score:{Colors.END} {status_color}{score}/100{Colors.END}")
    print(f"{Colors.BOLD}Status:{Colors.END} {status_color}{status}{Colors.END}")
    
    if local_result['warnings']:
        print(f"\n{Colors.YELLOW}⚠️  Warnings:{Colors.END}")
        for warning in local_result['warnings']:
            print(f"  • {warning}")
    
    print(f"\n{Colors.MAGENTA}Tool by: {DEVELOPER_INFO['name']} | {DEVELOPER_INFO['qualification']}{Colors.END}")
    print(f"{Colors.CYAN}{'='*60}{Colors.END}")

def main():
    parser = argparse.ArgumentParser(description=f'Phishing Detector by {DEVELOPER_INFO["name"]}')
    parser.add_argument('-u', '--url', help='URL to scan')
    parser.add_argument('-f', '--file', help='File with URLs')
    parser.add_argument('-i', '--interactive', action='store_true', help='Interactive mode')
    parser.add_argument('-v', '--version', action='store_true', help='Show version')
    parser.add_argument('-d', '--developer', action='store_true', help='Show developer info')
    
    args = parser.parse_args()
    
    if args.version or args.developer:
        print_developer_banner()
        return
    
    if args.interactive:
        print_developer_banner()
        while True:
            url = input(f"\n{Colors.CYAN}[?] URL (or 'quit'): {Colors.END}").strip()
            if url.lower() in ['quit', 'exit', 'q']:
                break
            if url:
                result = local_url_analysis(url)
                print_result(url, None, result)
    elif args.url:
        print_developer_banner()
        google_result = check_url_with_google(args.url)
        local_result = local_url_analysis(args.url)
        print_result(args.url, google_result, local_result)
    else:
        print_developer_banner()
        parser.print_help()

if __name__ == "__main__":
    main()