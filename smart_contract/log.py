#!/usr/bin/env python
# encoding: utf-8
'''
@author: caroline
@license: (C) Copyright 2019-2022, Node Supply Chain Manager Corporation Limited.
@contact: caroline.fang.cc@gmail.com
@software: pycharm
@file: log.py
@time: 2020/3/13 4:58 pm
@desc:
'''

'''
import logging

logging.basicConfig(filename='example.log',
                    filemode='w',
                    format='%(asctime)s %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.DEBUG)

'''

'''
import logging.config

# 通过yaml文件配置logging
import yaml

f = open("log_conf.yaml")
dic = yaml.load(f, Loader=yaml.FullLoader)
f.close()
logging.config.dictConfig(dic)
# 创建logger
logger = logging.getLogger('example.log')

# 输出日志
logger.debug('debug message')
logger.info('info message')
logger.warning('warning message')
logger.error('error message')
logger.critical('critical message')

'''

import yaml
import logging.config
import os


def set_log_cfg(default_path="log_conf.yaml", default_level=logging.INFO, env_key="LOG_CFG"):
	path = default_path
	value = os.getenv(env_key, None)
	if value:
		path = value
	if os.path.exists(path):
		with open(path, "r") as f:
			config = yaml.load(f, Loader=yaml.FullLoader)
			logging.config.dictConfig(config)
	else:
		logging.basicConfig(level=default_level)


def record_some_thing():
	logging.debug("Log level debug")
	logging.info("Log level info")
	logging.warning("Log level warning")
	logging.error("Log level error")



if __name__ == "__main__":
	set_log_cfg(default_path="log_conf.yaml")

