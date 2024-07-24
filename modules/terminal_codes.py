'''
This module provides codes for terminal usage    
'''
# Colors
clear: str = "\x1b[0m"
c: str = "\x1b[0m"
bold: str = "\x1b[1m"
b: str = "\x1b[1m"
cb: str = "\x1b[0m\x1b[1m"
black: str = "\x1b[30m"
cblack: str = "\x1b[0m\x1b[30m"
bblack: str = "\x1b[1m\x1b[30m"
cbblack: str = "\x1b[0m\x1b[1m\x1b[30m"
red: str = "\x1b[31m"
cred: str = "\x1b[0m\x1b[31m"
bred: str = "\x1b[1m\x1b[31m"
cbred: str = "\x1b[0m\x1b[1m\x1b[31m"
green: str = "\x1b[32m"
cgreen: str = "\x1b[0m\x1b[32m"
bgreen: str = "\x1b[1m\x1b[32m"
cbgreen: str = "\x1b[0m\x1b[1m\x1b[32m"
yellow: str = "\x1b[33m"
cyellow: str = "\x1b[0m\x1b[33m"
byellow: str = "\x1b[1m\x1b[33m"
cbyellow: str = "\x1b[0m\x1b[1m\x1b[33m"
blue: str = "\x1b[34m"
cblue: str = "\x1b[0m\x1b[34m"
bblue: str = "\x1b[1m\x1b[34m"
cbblue: str = "\x1b[0m\x1b[1m\x1b[34m"
magenta: str = "\x1b[35m"
cmagenta: str = "\x1b[0m\x1b[35m"
bmagenta: str = "\x1b[1m\x1b[35m"
cbmagenta: str = "\x1b[0m\x1b[1m\x1b[35m"
cyan: str = "\x1b[36m"
ccyan: str = "\x1b[0m\x1b[36m"
bcyan: str = "\x1b[1m\x1b[36m"
cbcyan: str = "\x1b[0m\x1b[1m\x1b[36m"
gray: str = "\x1b[90m"
cgray: str = "\x1b[0m\x1b[90m"
bgray: str = "\x1b[1m\x1b[90m"
cbgray: str = "\x1b[0m\x1b[1m\x1b[90m"
grey: str = "\x1b[90m"
cgrey: str = "\x1b[0m\x1b[90m"
bgrey: str = "\x1b[1m\x1b[90m"
cbgrey: str = "\x1b[0m\x1b[1m\x1b[90m"
light_red: str = "\x1b[91m"
clight_red: str = "\x1b[0m\x1b[91m"
blight_red: str = "\x1b[1m\x1b[91m"
cblight_red: str = "\x1b[0m\x1b[1m\x1b[91m"
light_green: str = "\x1b[92m"
clight_green: str = "\x1b[0m\x1b[92m"
blight_green: str = "\x1b[1m\x1b[92m"
cblight_green: str = "\x1b[0m\x1b[1m\x1b[92m"
light_yellow: str = "\x1b[93m"
clight_yellow: str = "\x1b[0m\x1b[93m"
blight_yellow: str = "\x1b[1m\x1b[93m"
cblight_yellow: str = "\x1b[0m\x1b[1m\x1b[93m"
light_blue: str = "\x1b[94m"
clight_blue: str = "\x1b[0m\x1b[94m"
blight_blue: str = "\x1b[1m\x1b[94m"
cblight_blue: str = "\x1b[0m\x1b[1m\x1b[94m"
light_magenta: str = "\x1b[95m"
clight_magenta: str = "\x1b[0m\x1b[95m"
blight_magenta: str = "\x1b[1m\x1b[95m"
cblight_magenta: str = "\x1b[0m\x1b[1m\x1b[95m"
light_cyan: str = "\x1b[96m"
clight_cyan: str = "\x1b[0m\x1b[96m"
blight_cyan: str = "\x1b[1m\x1b[96m"
cblight_cyan: str = "\x1b[0m\x1b[1m\x1b[96m"

# Terminal manipulation
delete: str = "\x1b[1A\x1b[2K"
d: str = "\x1b[1A\x1b[2K"

def delete_lines(num: int = 1) -> None:
    '''
    Delete lines printed on a terminal

    Args:
        num (int, optional): How many lines to delete. Defaults to 1.
    '''
    while num > 0:
        print(delete, end="")
        num -= 1