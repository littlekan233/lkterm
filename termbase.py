from socket import socket, AF_INET, SOCK_STREAM
from socket import error as SocketError
class TerminalException(Exception): ...

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
    raise RuntimeError("Don't open this file!!! This file is a LKTerm system plugin!!!")