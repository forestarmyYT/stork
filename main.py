import json
import os
import subprocess

CONFIG_FILE = "config.json"

# ANSI color codes for bright colors
BOLD_RED = "\033[1;91m"
BOLD_YELLOW = "\033[1;93m"
BOLD_CYAN = "\033[1;96m"
RESET = "\033[0m"

BANNER = f"""
{BOLD_RED} 𝐅 𝐎 𝐑 𝐄 𝐒 𝐓 𝐀 𝐑 𝐌 𝐘 {RESET}
"""

def setup_account():
    """Setup account by asking for email and password, then saving to config.json"""
    print(f"\n{BOLD_YELLOW}[1] Account Setup{RESET}")
    email = input(f"{BOLD_CYAN}Enter Email: {RESET}")
    password = input(f"{BOLD_CYAN}Enter Password: {RESET}")

    config_data = {
        "cognito": {
            "region": "ap-northeast-1",
            "clientId": "5msns4n49hmg3dftp2tp1t2iuh",
            "userPoolId": "ap-northeast-1_M22I44OpC",
            "username": email,
            "password": password
        },
        "stork": {
            "intervalSeconds": 5
        },
        "threads": {
            "maxWorkers": 1
        }
    }

    with open(CONFIG_FILE, "w") as file:
        json.dump(config_data, file, indent=2)

    print(f"\n✅ {BOLD_YELLOW}Configuration saved in {CONFIG_FILE}{RESET}\n")

def run_script():
    """Run index.js using Node.js"""
    print(f"\n{BOLD_YELLOW}[2] Running index.js...{RESET}\n")
    try:
        subprocess.run(["node", "index.js"], check=True)
    except FileNotFoundError:
        print(f"{BOLD_RED}❌ Error: Node.js is not installed or not in PATH.{RESET}")

if __name__ == "__main__":
    print(BANNER)
    print(f"{BOLD_YELLOW}Select an option:{RESET}")
    print(f"{BOLD_CYAN}1. Account Setup{RESET}")
    print(f"{BOLD_CYAN}2. Run Script{RESET}")
    
    choice = input(f"\n{BOLD_YELLOW}Enter choice (1 or 2): {RESET}")

    if choice == "1":
        setup_account()
    elif choice == "2":
        run_script()
    else:
        print(f"{BOLD_RED}❌ Invalid choice. Please enter 1 or 2.{RESET}")
