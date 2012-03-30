import sys, time, platform, math
try:
        import MySQLdb,ConfigParser,os
        from optparse import OptionParser
        from ds import *
except ImportError:
        print >> sys.stderr, ""

class DatabaseSource:
    def __init__(self,host,user,passwd,port=3306):
        self.host       = host
        self.username   = user
        self.passwd     = passwd
        self.port       = port
        self.initDS()

    def initDS(self):
        self.conn = self._getConnection()
        self.cursor = self._getCursor()
        self.globalVars = self._queryGlobalVars()
        self._version()

    def _getConnection(self):
        try:
            conn = MySQLdb.connect(host=self.host, user=self.username,passwd=self.passwd,port=self.port)
        except Exception,e:
            print e
            sys.exit()
        return conn

    def _getCursor(self):
        return self.conn.cursor()

    def _queryGlobalVars(self):
        self.cursor.execute("show global variables")
        var_rs = self.cursor.fetchall()
        varis = {}
        for v in var_rs:
            varis[v[0]] = v[1]
        return varis

    def _version(self):
        version_str = self.getVar("version")
        versions = version_str.split(".")
        self.version_main = int(versions[0])
        self.version_middle = int(versions[1])
        details = versions[2].split("-")
        self.version_tail = int(details[0])
        
    def getVar(self,name,is_float=0):
        try:
            v = self.globalVars[name]
            if is_float:
                return float(v)
            else:
                return v
        except KeyError:
            return False

    def destroy(self):
        self.cursor.close()
        self.conn.close()