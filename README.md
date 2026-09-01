# 1212p Smart Scanner 🚀

Hey there! 👋 Just a quick heads-up: I'm a cybersecurity student and a complete beginner when it comes to coding. **This is actually the very first script I have ever designed and built!** I'm learning as I go, so any feedback, tips, or pull requests are more than welcome.

I built this tool because I got tired of manually running Nmap, waiting forever, and then realizing the target doesn't even have a web server running. 

**1212p** is a smart Python script that automates the boring stuff in your recon process. It scans the target, checks if web ports are actually responding, and only fires up heavy web tools (like Nikto and Dirb) if it makes sense.

## Why use this?
- **Saves time:** Doesn't run web directory brute-forcing on a closed port.
- **Clean output:** Everything is saved neatly in a target-specific folder.
- **No freezes:** Designed to work smoothly right in your terminal without hanging.

## Requirements
Make sure you are on Kali Linux and have the following basic tools installed:
- Python 3
- Nmap
- curl
- whatweb
- nikto
- dirb

## Installation & Usage

**1. Clone the repository to your machine:**
```bash
git clone https://github.com/ali1212m/1212p-scanner.git

**2. Navigate to the tool's folder:**
```bash
cd 1212p-scanner

chmod +x 1212p.py

./1212p.py
