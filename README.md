# MAC-changer
Programm for change MAC-address 

## Installation

Clone repo https://github.com/kutuzov13/mac_changer.git

```
The program is tested on Kali Linux.
```

## Import

```python
import subprocess
import optparse
import re
```

## Description
```
Changes the MAC address when executing the script with the parameters: -i <name_interface> -m <new_mac_adress>

Next, the script will make changes from the current MAC address to <new_mac_adress>

If the script is successfully executed, the following is printed on the screen:

MAC address was successfully changed to <current_mac_adress>
```
