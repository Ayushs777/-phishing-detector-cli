#!/usr/bin/env python3
"""
Test script for Phishing Detector
Developer: Ayush Chaudhary | B.Tech IT
"""

import unittest
from src.phishdetect import local_url_analysis

class TestPhishingDetector(unittest.TestCase):
    def test_safe_url(self):
        result = local_url_analysis("https://www.google.com")
        self.assertGreaterEqual(result['score'], 80)
    
    def test_phishing_url(self):
        result = local_url_analysis("http://facebook-login-secure.xyz")
        self.assertLess(result['score'], 50)
    
    def test_ip_url(self):
        result = local_url_analysis("http://192.168.1.1/login.php")
        self.assertLess(result['score'], 60)

if __name__ == "__main__":
    print("Running tests...")
    print("Developer: Ayush Chaudhary | B.Tech IT")
    unittest.main()