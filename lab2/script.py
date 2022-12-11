import os
import argparse
import subprocess

def check_mtu(mtu, destination, counter, verbose=False):
    cmd = ["ping", "-c", str(counter), "-M", "do", "-s", str(mtu), destination]
    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    if verbose:
        print("Ping exit code: " + str(result.returncode))
        print("Ping stdout:\n" + str(result.stdout))
        print("Ping stderr:\n" + str(result.stderr))
    return result.returncode

argument_parser = argparse.ArgumentParser()
argument_parser.add_argument('destination', help='dns name or ip address')
argument_parser.add_argument('-c', help='ping counter', default=1, type=int)
argument_parser.add_argument('-v', help='verbose output', default=False, type=bool)

args = argument_parser.parse_args()

counter = args.c
verbose = args.v
destination = args.destination

lower_bound = 0
upper_bound = 10000

check = check_mtu(lower_bound, destination, counter, verbose)
if check != 0:
    print("Can't ping to destination. Ping exit code: " + str(check))
    os._exit(1)

while lower_bound != upper_bound:
    mid = (lower_bound + upper_bound + 1) // 2
    res_code = check_mtu(mid, destination, counter, verbose)
    if res_code == 0:
        lower_bound = mid
    elif res_code == 1:
        upper_bound = mid - 1
    else:
        print("Can't find mtu. No reply from destination. Ping error code: " + str(res_code))
        os._exit(1)

print("Result mtu: " + str(lower_bound + 28) + " bytes")
