#!/usr/bin/env python3
import os, sys, time

def banner():
    os.system('clear')
    print("\033[92m")
    print(" ██████╗ ██╗  ██╗ █████╗ ███╗   ██╗ █████╗ ")
    print("██╔════╝ ██║  ██║██╔══██╗████╗  ██║██╔══██╗")
    print("██║  ███╗███████║███████║██╔██╗ ██║███████║")
    print("██║   ██║██╔══██║██╔══██║██║╚██╗██║██╔══██║")
    print("╚██████╔╝██║  ██║██║  ██║██║ ╚████║██║  ██║")
    print(" ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝")
    print("\033[0m")
    print("\033[93m  Ghana Hacker Toolkit v2.0 | By Fred772772 - Accra\033[0m")
    print("\033[96m  GitHub: github.com/Fred772772/ghana-hacker-toolkit\033[0m")
    print("-"*55)

def menu():
    while True:
        banner()
        print("\n[1] Port Scanner")
        print("[2] WiFi Password Generator")
        print("[3] Password Strength Checker")
        print("[4] Hack Tool (Main)")
        print("[5] Secret / Hash Tool")
        print("[6] Final Tool")
        print("[0] Exit")
        choice = input("\n\033[92mSelect > \033[0m")

        if choice == "1":
            os.system("python portscan.py")
        elif choice == "2":
            os.system("python wifigen.py")
        elif choice == "3":
            os.system("python passcheck.py")
        elif choice == "4":
            os.system("python hacktool.py")
        elif choice == "5":
            os.system("python secret.py")
        elif choice == "6":
            os.system("python final.py")
        elif choice == "0":
            print("Goodbye, AccraHacker!")
            sys.exit()
        else:
            print("Invalid!")
            time.sleep(1)
        input("\nPress ENTER to return to menu...")

if __name__ == "__main__":
    menu()
