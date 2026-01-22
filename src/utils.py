"""
Utility functions for Phishing Detector
Developer: Ayush Chaudhary | B.Tech IT
"""

def get_developer_info():
    return {
        "name": "Ayush Chaudhary",
        "qualification": "B.Tech Information Technology",
        "version": "2.0.0"
    }

def print_colored(text, color_code):
    """Print colored text"""
    colors = {
        'red': '\033[91m',
        'green': '\033[92m',
        'yellow': '\033[93m',
        'blue': '\033[94m',
        'end': '\033[0m'
    }
    return f"{colors.get(color_code, '')}{text}{colors['end']}"