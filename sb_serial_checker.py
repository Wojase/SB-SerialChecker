import os
import platform
import uuid
import socket
import subprocess
from colorama import Fore, Style, init

# Initialize colorama for cross-platform support
init(autoreset=True)

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_disk_serials():
    print(Fore.CYAN + "\U0001F4BE 💾 Disk Drives:" + Style.RESET_ALL)
    try:
        result = subprocess.check_output("wmic diskdrive get model,serialnumber", shell=True, text=True)
        print(Fore.GREEN + result.strip())
    except Exception as e:
        print(Fore.RED + f"Error: {e}")

def get_cpu_serial():
    print(Fore.CYAN + "\U0001F5A5️ 🖥️ CPU:" + Style.RESET_ALL)
    try:
        result = subprocess.check_output("wmic cpu get serialnumber", shell=True, text=True)
        print(Fore.GREEN + result.strip())
    except Exception as e:
        print(Fore.RED + f"Error: {e}")

def get_bios_serial():
    print(Fore.CYAN + "\U0001F4E6 📦 BIOS:" + Style.RESET_ALL)
    try:
        result = subprocess.check_output("wmic bios get serialnumber", shell=True, text=True)
        print(Fore.GREEN + result.strip())
    except Exception as e:
        print(Fore.RED + f"Error: {e}")

def get_motherboard_serial():
    print(Fore.CYAN + "\U0001F527 🔧 Motherboard:" + Style.RESET_ALL)
    try:
        result = subprocess.check_output("wmic baseboard get serialnumber", shell=True, text=True)
        print(Fore.GREEN + result.strip())
    except Exception as e:
        print(Fore.RED + f"Error: {e}")

def get_smbios_uuid():
    print(Fore.CYAN + "\U0001F4CC 🆔 smBIOS UUID:" + Style.RESET_ALL)
    try:
        result = subprocess.check_output("wmic path win32_computersystemproduct get uuid", shell=True, text=True)
        print(Fore.GREEN + result.strip())
    except Exception as e:
        print(Fore.RED + f"Error: {e}")

def get_mac_addresses():
    print(Fore.CYAN + "\U0001F517 🔗 MAC Addresses:" + Style.RESET_ALL)
    try:
        macs = subprocess.check_output("getmac", shell=True, text=True)
        print(Fore.GREEN + macs.strip())
    except Exception as e:
        print(Fore.RED + f"Error: {e}")

def main():
    while True:
        clear_console()
        print(Fore.MAGENTA + "\n" + "*" * 40)
        print("\U0001F31F 🌟 " + Fore.YELLOW + "Hardware Serial Checker" + Fore.MAGENTA + " 🌟")
        print("*" * 40 + Style.RESET_ALL)

        get_disk_serials()
        print()
        get_cpu_serial()
        print()
        get_bios_serial()
        print()
        get_motherboard_serial()
        print()
        get_smbios_uuid()
        print()
        get_mac_addresses()

        print(Fore.MAGENTA + "\n" + "=" * 40)
        print(Fore.YELLOW + "✨ Check complete! Press Ctrl+C to exit or press Enter to refresh." + Style.RESET_ALL)
        print(Fore.MAGENTA + "=" * 40)
        input()

if __name__ == "__main__":
    main()
