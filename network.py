import nmap
import subprocess
import argparse

# defining nmap scan function with arguments
# tgtHost will hold the host value and tgtPort will hold the port value
def nmapScan(Host, Port):
    nmscan = nmap.PortScanner()
    nmscan.scan(Host, Port)
    state = nmscan[Host]['tcp'][int(Port)]['state']
    print(" [*] " + Host + " tcp/"+Port + " "+state)

def portScan(host,port):

    tgtHost = host
    tgtPort = port

    print ("Scanning: " + tgtHost + "-" + str(tgtPort))
    # calling the nmapScan function with the provided values
    nmapScan(tgtHost, str(tgtPort))

def main():
    print("What do you wanna do\n 1. Port Scan\n 2. Banner Grabbing\n")
    a = int(input())

    if a == 1:
        host= input("Value for host: ")
        port = input("value for port: ")
        portScan(host, port)
    elif a==2:
        host = input("Value for host: ")
        subprocess.call(['nmap', '-sV', '--script=banner ', host])

if __name__ == '__main__':
    main()