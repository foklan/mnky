#!/usr/bin/env python3
import re
import subprocess
import optparse
import time


class Handler:
    def get_arguments(self):
        parser = optparse.OptionParser()
        parser.add_option("-s", "--source", dest="source", help="Source text file.")
        options, arguments = parser.parse_args()
        return options

    def find_ids(self):
        file_path = self.get_arguments()
        with open(file_path.source, 'r') as file:
            data = file.read()
            return re.findall(r';(\w\w\w\w\w\w\w\w);C', data)

    def command_executer(self, sam_id):
        for i in range(len(sam_id)):
            subprocess.call('curl -X POST "https://172.31.170.34:30035/sam-management/v1/sams/'+sam_id[i]+'\" --insecure -H \"Content-Type: application/json\" -H \"X-Auth-Business-Entity-Id: 0\" -H \"X-Auth-Business-Entity-Name: notUsedHeader\" -H \"X-Auth-Business-Entity-Role: ts\" -d \'{\"status\": \"ACTIVE\"}\'', shell=True)
            time.sleep(1)
            subprocess.call("echo", shell=True)

    def start(self):
        try:
            self.command_executer(self.find_ids())
        except TypeError:
            print("You must specify the source text file option.\n"
                  "Try 'python2 mnky.py --help' for more information.")


test = Handler()
test.start()