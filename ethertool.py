import os,sys
from pathlib import Path

from scapy.layers.inet import ICMP, IP
from scapy.sendrecv import *
from scapy.main import load_contrib

from inputs import ui
import confidential

load_contrib('pnio')
conf.verb=True

def main():
    Path(ui["results_folder"]).mkdir(parents=True, exist_ok=True)
    discover_devices()
    


















def discover_devices(interface=ui["interface"]):
    discover_commands = {
        "lldp":"lldpcli show neighbors ports " + interface,
        "IP":"ping 255.255.255.255 -c 3 -b -I" + interface
        }
    for scan in discover_commands:
        with open("device_discovery.md","a") as log:
            log.write("# "+ scan)
        os.system(discover_commands[scan] + " >> " + ui["results_folder"] + "device_discovery.md") 
        

if __name__ == "__main__":
    main()