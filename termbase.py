from socket import socket, AF_INET, SOCK_STREAM
from socket import error as SocketError
from time import time
import termcfg as config
class TerminalException(Exception): ...

def getPathOfPhysicalPC(fpath:str) -> str:
    return "./lktermfs"+fpath

def gpoppc(fpath:str) -> str:
    return getPathOfPhysicalPC(fpath)

def getValue(_str: str) -> str:
    return _str.replace(" ","").split(":")[1]

def isExpired(_salt: float, _waitTime: float) -> bool:
    if _salt + _waitTime < time(): return True
    return False

def getWelcomeScreen():
    wsf = open(gpoppc(config.welcomeScreenFilePath), "r", encoding="utf-8")
    return wsf.read()

def isTerminalRunning():
    try:
        conn = socket(AF_INET,SOCK_STREAM)
        conn.settimeout(10)
        conn.connect(("127.0.0.1",1145))
        conn.close()
        return True
    except SocketError:
        return False

def createSession(user: str, signkey: str, serverAddress: tuple[str,int]):
    userdb = open(gpoppc)

if __name__ == "__main__":
    raise RuntimeError("Don't open this file!!! This file is a LKTerm system plugin!!! (1)")