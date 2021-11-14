
import pl_logtest
import sqlite3
import os



def DatabaseRootDir():
    curdir = os.getcwd()
    #print(curdir)
    logger.debug("1234"+curdir)


def CreateDatabase(name:str):
    print("データベース[" + name + "]を作成")
    
    createName = name
    conn = sqlite3.connect(createName)
    conn.close()
    print("test")

#print(__name__)
logger = pl_logtest.Setup(__name__)
DatabaseRootDir()