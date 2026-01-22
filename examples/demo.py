#!/usr/bin/env python3
"""
Demo script for Phishing Detector CLI
Developer: Ayush Chaudhary | B.Tech IT
"""

import subprocess
import time

def run_demo():
    print("🛡️ Phishing Detector CLI Demo")
    print("Developer: Ayush Chaudhary | B.Tech IT\n")
    
    urls = [
        "https://www.google.com",
        "http://facebook-login-secure.xyz",
        "http://paypal-update-account.gq"
    ]
    
    for url in urls:
        print(f"\n{'='*50}")
        print(f"Testing: {url}")
        print('='*50)
        
        try:
            result = subprocess.run(
                ['phishdetect', '-u', url],
                capture_output=True,
                text=True,
                timeout=10
            )
            print(result.stdout)
        except:
            print("Error running scan")
        
        time.sleep(2)
    
    print("\n✅ Demo completed!")
    print("👨‍💻 Developer: Ayush Chaudhary")
    print("🎓 B.Tech Information Technology")

if __name__ == "__main__":
    run_demo()