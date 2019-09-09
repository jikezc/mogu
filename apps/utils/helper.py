# encoding: utf-8
# Author  : 小金
# File    : helper.py
# Time    : 2019/9/9 17:02
from redis import Redis


def get_redis_connection(option):
	return Redis(host=option.get("host"), port=option.get("port"), db=option.get("db"))