'''
Hi there!
This file is terminal config file!
DON'T MODIFY THIS FILE AT ANY TIME!
BECAUSE MODIFY THIS FILE MAYBE CAN MAKE TERMINAL CRASH!!!
'''

# FILE OPTIONS
welcomeScreenFilePath = "/var/system/welcome.txt"

# SYSTEM FUNCTIONS
def getPathOfPhysicalPC(fpath:str) -> str:
    return "./lktermfs"+fpath
gpoppc = getPathOfPhysicalPC

def getWelcomeScreen():
    wsf = open(gpoppc(welcomeScreenFilePath), "r", encoding="utf-8")
    return wsf.read()

if __name__ == "__main__":
    raise RuntimeError("Don't open this file!!! This file is a LKTerm system plugin!!!")