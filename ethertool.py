from scapy.all import conf,AsyncSniffer,TCP,IP, send, sr, ICMP, Ether, load_contrib, sendp

load_contrib('pnio')
conf.verb=True

sniffer=AsyncSniffer(prn = lambda x: x.summary(), timeout=2)
pkt=Ether(src='84:3a:5b:03:c7:3d', dst='10:65:30:b9:19:bb')/ProfinetIO(frameID="RT_CLASS_1")/b'ABC'

sendp(iface="eth0", x=pkt, count=10)