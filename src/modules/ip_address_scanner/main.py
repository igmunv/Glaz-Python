import subprocess
import os
import ipaddress
import time
import threading

from base import BaseModule

class IPAddressScanner_Glaz(BaseModule):

    # Module information
    name = "IP Address Scanner"
    description = "IP address lookup"
    build = True
    build_sources = {"/scanner.c": "/bin/scanner"}
    variables = {"range": {"description": "Scanned IP Address Range", "is_required": True}}


    # Main function
    def run(self, VAR_VALUE_DICT):

        # Get 'range' variable
        range_ = VAR_VALUE_DICT['range']

        # Check CIDR
        if "/" not in range_:
            print(f"[!] CIDR is missing. The format should be 'ADDRESS/CIDR'. Example: 192.168.0.1/24")
            return -1

         # Check IP network
        try:
            ipaddress.ip_network(range_, strict=False)
        except ValueError:
            print(f"[!] '{range_}' does not appear to be an IPv4 network!")
            return -1

        # Get network and broadcast address
        network_cidr = ipaddress.IPv4Network(range_, strict=False)

        # Start scan
        self._scan_all_ip_addr(network_cidr.network_address, network_cidr.broadcast_address)

        time.sleep(0.25) # For correct output


    # Division into chunks
    def _chunked(self, data, n):
        k, m = divmod(len(data), n)
        result = [data[i * k + min(i, m):(i + 1) * k + min(i + 1, m)] for i in range(n)]
        return result


    # Scan all ip address in range and ping
    def _scan_all_ip_addr(self, network_address, broadcast_address):
        try:
            network_obj = ipaddress.IPv4Network(f"{network_address}/" +
                                            str(ipaddress.IPv4Address(broadcast_address).max_prefixlen -
                                                (int(ipaddress.IPv4Address(broadcast_address)) -
                                                    int(ipaddress.IPv4Address(network_address))).bit_length()))

            # ptr = 0
            # total_result = network_obj.num_addresses

            threads_num = 20

            ip_addresses = []

            print("[*] Calculating available addresses...")
            for ip in network_obj.hosts():
                ip_addresses.append(ip)

            print("[*] Division into chunks...")
            chunks = self._chunked(ip_addresses, threads_num)

            print(f"[*] Scanning {len(ip_addresses)} addresses:")
            start_time = time.time()
            self._threads_start(chunks)
            end_time = time.time()
            print(f"[v] The scan is completed in {end_time-start_time} seconds")

                # self._run_bin(ip)
                # ptr+=1
                # procent = int((ptr * 100) / total_result)
                # print(f"{procent}% | {total_result} / {ptr}\r", end='', flush=True)

        except ipaddress.AddressValueError as e:
            print(f"[!] Invalid IP address or network format: {e}")
            return []
        except ValueError as e:
            print(f"[!] Could not determine network from provided addresses: {e}")
            return []


    # Run scanner (bin)
    def _run_bin(self, ip_address, ):

        binary_path = "/bin/scanner"
        full_binary_path = os.path.dirname(__file__) + binary_path
        proc = subprocess.Popen(
            [full_binary_path],
            stdin=subprocess.PIPE
        )
        proc.stdin.write(str(ip_address).encode("ascii"))
        proc.stdin.close()
        proc.wait()

        time.sleep(0.05) # For correct output


    def _iterate_chunk(self, chunk):

        for ip_address in chunk:
            self._run_bin(ip_address)


    def _threads_start(self, chunks):

        threads = []
        for chunk in chunks:

            thread = threading.Thread(target=self._iterate_chunk, args=(chunk,))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()
