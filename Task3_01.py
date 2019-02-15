from netifaces import interfaces, ifaddresses, AF_INET

def ip4_addresses():
    ip_addr = []
    for i in interfaces():
        for link in ifaddresses(i)[AF_INET]:
            ip_addr.append(link['addr'])
    return ip_list
