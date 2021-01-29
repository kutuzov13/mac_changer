# 1/usr/bin/env python
import subprocess
import optparse
import re


def get_arguments():
    """example passing arguments -i eth0 -m 00:15:5d:64:e6:7b"""
    parser = optparse.OptionParser()
    parser.add_option('-i', '--interface', dest='interface', help='')
    parser.add_option('-m', '--mac', dest='new_mac', help='New MAC address')
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error('[-] Please specify an interface, use --help for more info.')
    elif not options.new_mac:
        parser.error('[-] Please specify a new mac, use --help for more info.')
    return options


def change_mac(interface, new_mac):
    print(f'[+] Changing MAC address for {interface} to {new_mac}')
    subprocess.call(['sudo', 'ifconfig', interface, 'down'])
    subprocess.call(['sudo', 'ifconfig', interface, 'hw', 'ether', new_mac])
    subprocess.call(['sudo', 'ifconfig', interface, 'up'])


def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(['ifconfig', interface])
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result.decode('UTF-8'))
    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print('[-] Could not read MAC address.')


# Get arguments input user
options = get_arguments()
current_mac = get_current_mac(options.interface)
print(f'Current MAC = {str(current_mac)}')

# Edit MAC-address
change_mac(options.interface, options.new_mac)

# Complete change mac-address
current_mac = get_current_mac(options.interface)
if current_mac == options.new_mac:
    print(f'[+] MAC address was successfully changed to {current_mac}')
else:
    print('[-] MAC address did not get changed.')
