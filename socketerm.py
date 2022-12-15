import socketserver as server
import termcfg as config
from termbase import *

class TerminalCore(server.BaseRequestHandler):
    def handle(self):
        conn = self.request
        if conn:
            conn.sendall("--LOGIN SUCCESS--")
            conn.sendall(":welcomescreen")
            conn.sendall(config.getWelcomeScreen())
            conn.sendall(":/welcomescreen")
    
def addSession(user = "#$@$#_invaild_user_#$@$#"):
    if user == "#$@$#_invaild_user_#$@$#":
        raise TerminalException("Invaild user!! Are you sure LKTUI file not broken or moved?")

if __name__ == "__main__":
    raise RuntimeError("Don't open this file!!! This file is a LKTerm system plugin!!!")