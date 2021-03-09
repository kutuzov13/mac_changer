# MAC-changer
Programm for change MAC-address 

## Installation

```
git clone https://github.com/kutuzov13/mac_changer.git
```

The program is tested on Kali Linux.


## Import

```python
import subprocess
import optparse
import re
```
## Steps
```text
1. Execute and read ifconfig
2. Read the mac address from output
3. Check if MAC in ifconfig is what the user requested
4. Print appropriate message.
   If the script is successfully executed, the following is printed on the screen:
   MAC address was successfully changed to <current_mac_adress>
```

## Example
```bash
python3.8 mac-change.py -i <name_interface> -m <mac-adrees>
```

