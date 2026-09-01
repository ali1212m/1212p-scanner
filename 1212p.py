#!/usr/bin/env python3
import os
import subprocess

os.system("clear")
print("\033[1;31m")
print("  __ ___  __ ___         ")
print(" /_ |__ \\/_ |__ \\        ")
print("  | |  ) | | |  ) |____  ")
print("  | | / /  | | / /|  _ \\ ")
print("  | |/ /_  | |/ /_| |_) |")
print("  |_|____| |_|____| .__/ ")
print("                  | |    ")
print("                  |_|    ")
print("\033[0m")
print("\033[1;36m================================================\033[0m")
print("\033[1;36m         1212p Smart Auto Scanner               \033[0m")
print("\033[1;36m================================================\033[0m\n")

# Get the target from user input
target = input("\033[1;33m[*] Enter Target IP or URL: \033[0m").strip()

if not target:
    print("\033[1;31m[!] No target provided! Exiting the tool.\033[0m")
    exit()

# Create a dedicated directory to save the scan results
dir_name = f"{target}_results"
os.makedirs(dir_name, exist_ok=True)

print(f"\n\033[1;33m[*] Scanning {target}... This will take some time.\033[0m\n")

# 1. Port scanning using Nmap
print("\033[1;32m[1/4] Running Nmap to find open ports...\033[0m")
subprocess.run(f"nmap -sV {target} -oN {dir_name}/nmap_scan.txt", shell=True)
print("\033[1;34m------------------------------------------------\033[0m")

# 2. Smart Web Check: Verify if web services (HTTP/HTTPS) are responsive
print("\033[1;33m[*] Checking if web services are responsive...\033[0m")
curl_http = subprocess.run(["curl", "-s", "-m", "5", f"http://{target}"], stdout=subprocess.DEVNULL)
curl_https = subprocess.run(["curl", "-s", "-m", "5", f"https://{target}"], stdout=subprocess.DEVNULL)

if curl_http.returncode == 0 or curl_https.returncode == 0:
    print("\033[1;32m[+] Web server detected, continuing with web tools...\033[0m\n")
    
    # 3. Technology fingerprinting (WhatWeb)
    print("\033[1;32m[2/4] Running WhatWeb...\033[0m")
    with open(f"{dir_name}/whatweb_scan.txt", "w") as f:
        subprocess.run(["whatweb", target], stdout=f)
    print("WhatWeb results saved.")
    
    # 4. Web server vulnerability scanning (Nikto)
    print("\033[1;32m[3/4] Running Nikto...\033[0m")
    with open(os.devnull, "w") as devnull:
        subprocess.run(["nikto", "-h", target, "-output", f"{dir_name}/nikto_scan.txt"], stdout=devnull, stderr=devnull)
    print("Nikto results saved.")
    
    # 5. Directory and file brute-forcing (Dirb)
    print("\033[1;32m[4/4] Running Dirb...\033[0m")
    with open(os.devnull, "w") as devnull:
        subprocess.run(["dirb", f"http://{target}/", "-o", f"{dir_name}/dirb_scan.txt"], stdout=devnull, stderr=devnull)
    print("Dirb results saved.")
    
    print(f"\n\033[1;32m[*] Scan complete! All details are saved in: {dir_name}\033[0m")
else:
    # Skip web tools to prevent the script from hanging on closed ports
    print("\033[1;31m[!] No web server detected. Skipped web tools to prevent hanging.\033[0m")
    print(f"\033[1;32m[*] Scan complete! All details are saved in: {dir_name}\033[0m")
