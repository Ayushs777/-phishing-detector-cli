# Create PDF from markdown
echo "# Phishing Detector CLI Manual
## Developer: Ayush Chaudhary
## Qualification: B.Tech Information Technology

### Installation
1. Clone repository
2. Run install.sh
3. Use phishdetect command

### Usage
- phishdetect -u URL
- phishdetect -i
- phishdetect --developer

### Support
Email: ayush.chaudhary@example.com
GitHub: github.com/ayushchaudhary-it
" > manual.md

# Convert to PDF (if pandoc installed)
# pandoc manual.md -o docs/manual.pdf