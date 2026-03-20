#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2026/3/19 11:01
# @Author : qy
# @File : default_config.py


DEFAULT_CONFIG = {
    # wtf配置
    "WTF_CSRF_ENABLED": "False",

    # SQLALCHEMY数据库配置
    "SQLALCHEMY_DATABASE_URI": "",
    "SQLALCHEMY_POOL_SIZE": "30",
    "SQLALCHEMY_POOL_RECYCLE": "3600",
    "SQLALCHEMY_ECHO": "True",
}
