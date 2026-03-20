#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2026/3/19 15:39
# @Author : qy
# @File : app_service.py
from dataclasses import dataclass

from injector import inject

from internal.model import App
from pkg.sqlalchemy import SQLAlchemy


@inject
@dataclass
class AppService:
    db = SQLAlchemy()

    def create_app(self) -> App:
        # 1.创建模型的实体类
        app = App
