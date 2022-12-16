import socketserver as server
import termcfg as config
import base64, time
from termbase import *
from getpass import getpass

svraddr = ("0.0.0.0", 1145)
realsvraddr = ("127.0.0.1", 1145)
class TerminalCore(server.BaseRequestHandler):
    def handle(self):
        while True:
            data = self.request.recv(1024).strip()

def loginTerm(user = "#$@$#_invaild_user_#$@$#"):
    if user == "#$@$#_invaild_user_#$@$#":
        raise TerminalException("Invaild user!! Are you sure LKTUM file not broken or moved?")
    if isTerminalRunning():
        print("Oh, Terminal is running! ")
    else:
        print("Terminal not started. Starting terminal...")
        svr = server.ThreadingTCPServer(svraddr, TerminalCore)
        svr.serve_forever()
    passwd = getpass("Please input password (user: "+user+" - If this user not have password, You just press <Enter>): ")
    print("Creating session...")
    passwd = base64.b64encode(passwd)
    sign = base64.b64encode("USER: {}; PASSWORD: {}; SALT: {}".format(user, passwd, time.time()))
    createSession(user, sign, realsvraddr)

if __name__ == "__main__":
    raise RuntimeError("Don't open this file!!! This file is a LKTerm system plugin!!! (1)")