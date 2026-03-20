#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2025/12/25 11:30
# @Author : Administrator
# @File : conftest.py
# @Project : llmops-api
# @Software: PyCharm
import pytest

from app.http.app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client
