#!/bin/env python
import pyshark
from dataclasses import dataclass
from sys import exit


@dataclass
class Packet():
    protocol: str
    src_addr: str
    dst_addr: str
    src_port: int
    dst_port: int


def get_most_visited_websites(cap):
    websites = {}
    for packet in cap:
        if 'http' in packet:
            try:
                host = packet.http.host
            except AttributeError:
                pass
            else:
                if host in websites:
                    websites[host] += 1
                else:
                    websites[host] = 1

    websites = {
        k: v for k,
        v in sorted(
            websites.items(),
            key=lambda item: item[1],
            reverse=True)}
    return dict(list(websites.items())[:10])


def get_user_agents(cap):
    user_agents = {}
    for packet in cap:
        try:
            user_agent = packet.http.user_agent

        except AttributeError:
            pass

        else:
            if user_agent in user_agents:
                user_agents[user_agent] += 1
            else:
                user_agents[user_agent] = 1
    user_agents = {
        k: v for k,
        v in sorted(
            user_agents.items(),
            key=lambda item: item[1],
            reverse=True)}
    return user_agents


def get_ip_addresses(cap):  # Useful while running in module
    addresses = []
    for packet in cap:
        try:
            addr = packet.ip.src

        except AttributeError:
            addr = packet.eth.src

        if addr not in addresses:
            addresses.append(addr)
    return addresses


def print_ip_addresses(cap):
    addresses = []
    print('\r\n\r\n')
    for packet in cap:
        try:
            addr = packet.ip.src

        except AttributeError:
            addr = packet.eth.src

        if addr not in addresses:
            addresses.append(addr)
            print(addr)
    print('\r\n\r\n')


def get_used_ports(cap):
    ports = {}
    for packet in cap:
        try:
            port = f'{packet[packet.transport_layer].dstport}/{packet.transport_layer.lower()}'
        except AttributeError:
            pass
        else:
            if port in ports:
                ports[port] += 1
            else:
                ports[port] = 1
    ports = {
        k: v for k,
        v in sorted(
            ports.items(),
            key=lambda item: item[1],
            reverse=True)}
    return ports


def get_connection_info(cap):   # This function is useful while using in a module
    packets = []
    for packet in cap:
        protocol = packet.transport_layer   # returns tcp or udp
        try:
            src_addr = packet.ip.src
            dst_addr = packet.ip.dst
        except AttributeError:  # If IP layer is skiped e.g DHCP
            src_addr = packet.eth.src
            dst_addr = packet.eth.dst
        try:
            src_port = packet[packet.transport_layer].srcport
            dst_port = packet[packet.transport_layer].dstport
        except AttributeError:
            src_port = 0
            dst_port = 0
            if 'icmp' in packet:
                protocol = 'ICMP'
            elif 'dhcpv6' in packet:
                protocol = 'DHCP v6'
            elif 'dhcp' in packet:
                protocol = 'DHCP'
        packets.append(
            Packet(
                protocol,
                src_addr,
                dst_addr,
                src_port,
                dst_port))
    return packets


def print_connection_info(cap):
    print('\r\n\r\n')
    for packet in cap:
        protocol = packet.transport_layer   # returns tcp or udp
        try:
            src_addr = packet.ip.src
            dst_addr = packet.ip.dst
        except AttributeError:  # If IP layer is skiped e.g DHCP
            src_addr = packet.eth.src
            dst_addr = packet.eth.dst
        try:
            src_port = packet[packet.transport_layer].srcport
            dst_port = packet[packet.transport_layer].dstport
        except AttributeError:
            src_port = 0
            dst_port = 0
            if 'icmp' in packet:
                protocol = 'ICMP'
            elif 'dhcpv6' in packet:
                protocol = 'DHCP v6'
            elif 'dhcp' in packet:
                protocol = 'DHCP'
        print(
            f'Protocol: {protocol} - Source: {src_addr} - PORT: {src_port} \t ----> \t Destination: {dst_addr} - PORT: {dst_port}')
    print('\r\n\r\n')


def grep(cap, grep_val):
    for packet in cap:
        if packet.transport_layer == 'TCP':
            try:
                raw_data = packet.data.tcp_reassembled_data.split(':')
                data = ""
                for char in raw_data:
                    data += chr(int(char, 16))

            except AttributeError:
                pass

            else:
                if grep_val in data:
                    print(f'Packet no. {packet.number}:')
                    for line in data.split('\r\n'):
                        if grep_val in line:
                            print(line)
                    print('\r\n')

        elif packet.transport_layer == 'UDP':
            try:
                raw_data = packet.data.data
                i = 0
                data = ""
                while i < len(raw_data):
                    data += chr(int(raw_data[i:i + 1], 16))
                    i += 2
                if grep_val in data:
                    print(f'Packet no. {packet.number}:')
                    for line in data.split('\r\n'):
                        if grep_val in line:
                            print(line)
                    print('\r\n')
            except AttributeError:
                pass
        else:
            pass


def print_dict(_dict):
    print('\r\n\r\namount \t | value')
    print('-------------------------')
    for item in _dict:
        print(f'{_dict[item]} \t | {item}')
    print('\r\n\r\n')


def print_list(_list):
    print('\r\n\r\n')
    for item in _list:
        print(item)
    print('\r\n\r\n')


def print_packages_detailed(packets):
    print('\r\n\r\n')
    for packet in packets:
        print(
            f'Protocol: {packet.protocol} - Source: {packet.src_addr} - PORT: {packet.src_port} \t ----> \t Destination: {packet.dst_addr} - PORT: {packet.dst_port}')
    print('\r\n\r\n')


def main():
    filename = input("[?] Pcap file path: ")
    try:
        cap = pyshark.FileCapture(filename)
    except FileNotFoundError:
        exit(f"[-] File {filename} not found.")
    else:
        print(f"[+] Successfully opened {filename}")
    while True:
        print("[?] What you want to do?")
        print("[1] Get 10 most visited websites")
        print("[2] Get user-agents")
        print("[3] Get connection details")
        print("[4] Grep mode")
        print("[5] IP list")
        print("[6] Port list")
        print("[7] Exit")
        try:
            choice = int(input("> "))
        except ValueError:
            print(f"[-] {choice} is not a valid number within range 1-7")
        else:
            if choice == 1:
                print_dict(get_most_visited_websites(cap))
            elif choice == 2:
                print_dict(get_user_agents(cap))
            elif choice == 3:
                print_connection_info(cap)
            elif choice == 4:
                grep_val = input("[?] What you want to grep by? ")
                if grep_val != '':
                    grep(cap, grep_val)
                else:
                    print("[-] You entered empty value.")
            elif choice == 5:
                print_ip_addresses(cap)
            elif choice == 6:
                print_dict(get_used_ports(cap))
            elif choice == 7:
                cap.close()
                exit("[+] Exiting.")
            else:
                print(f"[-] {choice} is not a valid number within range 1-7")


if __name__ == "__main__":
    main()
