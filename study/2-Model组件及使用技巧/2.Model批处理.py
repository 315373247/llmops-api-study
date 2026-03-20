#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2026/1/8 09:37
# @Author : Administrator
# @File : 2.Model批处理.py
# @Project : llmops-api
# @Software: PyCharm
"""

"""
from datetime import datetime

import dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

dotenv.load_dotenv()

# 1.编排prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", "你是OpenAI开发的聊天机器人，请回答用户的问题，现在的时间是{now}"),
    ("human", "{query}")
]).partial(now=datetime.now())

# 2.创建大语言模型
llm = ChatOpenAI(model="gpt-3.5-turbo-16k")
prompt_value1 = prompt.invoke({"query": "你好，你是？"})
prompt_value2 = prompt.invoke({"query": "请讲一个程序员的冷笑话"})
ai_messages = llm.batch([
    prompt_value1,
    prompt_value2
])
print(ai_messages)
for ai_message in ai_messages:
    print(ai_message.content)
    print("================")
