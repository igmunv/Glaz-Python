from base import BaseModule

import subprocess, os, ipaddress

class IPAddressScanner_Glaz(BaseModule):
    name = "IP Address Scanner"
    description = ""
    usage = "Usage"
    variables = {"range": {"description": "Scanned IP Address Range", "is_mandatory": True}} # MANDATORY !!!

    def run(self, VAR_VALUE_DICT):
        # переменные, которые указаны в словаре variables, и их значения
        # передаются в модуль через переменную словарь VAR_VALUE_DICT
        # все значения которые передаются в модуль через словарь VAR_VALUE_DICT являются типом string
        range_ = VAR_VALUE_DICT['range']
        try:
            ipaddress.ip_network(range_, strict=False)
        except ValueError:
            print(f"[!] '{range_}' does not appear to be an IPv4 network!")
            return -1

        network_cidr = ipaddress.IPv4Network(range_, strict=False)

        self.scan_all_ip_addr(network_cidr.network_address, network_cidr.broadcast_address)


    def run_ping_bin(self, ip_address):

        binary_path = "/bin/scanner"
        full_binary_path = os.path.dirname(__file__) + binary_path
        proc = subprocess.Popen(
            [full_binary_path],
            stdin=subprocess.PIPE
        )
        proc.stdin.write(str(ip_address).encode("ascii"))
        proc.stdin.close()
        proc.wait


    def scan_all_ip_addr(self, network_address, broadcast_address):
        try:
            network_obj = ipaddress.IPv4Network(f"{network_address}/" +
                                            str(ipaddress.IPv4Address(broadcast_address).max_prefixlen -
                                                (int(ipaddress.IPv4Address(broadcast_address)) -
                                                    int(ipaddress.IPv4Address(network_address))).bit_length()))

            for ip in network_obj.hosts():
                self.run_ping_bin(ip)

        except ipaddress.AddressValueError as e:
            print(f"Error: Invalid IP address or network format: {e}")
            return []
        except ValueError as e:
            print(f"Error: Could not determine network from provided addresses: {e}")
            return []


if __name__ == "__main__":
    pass
