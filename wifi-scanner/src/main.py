import ipaddress
import socket
from scapy.all import *
from macvendors_api import MacVendors

def get_network():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.connect(("8.8.8.8", 53))
    addr = sock.getsockname()[0]
    sock.close()
    return ipaddress.ip_network(addr+"/24", strict=False)

def ping_scan(addr):
    hosts = []
    response, not_responded = sr(IP(dst=addr)/ICMP(), timeout=1, verbose=False)
    for sent, recv in response:
        if recv:
            return True
    return False

def arp_scan(addr):
    hosts = []
    packet = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=addr)    # ff:ff:ff:ff:ff:ff means broadcast
    response, not_responded = srp(packet, timeout=1, verbose=False)
    for sent, recv in response:
        if recv:
            hosts.append({'ip': recv[ARP].psrc, 'mac': recv[Ether].src, 'vendor': MacVendors().get_vendor(recv[Ether].src)})
    return hosts

def syn_scan(addr, port):
    packet = IP(dst=addr) / TCP(dport=port, flags='S')
    response = sr1(packet, verbose=False)
    if (tcp := response.getlayer("TCP")):
        return tcp.flags == "SA"

if __name__ == "__main__":
    network = get_network()
    arp_result = arp_scan(network.network_address.exploded+"/24")
    print(f"IP\t\tMAC\t\t\tVendor")
    for host in result:
        print(f"{host['ip']}\t{host['mac']}\t{host['vendor']}")