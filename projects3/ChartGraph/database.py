
import pl_logtest
import sqlite3
import os
import subprocess
from subprocess import PIPE


# 
logger = pl_logtest.Setup(__name__)

#
def DatabaseRootDir():
    curdir = os.getcwd()
    #print(curdir)
    logger.debug(curdir+"/database/")

#
def CreateDatabase(path:str):
    print("データベース[" + path + "]を作成")
    
    createName = path
    conn = sqlite3.connect(createName)
    conn.close()
   
# 
def RunQuery(dbPath:str, queryPath:str):
     msg="sqlite3 "+dbPath+" < "+queryPath
     subprocess.run(msg, shell=True, text=True)
 	
 	

#
