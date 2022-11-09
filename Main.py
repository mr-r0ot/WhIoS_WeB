import socket
def whois():
    try:
        socket.gethostbyname("google.com")

        print('''
__          ___    _ _____ ____   _____ 
\ \        / / |  | |_   _/ __ \ / ____|
 \ \  /\  / /| |__| | | || |  | | (___  
  \ \/  \/ / |  __  | | || |  | |\___ \ 
   \  /\  /  | |  | |_| || |__| |____) |
    \/  \/   |_|  |_|_____\____/|_____/ 
                                        
                                        
       _____  _____ _____  _____ _____ _______ 
      / ____|/ ____|  __ \|_   _|  __ \__   __|
     | (___ | |    | |__) | | | | |__) | | |   
      \___ \| |    |  _  /  | | |  ___/  | |   
      ____) | |____| | \ \ _| |_| |      | |   
     |_____/ \_____|_|  \_\_____|_|      |_|   
                                          
                                          
''')
        domain = input("Domain : ").lower()
        domain = domain.replace("http://","")
        domain = domain.replace("https://","")
        domain = domain.replace("www.","")
        if domain[-3:] == "org" or domain[-3:] == "com" or domain[-3:] == "net":
            whois_server = "whois.internic.net"
        else:
            whois_server =  "whois.iana.org"
        s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
        s.connect((whois_server,43))
        s.send((domain+"\r\n").encode())
        msg = s.recv(10000)
        print(msg.decode())
        input("\n\n\n\n\t  Enter for close ")
    except:
        print("  . . . . .  Your Not Connect To Net! . . . . . .\n")
        input("\n\n\n\n\t  Enter for close ")
# ================================================

whois()
