#!/usr/bin/python3

# +----------------------------------------------------------------------+
# | mnky 1.3.1                                                           |
# | created by Foklan                                                    |
# | Script works only with Python 3                                      |
# | This script is used for automated SAMs activation                    |
# | Takes 2 arguments, response_file and host:port of sam-management     |
# +----------------------------------------------------------------------+

import re
import subprocess
from optparse import OptionParser
from time import sleep


class Mnky:
    def get_arguments(self):
        parser = OptionParser()
        parser.add_option("-f", "--file", dest="file", help="Source response file.")
        parser.add_option("-k", "--host", dest="host", help="IP:PORT of sam-management")
        parser.add_option("-t", "--delay", dest="delay", help="Delay between POST requests, default 1s")
        options, arguments = parser.parse_args()
        return options

    # reads response_file and returns LIST of SAM IDs
    def find_ids(self):
        outlist = []
        templist = []
        parser_options = self.get_arguments()
        with open(parser_options.file, 'r') as file:
            response_file = file.readlines()
            for line in response_file:
                outlist.append(line.split(";"))  # Append splitted line to outlist

            outlist.pop(0)   # Delete first line where isn't SAM ID
            outlist.pop(-1)  # Delete lastt line -||-
            
            for element in outlist:
                templist.append(element[3])

        return templist

    # sam_id = LIST of sam IDs
    # host = STRING
    def command_executer(self, sam_id, host):
        if self.get_arguments().host is None:
            print("You must specify HOST:PORT!")
        else:
            confirmation = input(f"script will now execute activation process! \n Number of SAMs: {len(sam_id)} \n File: {self.get_arguments().file}\n Host: {self.get_arguments().host} \nDo you want to continue? (yes/No): ")
            if (confirmation == 'yes' or confirmation == 'y') and self.get_arguments().host != None:
                for i in range(len(sam_id)):
                    subprocess.call(f'curl -X POST "https://{host}/sam-management/v1/sams/{sam_id[i]}' + '\" --insecure -H \\"Content-Type: application/json\" -H \"X-Auth-Business-Entity-Id: 0\" -H \"X-Auth-Business-Entity-Name: notUsedHeader\" -H \"X-Auth-Business-Entity-Role: ts\" -d \'{\"status\": \"ACTIVE\"}\'', shell=True)

                    # Print for debugging
                    #print(f'curl -X POST "https://{host}/sam-management/v1/sams/{sam_id[i]}' + '\" --insecure -H \"Content-Type: applicat\ion/json\" -H \"X-Auth-Business-Entity-Id: 0\" -H \"X-Auth-Business-Entity-Name: notUsedHeader\" -H \"X-Auth-Business-Entity-Role: ts\" -d \'{\"status\": \"ACTIVE\"}\'')
                    if self.get_arguments().delay is None:
                        sleep(1)
                    else:
                        sleep(int(self.get_arguments().delay))
                    subprocess.call("echo", shell=True)
            else:
                print("Script will now exit...")
                exit()

    def main(self):
        try:
            self.command_executer(self.find_ids(), self.get_arguments().host)
        except TypeError:
            print("You must specify the source response file and host:port!\n"
                  "Try run mnky with --help option for more information.")
        except KeyboardInterrupt:
            print("\nExitting script...")
            exit()
        except FileNotFoundError:
            print(f"{self.get_arguments().file}: No such file")
        finally:
            exit()


test = Mnky()
test.main()


