# from base import BaseModule

import subprocess, os, ipaddress

class IPAddressScanner_Glaz: # BaseModule
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
            ipaddress.ip_network(range_)
        except ValueError:
            print(f"[!] '{range_}' does not appear to be an IPv4 network!")
            return -1

        data


        print(os.path.dirname(__file__))

    def run_binary(self, data):

        binary_path = "/bin/scanner"
        full_binary_path = os.path.dirname(__file__) + binary_path
        proc = subprocess.Popen(
            [full_binary_path],
            stdin=subprocess.PIPE
        )
        proc.stdin.write(data.encode("ascii"))
        proc.stdin.close()
        proc.wait()


if __name__ == "__main__":
    s = IPAddressScanner_Glaz();
    abc = "192.168.0.1-255.255.255.0"
    s.run_binary(abc)
