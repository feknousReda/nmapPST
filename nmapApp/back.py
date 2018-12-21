import nmap
from nmapApp import nmapcsvconverter
import csv,sqlite3


class backProcess():

    def launchNmap(url,opt):
        argument =  opt + "  -oG /scan.txt"
        nm = nmap.PortScanner()
        nm.scan( arguments = argument,hosts = url)
        nmapcsvconverter.converter()
        nmapcsvconverter.tosql()
        raws = nmapcsvconverter.collecte_info_sqlite()
        return raws
