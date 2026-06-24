import requests
import time
import sys
import os
import random

# Feature 1: Auto Screen Clear & Fit Terminal
os.system('clear')

def slow_print(text, speed=0.02):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)

# Cyberpunk Neon Color Palette
G = "\033[1;32m"  # Matrix Green
R = "\033[1;31m"  # Cyber Red
Y = "\033[1;33m"  # Warning Yellow
C = "\033[1;36m"  # Info Cyan
W = "\033[0m"     # Reset

# ======================================================
# PASSWORD / LOGIN SYSTEM (Added)
# ======================================================
CORRECT_PASSWORD = "movindi"

print(f"{G}======================================================")
print(f"{Y}        LOGIN TO ACCSESS SPAM MODULE       ")
print(f"{G}======================================================{W}")

# User ගෙන් password එක ඉල්ලීම (ටයිප් කරද්දී පේන්නේ නැති වෙන්න නෙවෙයි, සාමාන්‍ය input එකක් විදිහට)
user_password = input(f"{C}[?] ENTER LOGIN PASSWORD: {W}")

if user_password != CORRECT_PASSWORD:
    print(f"\n{R}[-[ ❌ ACCESS DENIED: INVALID PASSWORD ]-{W}")
    time.sleep(1)
    sys.exit()
else:
    print(f"\n{G}[+] ACCESS GRANTED! DECRYPTING SYSTEM...{W}")
    time.sleep(1.5)
    os.system('clear')
# ======================================================

# Massive ASCII Banner
print(f"{G}======================================================")
print(r"  ________ ____  _____  _ __  _       _       ")
print(r" / ___/  |/  / |/ / _ \| |  \| |     /_\      ")
print(r"/ (_ / /|_/ /    / // /| | |\  |    / _ \     ")
print(r"\___/_/  /_/_/|_/_/ /_/|_|_| \_|   /_/ \_\    ")
print(f"======================================================")
print(f" >>  GUNIYA SPAMS #NO.1 SRI LANKA v1.0 <<          ")
print(f" >> BY GUNIDU LIYANAGE <<          ")
print(f"======================================================{W}")

# Target Settings
NOTIFY_USER_ID = "32118"
NOTIFY_API_KEY = "xvSEUfgFX72aW0CzCiEX"
SENDER_ID = "NotifyDEMO"

# Feature 2: All English Pro Prompts
number = input(f"\n{C}[?] ENTER TARGET NUMBER (e.g. 9471xxxxxxx): {W}")
try:
    total_msg = int(input(f"{C}[?] ENTER INJECTION COUNT: {W}"))
except ValueError:
    print(f"\n{R}[-[ CRITICAL ERROR: INVALID COUNT TYPE ]-{W}")
    exit()

# Custom Text Requested by User (Emoji clean to prevent '??')
message = "GUNIYA SPAMS! WORLD BEST SPAMS HAVE NICE SPAMS"

print(f"\n{Y}[!] INITIALIZING MATRIX DISPATCH OVERRIDE...{W}")
time.sleep(0.5)

# Feature 3: System Handshake Simulation
modules = ["SECURE_PORT_CHECK", "GATEWAY_ESTABLISH", "TOKEN_VALIDATION", "PAYLOAD_INJECTION_READY"]
for mod in modules:
    sys.stdout.write(f"{G}[+] STAGE: {mod}... ")
    sys.stdout.flush()
    time.sleep(0.3)
    print(f"[ SUCCESS ]{W}")

print(f"{G}------------------------------------------------------{W}")
print(f"{Y}[*] LAUNCHING VECTOR ATTACK ON: {number}{W}")
print(f"{G}------------------------------------------------------{W}")

# Timer Start
start_time = time.time()
success_count = 0

for i in range(total_msg):
    try:
        # Feature 4: Randomized Hex Token Generation for Visual Effect
        fake_token = f"0x{random.randint(100000, 999999)}A{random.randint(10, 99)}"
        
        url = f"https://app.notify.lk/api/v1/send?api_key={NOTIFY_API_KEY}&user_id={NOTIFY_USER_ID}&sender_id={SENDER_ID}&to={number}&message={message} [{i+1}]"
        
        response = requests.get(url)
        
        # Syntax Errors Fixed (response.status_code and success_count tracking)
        if response.status_code == 200:
            print(f"{G}[{i+1:02d}] [{fake_token}] SENDING SPAMS MSG{W}")
            success_count += 1
        else:
            print(f"\n{R}[{i+1:02d}] [{fake_token}] REJECTED -> SERVER DROPPED [HTTP {response.status_code}]{W}")
            
    except Exception as e:
        print(f"\n{R}[!] CONNECTION BREACH -> RETRYING: {e}{W}")
        
    # Sleep timer modified to 0.1 seconds
    time.sleep(0.1)

# Timer End
end_time = time.time()
duration = round(end_time - start_time, 2)

# Feature 5: Execution Metrics Output
print(f"{G}------------------------------------------------------{W}")
print(f"{C}[+] PROCESS TERMINATED SUCCESSFULLY.{W}")
print(f"{G}[+] TOTAL SUCCESSFUL INJECTIONS: {success_count}/{total_msg}{W}")
print(f"{G}[+] TOTAL TIME ELAPSED: {duration} SECONDS{W}")
print(f"{G}======================================================{W}")

