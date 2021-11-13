from logging import getLogger, StreamHandler, DEBUG
logger = getLogger(__name__)
handler = StreamHandler()
handler.setLevel(DEBUG)
logger.setLevel(DEBUG)
logger.addHandler(handler)
logger.propagate = False
logger.debug('hello')

import sqlite3
import os

def DatabaseRootDir():
    curdir = os.getcwd()
    #print(curdir)
    logger.debug(curdir)


def CreateDatabase(name:str):
    print("データベース[" + name + "]を作成")
    
    createName = name
    conn = sqlite3.connect(createName)
    conn.close()
    print("test")


DatabaseRootDir()