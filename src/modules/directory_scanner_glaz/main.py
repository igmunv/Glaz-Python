from base import BaseModule
import requests

class DIrectoryScanner_Glaz(BaseModule):
    name = "Directory Scanner (Glaz)"
    description = ""
    variables = {"host": {"description": "Hostname or IP address of target", "is_mandatory": True}, "wordlist": {"description": "Path to wordlist", "is_mandatory": False}}

    def run(self, VAR_VALUE_DICT):

        host = VAR_VALUE_DICT['host']
        header = {}

        wordlist = ['1', '2', '3']
        for word in wordlist:
            r = requests.get(f"{host}/{word}")
            status_code = r.status_code
            print(f"{status_code} - /{word}")



