#=================
# ログテスト
#=================
import logging
from logging import getLogger

def GetLevel():
    return logging.DEBUG


def Setup(moduleName):
    # ログの設定を追加
    # これは全てのファイルで設定を行います
    # getLogger関数の第一引数に設定された文字列が、そのロガーの名前になる 
    logger = getLogger(moduleName)
    
    # 標準出力(コンソール)にログを出力するハンドラを生成する
    handler = logging.StreamHandler()
    
    # フォーマッタを定義する（第一引数はメッセージのフォーマット文字列、第二引数は日付時刻のフォーマット文字列
    fmt = logging.Formatter("%(asctime)s : [%(name)s : %(levelname)s] %(message)s", "%Y-%m-%dT%H:%M:%S")
    # フォーマッタをハンドラに紐づける
    handler.setFormatter(fmt)
    logger.addHandler(handler)
    
    # 表示するレベルを設定
    # ログレベルは、CRITICAL > ERROR > WARNING > INFO > DEBUG > NOTSET の順で高くなります。
    logger.setLevel(GetLevel())
    #logger.setLevel(logging.DEBUG)
    logger.propagate = False
    #print(moduleName)
    return logger

