# mnky script
**automated activation of SAMs in S&amp;B**

1. Tested with Python 3.8.10
2. Run script on required system with python3 mnky.py -f [file] -k [host/ip:port]
3. Enter parameters sam-management IP and PORT
4. Script will show you how many SAMs are in the response file

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
script will now execute activation process!
 Number of SAMs: 100
 File: some_response_file.txt
 Host: 10.66.36.100:30001
Do you want to continue? (yes/No):
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

5. Confirm activation


**COMMAND SAMPLES:**
python3 mnky.py -f [RESPONSE FILE] -k [IP:PORT]
python3 mnky.py -f response_file_2.txt -k 172.164.42.21:30004
python3 mnky.py --file response_file_2.txt --host 172.164.42.21:30004

**OPTIONAL PARAMETER:**
parameter -t sets delay (in seconds) between individual activation requests (useful for systems with higher delay)
python3 mnky.py --file response_file_2.txt --host 172.164.42.21:30004 -t 1
