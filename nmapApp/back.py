import nmap
from nmapApp import nmapcsvconverter
import csv,sqlite3
#from nmapcsvconverter import main

class backProcess():

    def launchNmap(url,opt):
        argument =  opt + "  -oG /root/scan.txt"
        nm = nmap.PortScanner()
        nm.scan( arguments = argument,hosts = url)
        print(nm.command_line())
        print(argument)
        #exec(open("nmapApp.nmapcsvconverter.py").read())
        nmapcsvconverter.converter()
#execfile("nmapcsvconverter.py")
#nm.scan(hosts)

#print(nm.scaninfo())
