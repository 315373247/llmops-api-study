#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2026/3/19 10:41
# @Author : qy
# @File : app_schema.py

from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length


class CompletionReq(FlaskForm):
    """基础聊天接口请求验证"""
    query = StringField("query", validators=[
        DataRequired(message="用户的提问是必填"),
        Length(max=2000, message="用户的提问长度不能超过2000")
    ])
