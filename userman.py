from base64 import b64decode, b64encode
from time import time
from termcfg import userFile
from termbase import TerminalException, getValue, isExpired, gpoppc
def encodeAuthText(_user: str, _passwd: str) -> str:
    salt = time()
    return "USER: {}; PASSWD: {}; SALT: {}".format(b64encode(_user), b64encode(_passwd), b64encode(salt))
def getUserInfo(_user):
    ulist = list(open(gpoppc(userFile),"r",encoding="utf-8").read())
    for user in ulist:
        if dict(b64decode(user))["user"] == _user:
            return dict(b64decode(user))
    raise TerminalException("User not found! (3)")
def vaildateUser(user: str, sign: str):
    _user = _passwd = ""
    decodedSign = b64decode(sign).replace(" ","").split(";")
    for a in decodedSign:
        if a.find("USER:") != -1:
            if getValue(a) != user: raise TerminalException("Authenticate error! (-1)")
        elif a.find("PASSWD:") != -1:
            _passwd = getValue(a)
        elif a.find("SALT"):
            if isExpired(float(getValue(a)), 120):
                raise TerminalException("Invaild session token! (2)")
    getUserInfo(_user)