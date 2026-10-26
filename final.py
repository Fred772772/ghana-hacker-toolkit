import socket, base64, random, string
from colorama import Fore, Style, init
init()

banner = f"""
{Fore.GREEN}
██╗  ██╗ █████╗  ██████╗██╗  ██╗
██║  ██║██╔══██╗██╔════╝██║ ██╔╝
███████║███████║██║     █████╔╝ 
██╔══██║██╔══██║██║     ██╔═██╗ 
██║  ██║██║  ██║╚██████╗██║  ██╗
╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝
{Style.RESET_ALL}
{Fore.CYAN}  GHANA HACKER TOOLKIT v2.0 - By YOU{Style.RESET_ALL}
"""

print(banner)

while True:
    print(f"{Fore.YELLOW}1{Style.RESET_ALL}. Check Password")
    print(f"{Fore.YELLOW}2{Style.RESET_ALL}. Scan Website")
    print(f"{Fore.YELLOW}3{Style.RESET_ALL}. Hide Message")
    print(f"{Fore.YELLOW}4{Style.RESET_ALL}. Generate WiFi Pass")
    print(f"{Fore.RED}5. Exit{Style.RESET_ALL}")
    c=input(f"\n{Fore.GREEN}root@accra:~# {Style.RESET_ALL}")

    if c=="1":
        pwd=input("Password: ")
        score=len(pwd)>=8 and 1 or 0
        print(f"{Fore.GREEN}Strength checked!{Style.RESET_ALL}")
    elif c=="2":
        target=input("Target: ")
        print(f"{Fore.CYAN}Scanning {target}...{Style.RESET_ALL}")
        for p in [80,443]:
            s=socket.socket(); s.settimeout(1)
            if s.connect_ex((target,p))==0:
                print(f"{Fore.GREEN}[OPEN] {p}{Style.RESET_ALL}")
            s.close()
    elif c=="3":
        m=input("Message: ")
        e=base64.b64encode(m.encode()).decode()
        print(f"{Fore.MAGENTA}Hidden: {e}{Style.RESET_ALL}")
    elif c=="4":
        chars=string.ascii_letters+string.digits+"!@#"
        pwd="".join(random.choice(chars) for _ in range(16))
        print(f"{Fore.GREEN}Generated: {pwd}{Style.RESET_ALL}")
    elif c=="5":
        print(f"{Fore.CYAN}Goodbye, hacker!{Style.RESET_ALL}")
        break
