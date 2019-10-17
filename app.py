import os
import logging
import time
import logging.handlers

BASE_URL= "http://182.92.81.159/api/sys/"

PRO_PATH=os.path.dirname(os.path.abspath(__file__))

TOKEN = None

def log_config():
    #获取日志对象
    logger = logging.getLogger()
    logger.setLevel(level=logging.INFO)
    #设置日志处理器
    to1 = logging.StreamHandler()
    file = PRO_PATH+"/log/IHRM"+time.strftime("%Y%m%d%H%M%S")+".log"
    to2=logging.handlers.TimedRotatingFileHandler(filename=file,when="h",interval=1,backupCount=1,encoding="utf-8")

    #设置格式化器
    fmt = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s"
    formatter=logging.Formatter(fmt)

    #组织上述对象
    to1.setFormatter(formatter)
    to2.setFormatter(formatter)
    logger.addHandler(to1)
    logger.addHandler(to2)
















