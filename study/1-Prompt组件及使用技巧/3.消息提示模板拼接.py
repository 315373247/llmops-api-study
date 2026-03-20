#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2026/1/7 20:52
# @Author : Administrator
# @File : 3.消息提示模板拼接.py
# @Project : llmops-api
# @Software: PyCharm
"""

"""
from langchain_core.prompts import ChatPromptTemplate

system_chat_prompt = ChatPromptTemplate.from_messages([
    ("system", "你是OpenAI开发的聊天机器人，请根据用户的提问进行回复，我叫{username}")
])
human_chat_prompt = ChatPromptTemplate.from_messages([
    ("human", "{query}")
])
chat_prompt = system_chat_prompt + human_chat_prompt
print(chat_prompt.invoke({
    "username": "Alice",
    "query": "你好，请问有什么可以帮助您？"
}).to_string())
