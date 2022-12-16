from socket import socket, AF_INET, SOCK_STREAM
from socket import error as SocketError
from time import time
import termcfg as config
from userman import vaildateToken
class TerminalException(Exception): ...

def getPathOfPhysicalPC(fpath:str) -> str:
    return "./lktermfs"+fpath

def gpoppc(fpath:str) -> str:
    return getPathOfPhysicalPC(fpath)

class StringifyDictExtract():
    '''Extract name/value & to dict from stringify dict.
    CAUTION: Now it doesn't support list (value type)!!!'''
    def getName(self, string: str) -> str:
        return string.replace(" ","").split(":")[0]
    def getValue(self, string: str) -> str:
        return string.replace(" ","").split(":")[1]
    def toDict(self, string: str, sep = ",") -> dict:
        string = string.replace(" ","")
        ls = string.split(sep)
        ret = ""
        retStart = "dict("
        retEnd = ")"
        ret += retStart
        count = 0
        for item in ls:
            ret += self.getName(item) + "=" + self.getValue(item)
            if count != len(ls) - 1:
                ret += ","
            count += 1
        ret += retEnd
        return eval(ret)

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

def createSession(user: str, token: str, serverAddress: tuple[str,int]):
    if vaildateToken(user,token):
        okconn = socket(AF_INET, SOCK_STREAM)
        okconn.settimeout(10)
        okconn.connect(serverAddress)
        okconn.sendall("--AUTHENTICATE SUCCESS--")
        okconn.close()

if __name__ == "__main__":
    raise RuntimeError("Don't open this file!!! This file is a LKTerm system plugin!!! (1)")