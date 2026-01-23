#!/usr/bin/env python3
"""
PHISHING DETECTOR - KALI LINUX
Single file, no external packages needed
Developer: Ayush Chaudhary | B.Tech IT
"""

import sys
import re

def print_banner():
    print("""
╔══════════════════════════════════════════════╗
║        PHISHING URL DETECTOR                ║
║        Kali Linux Edition                   ║
║        Developer: Ayush Chaudhary           ║
║        B.Tech Information Technology        ║
╚══════════════════════════════════════════════╝
""")

def check_url(url):
    score = 100
    warnings = []
    good_points = []
    
    # 1. HTTPS check
    if url.startswith('https://'):
        score += 10
        good_points.append("✅ Uses HTTPS (Secure)")
    else:
        score -= 30
        warnings.append("❌ No HTTPS (Not secure)")
    
    # 2. Get domain
    try:
        if '://' in url:
            domain = url.split('://')[1].split('/')[0]
        else:
            domain = url.split('/')[0]
    except:
        domain = url
    
    # 3. Bad TLDs check
    bad_domains = ['.xyz', '.top', '.gq', '.ml', '.tk', '.cf', '.ga', '.men', '.loan']
    for bad in bad_domains:
        if bad in domain:
            score -= 25
            warnings.append(f"⚠️ Suspicious domain ({bad})")
            break
    
    # 4. IP address check
    if re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', url):
        score -= 40
        warnings.append("❌ Uses IP address")
    
    # 5. @ symbol check
    if '@' in url:
        score -= 35
        warnings.append("❌ Contains @ symbol (phishing trick)")
    
    # 6. Brand impersonation
    brands = ['facebook', 'paypal', 'amazon', 'google', 'instagram', 'whatsapp', 'netflix']
    brand_found = False
    for brand in brands:
        if brand in url.lower():
            brand_found = True
            break
    
    if brand_found and any(bad in domain for bad in bad_domains):
        score -= 50
        warnings.append("🚨 BRAND IMPERSONATION DETECTED!")
    
    # 7. URL length
    if len(url) > 100:
        score -= 20
        warnings.append(f"⚠️ Very long URL ({len(url)} chars)")
    
    # 8. Hyphen count
    if url.count('-') > 4:
        score -= 15
        warnings.append(f"⚠️ Too many hyphens ({url.count('-')})")
    
    # 9. Phishing keywords
    bad_words = ['login', 'signin', 'verify', 'secure', 'account', 'password', 'banking', 'update']
    found_words = []
    for word in bad_words:
        if word in url.lower():
            found_words.append(word)
    
    if len(found_words) > 2:
        score -= len(found_words) * 8
        warnings.append(f"⚠️ Phishing keywords: {', '.join(found_words)}")
    
    # Ensure score between 0-100
    score = max(0, min(100, score))
    
    return score, warnings, good_points

def print_result(url, score, warnings, good_points):
    print(f"\n{'='*60}")
    print(f"🔗 URL: {url}")
    print(f"📊 SECURITY SCORE: {score}/100")
    print(f"{'='*60}")
    
    if score >= 80:
        print("✅ STATUS: SAFE TO USE")
    elif score >= 50:
        print("⚠️  STATUS: BE CAUTIOUS")
    else:
        print("🚨 STATUS: DANGEROUS - DO NOT VISIT!")
    
    if good_points:
        print("\n👍 GOOD SIGNS:")
        for point in good_points:
            print(f"  {point}")
    
    if warnings:
        print("\n👎 SECURITY WARNINGS:")
        for warning in warnings:
            print(f"  {warning}")
    
    print(f"\n{'='*60}")
    print("👨‍💻 Developer: Ayush Chaudhary")
    print("🎓 B.Tech Information Technology")
    print(f"{'='*60}")

def main():
    if len(sys.argv) == 1:
        # Interactive mode
        print_banner()
        print("📝 Enter URLs to scan (type 'quit' to exit):")
        
        while True:
            print("\n" + "-"*40)
            url = input("Enter URL: ").strip()
            
            if url.lower() in ['quit', 'exit', 'q']:
                print("\n👋 Thank you for using Phishing Detector!")
                break
            
            if not url:
                continue
            
            print("⏳ Scanning...")
            score, warnings, good_points = check_url(url)
            print_result(url, score, warnings, good_points)
    
    elif sys.argv[1] in ['-h', '--help']:
        print_banner()
        print("""
Usage:
  python3 phishing-detector.py                    # Interactive mode
  python3 phishing-detector.py <url>             # Scan single URL
  python3 phishing-detector.py --developer       # Show developer info
  
Examples:
  python3 phishing-detector.py https://google.com
  python3 phishing-detector.py http://fake-facebook.xyz
        """)
    
    elif sys.argv[1] == '--developer':
        print_banner()
        print("""
Developer Information:
👨‍💻 Name: Ayush Chaudhary
🎓 Qualification: B.Tech Information Technology
📧 Email: ayush.chaudhary@example.com
🔧 Tool: Phishing URL Detector
🚀 Version: 2.0.0
📄 License: MIT
        """)
    
    else:
        # Single URL scan
        print_banner()
        url = sys.argv[1]
        print(f"⏳ Scanning: {url}")
        score, warnings, good_points = check_url(url)
        print_result(url, score, warnings, good_points)

if __name__ == "__main__":
    main()