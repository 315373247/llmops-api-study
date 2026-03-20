#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2026/3/19 12:04
# @Author : qy
# @File : response.py
from dataclasses import dataclass, field
from typing import Any

from flask import jsonify

from .http_code import HttpCode


@dataclass
class Response:
    code: HttpCode.SUCCESS
    message: str
    data: Any = field(default_factory=dict)


def json(data: Response = None):
    """基础的响应接口"""
    return jsonify(data), 200


def success_json(data: Response = None):
    """成功的响应接口"""
    return json(Response(code=HttpCode.SUCCESS, message="", data=data))


def fail_json(data: Response = None):
    """失败的响应接口"""
    return json(Response(code=HttpCode.FAIL, message="", data=data))


def validate_error_json(errors: dict = None):
    """验证错误的响应接口"""
    first_key = next(iter(errors))
    if first_key is not None:
        msg = errors.get(first_key)[0]
    else:
        msg = ""
    return json(Response(code=HttpCode.VALIDATE_ERROR, message=msg, data=errors))


def message(code: HttpCode, msg: str = ""):
    """基础的消息响应，固定返回消息提示，数据固定为空字典"""
    return json(Response(code=code, message=msg, data={}))


def success_message(msg: str = ""):
    """成功的消息响应"""
    return message(HttpCode.SUCCESS, msg)


def fail_message(msg: str = ""):
    """失败的消息响应"""
    return message(HttpCode.FAIL, msg)


def not_found_message(msg: str = ""):
    """未找到的消息响应"""
    return message(HttpCode.NOT_FOUND, msg)


def unauthorized_message(msg: str = ""):
    """未授权的消息响应"""
    return message(HttpCode.UNAUTHORIZED, msg)


def forbidden_message(msg: str = ""):
    """无权限的消息响应"""
    return message(HttpCode.FORBIDDEN, msg)
