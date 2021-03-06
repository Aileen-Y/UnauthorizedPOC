#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Zookeeper未授权访问漏洞验证脚本

import os
import sys
from loguru import logger

LOG = "./results.txt"
LogFile_LEVEL = 'DEBUG'
CLI_LEVEL = 'INFO'
logger.remove()
logger.add(
    "%s" % LOG, level=('%s' % LogFile_LEVEL))
logger.add(sys.stderr, level=('%s' % CLI_LEVEL), enqueue=True)  # 命令终端日志级别默认为INFO


def read_file(file_path):
    if not os.path.exists(file_path):
        print('Please create a file: ips.txt !')
        sys.exit(0)
    else:
        with open(file_path, "r") as source:
            for ip in source:
                ZookeeperCheck(ip)


def ZookeeperCheck(ip):
    try:
        command = "echo envi | nc %s 2181" % ip.replace("\n", "")
        # command = "echo envi | nc {} 2181".format(ip).replace("\n","")
        with os.popen(command, "r") as p:
            result = p.read()
            if "Environment:" in result:
                logger.info("Log In Success! {}".format(ip))
            else:
                logger.info("Something Wrong! {}".format(ip))
    except Exception as error:
        print(error)
        logger.info("Connection Refused! {}".format(ip))


if __name__ == '__main__':
    print("==========开始验证==========")
    file_path = "ips.txt"
    read_file(file_path)
    print("==========Ending==========")
