from base import BaseModule

import os, time, threading
from http import client as httpcli
from urllib.parse import quote, urlparse

class DirectoryScanner_Glaz(BaseModule):

    # Module information
    name = "Directory Scanner"
    description = "Search for site directories"
    build = False
    variables = {
        "host": {"description": "Hostname or IP address of target", "is_required": True},
        "port": {"description": "Port", "is_required": False},
        "wordlist": {"description": "Path to wordlist", "is_required": False},
        "threads": {"description": "", "is_required": False}
        }


    result_counter = 0
    wordlist_size = 0
    find_paths = {}

    # Splitting into chunks
    def chunked(self, data, n):
        k, m = divmod(len(data), n)
        result = [data[i * k + min(i, m):(i + 1) * k + min(i + 1, m)] for i in range(n)]
        return result

    # Get all parts from url
    def parse_url(url: str):
        p = urlparse(url)
        scheme = p.scheme
        hostname = p.hostname
        port = p.port
        path = p.path or '/'
        username = p.username
        password = p.password
        query = p.query
        fragment = p.fragment

        # If port = None then port = default
        if port is None:
            if scheme == 'http':
                port = 80
            elif scheme == 'https':
                port = 443

        return {
            'scheme': scheme,
            'hostname': hostname,
            'port': port,
            'path': path,
            'username': username,
            'password': password,
            'query': query,
            'fragment': fragment,
        }

    # Send get request
    def httpget(self, host, port, path):
        # headers = {"Host": host, "User-Agent": "Glaz"}
        conn = httpcli.HTTPConnection(host, port)
        conn.request("GET", path)
        response = conn.getresponse()
        return response

    # Http scan
    def http_run(self, host, port, path, wordlist):
        global result_counter
        for word in wordlist:
            time_sleep = 0
            while(True):
                result_path = f"{path}{word}"

                if time_sleep > 0:
                    time.sleep(time_sleep)

                try:
                    response = self.httpget(host, port, quote(result_path))
                    if response.status != 404:
                        self.find_paths[result_path] = {"status_code": response.status}
                        minus = (" " * (80-(len(result_path)+3+len(str(response.status)))))
                        print(f"\r{response.status} - {result_path}{minus}")



                except BaseException as ex:
                    if "[Errno 99] Cannot assign requested address" in str(ex):
                        time_sleep += 0.25
                        continue
                    else:
                        print(f"{ex} | {result_path}")
                self.result_counter += 1
                break



            # print(f"[{response.status}] - {result_path}")
            # print(f"T: {end_time-start_time}")

    #Main function
    def run(self, VAR_VALUE_DICT):
        host_path = VAR_VALUE_DICT['host']
        port = VAR_VALUE_DICT['port']
        wordlist_path = VAR_VALUE_DICT['wordlist']
        thread_num = VAR_VALUE_DICT['threads']
        path = ""

        # Check input data

        if not (host_path.startswith('http://') or host_path.startswith('https://')):
            print('Error protocol. Https or http')
            return -1

        if port != None and not port.isdigit():
            print('Port uncorect')
            return -1

        if wordlist_path != None and not os.path.exists(wordlist_path):
            print("Wordlist path not exists")
            return -1

        if wordlist_path == None:
            wordlist_path = "/usr/share/wordlists/big.txt"
            if not os.path.exists(wordlist_path):
                print("Default wordlist path not exists")
                return -1

        if thread_num != None and not thread_num.isdigit():
            print('Threads variable uncorect')
            return -1

        if thread_num == None:
            thread_num = 2

        # Get path and host from host_path
        comma_pos = host_path.find(':')
        protocol = host_path[:comma_pos]
        host_without_http_s = host_path.replace("https://", "").replace("http://", "")
        slesh_pos = host_without_http_s.find('/')
        host = host_without_http_s[:slesh_pos]
        path = host_without_http_s[slesh_pos:]

        if not path.endswith('/'):
            path += '/'

        # Get wordlist from file
        wordlist = open(wordlist_path, encoding='utf-8').read().split()
        self.wordlist_size = len(wordlist)

        wordlist_chunks = self.chunked(wordlist, thread_num)

        # Run
        print(f"Protocol: {protocol}\nHost: {host}\nPath: {path}") # http://google.com/

        if protocol == 'http':

            if port == None:
                port = 80

            threads = []
            for chunk in wordlist_chunks:
                thread = threading.Thread(target=self.http_run, args=(host, port, path, chunk,))
                threads.append(thread)
                thread.start()

            procent = 0

            while self.result_counter < len(wordlist):
                procent = int((self.result_counter*100) / self.wordlist_size)

                print(f"{procent}% | {self.result_counter} / {self.wordlist_size}\r", end='', flush=True)
                time.sleep(0.5)

            for thread in threads:
                thread.join()
            procent = int((self.result_counter*100) / self.wordlist_size)
            print(f"{procent}% | {self.result_counter} / {self.wordlist_size}\r", end='', flush=True)
            print()


        elif protocol == 'https':
            if port == None:
                port = 443


        else:
            print('[!] Unknown protocol')
            return -1
